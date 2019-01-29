#!/usr/bin/env ruby

class TrackGrid

    attr_reader :grid, :carts

    def initialize(file)
        # Read in grid from file
        @grid = Array.new { Array.new("")}
        IO.foreach(file) do |line|
            line.chomp!
            @grid.push(line.chars)
        end
        # @grid = @grid.transpose

        # Generate carts from grid, replacing with appropriate track piece
        @carts = []
        @grid.each_index do |x|
            @grid[x].each_index do |y|
                if @grid[x][y] =~ /[<>]/
                    @carts.push Cart.new(x, y, @grid[x][y])
                    @grid[x][y] = "-"
                elsif @grid[x][y] =~ /[v^]/
                    @carts.push Cart.new(x,y, @grid[x][y])
                    @grid[x][y] = "|"
                end
            end
        end
    end

    # Returns array of carts sorted by position
    def sortCarts
        # puts "orig"
        # @carts.each {|i| p i}
        # puts "sorted"
        sorted = @carts.sort { |a, b| (a.x == b.x) ? a.y <=> b.y : a.x <=> b.x }.each
        # sorted.each {|i| p i}
        sorted
    end

    def tick
        # Update carts sequentially
        # puts "tick"
        to_remove = []
        self.sortCarts.each do |c|
            # p c
            c.tick(@grid[c.x][c.y])
            crashes = c.crashed?(@carts - [c])
            if crashes
                to_remove.push c
                to_remove.push crashes
                puts "Crash b'twn #{c.str} and #{crashes.str}"
            end
            to_remove.uniq!
        end
        @carts = @carts - to_remove
    end

    # def crashes?
    #     crashes = ""
    #     @carts.each do |i|
    #         @carts.each do|j|
    #             next if i == j
    #             if i.x == j.x && i.y == j.y
    #                 crashes += "crash @ #{i.y},#{i.x}\n"
    #                 # p i
    #                 # p j
    #                 # puts crashes
    #                 # puts "putting x at #{i.x} #{i.y}"
    #                 # @grid[i.x][i.y] = "X"
    #             end
    #         end
    #     end
    #     if crashes.length > 0
    #         @carts.each &:display
    #         crashes
    #     else
    #         nil
    #     end
    # end

    def outputGrid
        output = ""
        @grid.each_index do |x|
            l = @grid[x].join('')
            @carts.each { |c|
                l[c.y] = c.d if c.x == x
            }
            output += l + "\n"
        end
        output
    end

    def display
        puts self.outputGrid
        # puts @carts
    end

    class Cart

        attr_reader :x, :y, :d

        def initialize(x, y, d)
            @x = x
            @y = y
            @d = d
            @last_turn = [:right, :left, :straight]
        end

        def tick(track)
            case track
            when "-"
                @y += 1 if @d == ">"
                @y -= 1 if @d == "<"
                if @d =~ /[v^]/
                    puts "ERROR"
                    exit
                end
            when "|"
                @x += 1 if @d == "v"
                @x -= 1 if @d == "^"
                if @d =~ /[<>]/
                    puts "ERROR"
                    exit
                end
            when "\\"
                if @d == ">"
                    @x += 1 
                    self.turnCW
                elsif @d == "<"
                    @x -= 1 
                    self.turnCW
                elsif @d == "^"
                    @y -= 1
                    self.turnCCW
                elsif @d == "v"
                    @y += 1
                    self.turnCCW
                end
            when "/"
                if @d == ">"
                    @x -= 1
                    self.turnCCW
                elsif @d == "<"
                    @x += 1
                    self.turnCCW
                elsif @d == "^"
                    @y += 1
                    self.turnCW
                elsif @d == "v"
                    @y -= 1
                    self.turnCW
                end
            when "+"
                # Get next turn direction
                @last_turn.rotate!(1)
                # puts "cart turning #{@last_turn.first}"
                if @last_turn.first == :straight
                    @y += 1 if @d == ">"
                    @y -= 1 if @d == "<"
                    @x += 1 if @d == "v"
                    @x -= 1 if @d == "^"
                elsif @last_turn.first == :left
                    @x -= 1 if @d == ">"
                    @x += 1 if @d == "<"
                    @y += 1 if @d == "v"
                    @y -= 1 if @d == "^"
                    self.turnCCW
                elsif @last_turn.first == :right
                    @x += 1 if @d == ">"
                    @x -= 1 if @d == "<"
                    @y -= 1 if @d == "v"
                    @y += 1 if @d == "^"
                    self.turnCW
                end
            when ""
                puts "ERROR: CART OFF TRACK"
                exit(false)
            end
        end

        def crashed?(carr)
            carr.each do |c|
                if @x == c.x && @y == c.y
                    return c
                end
            end
            false
        end

        def turnCW
            # puts "turning cw"
            case @d
            when "<"; @d = "^"
            when "^"; @d = ">"
            when ">"; @d = "v"
            when "v"; @d = "<"
            end
        end

        def turnCCW
            # puts "turning ccw"
            case @d
            when ">"; @d = "^"
            when "v"; @d = ">" 
            when "<"; @d = "v" 
            when "^"; @d = "<" 
            end
        end

        def str
            "X: #{@y} Y: #{@x} D: #{@d}"
        end

        def display
            puts self.str
        end
        
    end
end

def part1(file)
    tg = TrackGrid.new(file)
    i = 0
    while true
        # input = gets.strip
        # return if input == "q"
        i += 1
        puts i if i % 10 == 0
        tg.tick
    end
end

def part2(file)
    tg = TrackGrid.new(file)
    i = 0
    while tg.carts.length > 1
        # input = gets.strip
        # return if input == "q"
        puts tg.carts.length
        tg.tick
    end
    tg.carts[0].display
end 

# input = "13_test.txt"
# input = "13_test2.txt"
input = "13_input.txt"
# part1(input)
# 134,55 incorrect
# 135,44 incorrect
# 3,14 incorrect
# 57,104 correct

part2(input)
# 67,74

