#!/usr/bin/env ruby
require 'pp'

class Grid

    attr_reader :pixels

    def initialize(file)
        @time = 0
        @pixels = []
        IO.foreach(file) do |line|
            nums = line.scan(/-?\d+/).map(&:to_i)
            @pixels.push( Pixel.new(*nums))
        end
        # rezero
        # updateGrid
    end

    def shiftPixels(x, y)
        # puts "shifting by #{x} and #{y}"
        @pixels.each do |p|
            p.x += x
            p.y += y
        end
    end

    def rezero
        minx, miny = self.getBounds
        # p self.getBounds
        shiftPixels(minx.abs, 0) if minx < 0
        shiftPixels(0, miny.abs) if miny < 0
        shiftPixels(-minx, 0) if minx > 0
        shiftPixels(0, -miny) if miny > 0
    end

    def pixelStatus(px, py)
        @pixels.each do |p|
            return true if p.x == px && p.y == py
        end
        return false
    end

    def update(deltaTime = 1)
        @time += deltaTime
        self.updatePixels(deltaTime)
        self.rezero
        self.updateGrid
    end

    def updatePixels(time = 1)
        @pixels.each do |p|
            p.update(time)
            # p p
        end
    end

    def updateGrid
        minx, miny, maxx, maxy = self.getBounds
        @grid = []
        (0..maxx).each do |x|
            @grid[x] = []
            (0..maxy).each do |y|
                if pixelStatus(x, y)
                    # puts "point #{x} #{y}"
                    @grid[x].push "#"
                else
                    @grid[x].push "."
                end
            end
        end
    end

    def display
        # pp @grid
        puts "Time: #{@time}"
        transgrid = @grid.transpose
        transgrid.each do |line|
            puts line.join('')
        end
    end

    def getBounds
        minx, miny, maxx, maxy = @pixels[0].x, @pixels[0].y, @pixels[0].x, @pixels[0].y
        @pixels.each do |p|
            minx = p.x - 10 if p.x < minx
            miny = p.y - 10 if p.y < miny
            maxx = p.x + 10 if p.x > maxx
            maxy = p.y + 10 if p.y > maxy
        end
        [minx, miny, maxx, maxy]
    end

end

class Pixel

    attr_accessor :x, :y

    def initialize(x, y, vx, vy)
        @x = x
        @y = y
        @vx = vx
        @vy = vy
    end

    def update(time = 1)
        @x += @vx * time
        @y += @vy * time
    end

    def display
        # puts "<#{@x}, #{@y}> <#{@vx}, #{@vy}>"
        printf "<%3d, %3d> <%3d, %3d>\n", @x, @y, @vx, @vy
    end
end

def part1(file)
    g = Grid.new(file)

    # Find minimal area, which likely corresponds to message
    time = 0
    last_area = nil
    while true
        time += 1
        minx, miny, maxx, maxy = g.getBounds
        new_area = (maxx - minx) * (maxy - miny)
        if last_area && new_area > last_area
            puts "Minimum @ #{time}"
            break
        end
        last_area = new_area
        g.updatePixels(1)
        g.rezero
    end

    g = Grid.new(file)
    g.update(time - 10)
    # g.pixels.each(&:display)
    # p g.getBounds
    while true
        option = gets
        if option.strip == "q"
            return
        else
            puts ""
            g.display
            g.update
        end
    end
end

# input = "10_test.txt"
input = "10_input.txt"
part1(input) #ERKECKJJ