#!/usr/bin/env ruby

require 'matrix'

class Reservoir
    @@area_total = 0

    def initialize(file)
        @segments = []
        IO.foreach(file) do |line|
            @segments << Segment.new(line)
        end

        # Find min and max x and y
        @ys = [@segments[0].min_y, @segments[0].max_y]
        @xs = [@segments[0].min_x, @segments[0].max_x]
        @segments.each do |s|
            @xs[0] = s.min_x if s.min_x < @xs[0]
            @xs[1] = s.max_x if s.max_x > @xs[1]
            @ys[0] = s.min_y if s.min_y < @ys[0]
            @ys[1] = s.max_y if s.max_y > @ys[1]
        end
        # Extend x-limits by one to each side
        @xs[0] -= 1
        @xs[1] += 1
        puts "LIMITS: X: #{@xs} Y: #{@ys}"

        # Generate grid with sand "."
        @grid = []
        (@xs[1] - @xs[0] + 1).times do
            @grid << ["."] * ( @ys[1] - @ys[0] + 1)
        end

        # Generate clay from segments
        @segments.each do |s|
            # puts s.to_s
            s.positions.each do |pos|
                # puts "Pos #{pos}"
                # puts pos[0] - @xs[0]
                @grid[ pos[0] - @xs[0] ][ pos[1] - @ys[0] ] = "#"
            end
        end

        @waters = []
        @wetarea = []
    end


# Add water at position
#  
# If clay below, add water to left and to right. Goto 1 for each new water
# If water below, add water to left and to right. Goto 1 for each new water
# If no clay below, move water down one below. Goto 2 for current water

    def simulate
        initWater = Vector[ 500 - @xs[0], 0]
        # while true
        addWater(initWater)
        # end
        # while true
        #     self.spawn(initWater)
        #     self.update
        # end
    end

    def addWater(pos)
        curr_water = Water.new(pos, self)
        water_row = [ curr_water ]

        # puts self.to_s({pos => "X"})      
        puts "#{self.waterArea} #{pos}"
        if self.waterArea != @@area_total
            @@area_total = self.waterArea
            out_counter = 0
            out_file = "17_temp#{out_counter}.txt"
            while File.file?(out_file) do
                out_counter += 1
                out_file = "17_temp#{out_counter}.txt"
            end
            File.open(out_file, 'w') do |f|
                f.puts self.to_s({pos => "X"})      
            end
        end

        return if hasWaterAt?(pos)
        # If at bottom of map, return
        if outOfBounds?( curr_water.pos + Vector[0,1] )
            @waters << curr_water
            return
        end
        
        # If empty space below, addWater at that position
        if clear?(curr_water.pos + Vector[0,1])
            addWater( curr_water.pos + Vector[0,1] )
        end

        # If solid support beneath, add water to each side
        if !clear?( curr_water.pos + Vector[0,1])

            # Add left
            cp = curr_water.pos - Vector[1, 0]
            while clear?(cp) do
                water_row << Water.new(cp, self)
                if clear?(cp + Vector[0,1] )
                    addWater(cp + Vector[0,1] ) 
                    break
                end
                # puts self.to_s({cp => "X"})
                cp -= Vector[1, 0]
            end

            # Add right
            cp = curr_water.pos + Vector[1, 0]
            while clear?(cp) do
                water_row << Water.new(cp, self)
                if clear?(cp + Vector[0,1] )
                    addWater(cp + Vector[0,1] ) 
                    break
                end
                # puts self.to_s({cp => "X"})
                cp += Vector[1, 0]
            end

            # Decide if all water is settled
            row_settled = water_row.map { |w| clear?( w.pos + Vector[0,1] ) }.none?
            water_row.each { |w| w.settled = row_settled }

            # Flow water downwards if possible
            # water_row.each do |w|
            #     addWater(w.pos + Vector[0,1] ) if clear?(w.pos + Vector[0,1] )
            # end
        end
        
        # puts self.to_s({pos => "X"})      
        @waters.concat water_row
        
    end

    def spawn(pos)
        cwater = Water.new(pos, self)
        @waters << cwater
    end

    def update
        # Sort waters by y (update biggest y to smallest y)
        @waters.sort! { |a,b| b.pos[1] <=> a.pos[1] }
        @waters.each do |w|
            # Move down if possible
            if clear?(w.pos + Vector[0,1])
                w.pos += Vector[0,1]
                next
            end
            move_vec = [ Vector[-1,0], Vector[1,0] ].sample
            if clear?(w.pos + move_vec)
                w.pos += move_vec
            end
        end
        display
    end

    def outOfBounds?(pos)
        pos[0] >= @grid.length || pos[1] >= @grid[ pos[0] ].length
    end

    def clear?(pos)
        if pos[0] >= @grid.length || pos[1] >= @grid[ pos[0] ].length
            return false
        else
            @grid[ pos[0] ][ pos[1] ] == "." && !hasWaterAt?(pos)
        end
    end

    def hasWaterAt?(pos)
        @waters.map{ |w| w.pos == pos && w.settled }.any?
    end

    def to_s(addons = nil)
        output = ""
        tg = @grid.transpose

        # Add water
        @waters.each do |w|
            if w.settled
                tg[ w.pos[1] ][ w.pos[0] ] = "~"
            else
                tg[ w.pos[1] ][ w.pos[0] ] = "|"
            end
        end

        # Add addiitonal stuff if available
        if addons
            addons.each do |k,v|
                tg[ k[1] ][ k[0] ] = v
            end
        end

        tg.each_with_index do |line, idx|
            output += line.join('') + "\n"
        end

        output
    end

    def waterArea
        wp = @waters.map { |w| w.pos }
        wp.uniq.length
    end

end

class Water
    
    attr_accessor :pos, :settled

    def initialize(pos, res)
        @pos = pos
        @res = res
        @settled = false
    end

    def canDrop?
        @res.clear?(@pos + Vector[0,1])
    end

end

class Segment
    def initialize(line)
        digits = line.scan(/\d+/).map(&:to_i)
        if line =~ /^x/
            @v1 = Vector[digits[0], digits[1]]
            @v2 = Vector[digits[0], digits[2]]
        else
            @v1 = Vector[digits[1], digits[0]]
            @v2 = Vector[digits[2], digits[0]]
        end
    end

    def positions
        pos = []
        (min_x..max_x).each do |x|
            (min_y..max_y).each do |y|
                pos << Vector[x, y]
            end
        end
        pos
    end

    def min_x; [ @v1[0], @v2[0]].min end
    def max_x; [ @v1[0], @v2[0]].max end
    def min_y; [ @v1[1], @v2[1]].min end
    def max_y; [ @v1[1], @v2[1]].max end

    def to_s
        "#{@v1} : #{@v2}"
    end
end

def part1(input)
    res = Reservoir.new(input)
    res.simulate

    puts "Final:"
    puts res.to_s
    puts "Total: #{res.waterArea}"
end

part1(ARGV.first)

# 13452 => too low
# 25499 => too low