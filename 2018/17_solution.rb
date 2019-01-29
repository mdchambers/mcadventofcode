#!/usr/bin/env ruby

require 'matrix'

class Reservoir
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
        initWater = Vector[ 500 - @xs[0], 1]
        # while true
        addWater(initWater)
        # end
        # while true
        #     self.spawn(initWater)
        #     self.update
        # end
    end

    def addWater(pos)
        cwater = Water.new(pos, self)
        # @wetarea << pos
        # puts self.to_s( {pos => "X"} )
        # puts "\n"

        # If at bottom of map, return
        if cwater.pos[1] + 1 >= @ys[1]
            return false
        end

        # Display updated board
        puts self.to_s({ pos => "x"}, true)
        
        # If no support, add water below current water
        if clear?(cwater.pos + Vector[0,1])
            addWater( cwater.pos + Vector[0,1])
            
        end

        # If water or clay support beneath, spread left and right
        if !clear?(cwater.pos + Vector[0,1])
            @waters << cwater

            lset = true
            rset = true

            # Right
            if clear?(cwater.pos + Vector[1,0])
                rset = addWater( cwater.pos + Vector[1,0] )
            end
            
            # Left
            if clear?( cwater.pos + Vector[-1, 0] )
                lset = addWater( cwater.pos + Vector[-1, 0] )
            end

            cwater.settled = lset && rset

            # If left not settled and right settled, unsettle right
            if ! lset && rset



        end
        return cwater.settled
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

    def clear?(pos)
        if pos[0] >= @grid.length || pos[1] >= @grid[ pos[0] ].length
            return false
        else
            @grid[ pos[0] ][ pos[1] ] == "." && !hasWaterAt?(pos)
        end
    end

    def hasWaterAt?(pos)
        waterpos = @waters.map { |w| w.pos }
        waterpos.include? pos
    end

    def to_s(addons = nil, wetarea = false)
        output = ""
        tg = @grid.transpose

        # Add wetarea if indicated
        if wetarea
            @wetarea.each do |w|
                tg[ w[1] ][ w[0] ] = "|"
            end
        end

        # Add water
        @waters.each do |w|
            tg[ w.pos[1] ][ w.pos[0] ] = "~"
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

class Water; end

def part1(input)
    res = Reservoir.new(input)
    res.simulate
end

part1(ARGV.first)
