#!/usr/bin/env ruby

class Point
    def initialize(line, offset = 0)
        @x, @y = line.scan(/\d+/).map &:to_i
        @x += offset
        @y += offset
    end

    def x
        @x
    end

    def y
        @y
    end

    def distance(nx, ny)
        ( @x - nx ).abs + ( @y - ny).abs
    end


end

class Grid
    def initialize(maxX, maxY)
        @grid = Array.new(maxX + 1) {Array.new(maxY + 1, 0)}
    end

    def dims
        [@grid.length, @grid[0].length]
    end

    def display
        out_grid = @grid.transpose
        out_grid.each do |line|
            line.each do |pos|
                print pos.to_s.rjust(3)
            end
            print "\n"
        end
    end

    def assign(x, y, val)
        @grid[x][y] = val
    end

    # Given an array of points, assign each position on the grid to the closest point
    def assignClosest(parr)
        self.dims[0].times do |i|
            self.dims[1].times do |j|
                distances = Array.new
                parr.each do |point|
                    distances << point.distance(i, j)
                end
                mins = distances.min(2)
                if mins[0] == mins[1]
                    @grid[i][j] = -1
                else
                    @grid[i][j] = distances.index(mins[0])
                end
            end
        end
    end

    def removeInfinites
        # Identify infinites
        infs = Array.new
        infs = infs | @grid.first.uniq | @grid.last.uniq
        @grid.each do | row |
            infs = infs | [row.first] | [row.last]
        end

        infs.each do |i|
            self.replaceAll(i, -1)
        end
    end

    def replaceAll(old_val, new_val)
        self.dims[0].times do |i|
            self.dims[1].times do |j|
                @grid[i][j] = new_val if @grid[i][j] == old_val
            end
        end
    end

    # Returns an hash of areas for each point
    # Infinite areas are represented with areas -1
    def getAreas
        self.removeInfinites
        totals = Hash.new(0)
        self.dims[0].times do |i|
            self.dims[1].times do |j|
                totals[@grid[i][j]] += 1
            end
        end
        totals[-1] = 0
        totals
    end

end

def part1(file)
    points = IO.readlines(file).map do |line|
        Point.new(line)
    end
    # points.each do |point|
    #     p point
    # end
    maxX, maxY = 0, 0 
    points.each do |point|
        maxX = point.x if point.x > maxX
        maxY = point.y if point.y > maxY
    end
    grid = Grid.new(maxX, maxY)
    puts grid.dims.join(" ")
    # grid.display 
    # puts ""
    grid.assignClosest(points)
    # grid.display 
    # puts ""
    totals = grid.getAreas
    # grid.display
    p totals
    p totals.values.max
end


def findAreaWithDistance(parr, start_x, start_y, end_x, end_y, dist = 10000)
    area = 0
    (start_x..end_x).each do |x|
        puts "On x #{x}" if x % 100 == 0
        (start_y..end_y).each do |y|
            # puts "on y #{y}" if y % 1000 == 0
            curr_dist = 0   
            parr.each do |point|
                curr_dist += point.distance(x, y)
            end
            area += 1 if curr_dist <= dist
        end
    end
    area
end

def part2(file)
    points = IO.readlines(file).map do |line|
        Point.new(line)
    end
    maxX, maxY = 0, 0 
    points.each do |point|
        maxX = point.x if point.x > maxX
        maxY = point.y if point.y > maxY
    end
    grid = Grid.new(maxX, maxY)
    puts grid.dims.join(" ")

    # total = findAreaWithDistance(points, -500, -500, 500, 500)
    # p total
    dim = 500
    old_val = nil
    while true
        total = findAreaWithDistance(points, -dim, -dim, dim, dim)
        puts "Dim: #{dim} Total: #{total}"
        dim += 100
        if ! old_val
            old_val = total
        elsif old_val == total
            puts "convergence found"
            puts total
            break
        end
    end
end


# input = "06_test.txt"
input = "06_input.txt"

# part1(input)
part2(input)