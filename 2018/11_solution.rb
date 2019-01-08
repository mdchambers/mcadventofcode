#!/usr/bin/env ruby

class PowerGrid
    def initialize(serial)
        @serial = serial
        @grid = Array.new(300) { Array.new(300, 0)}
        self.populatePowerValues
    end

    def populatePowerValues
        @grid.each_index do |x|
            @grid[x].each_index do |y|
                @grid[x][y] = powerValue(x + 1, y + 1)
            end
        end
    end

    def powerValue(x, y)
        rack_id = x + 10
        power = rack_id * y
        power += @serial
        power *= rack_id
        power = power.to_s[-3].to_i
        power -= 5
        power
    end

    def largest(dimx = 3, dimy = 3)
        largest_val = 0
        largest_coords = []
        @grid.each_index do |x|
            @grid[x].each_index do |y|
                next unless @grid[x + dimx - 1] && @grid[x + dimx - 1][y + dimy - 1]
                pval = 0
                dimx.times do |i|
                    dimy.times do |j|
                        pval += @grid[x + i][y + j]
                    end
                end
                if pval > largest_val
                    largest_val = pval
                    largest_coords = [x + 1, y + 1]
                end
            end
        end
        [ largest_coords, largest_val ]
    end


    def display
        trans = @grid.transpose
        trans.each do |line|
            output = line.map { |i| i.to_s.rjust(3) }.join('')
            puts output
        end
    end


end

def part1(serial)
    pg = PowerGrid.new(serial)
    pg.populatePowerValues
    # pg.display
    p pg.largest
end

def part2(serial)
    pg = PowerGrid.new(serial)
    pg.populatePowerValues

    largest_coord = []
    largest_power = 0
    largest_size = 1
    300.times do |s|
        puts "Size: #{s}"
        coords, power = pg.largest(s, s)
        p coords, power
        if power > largest_power
            largest_power = power
            largest_coord = coords
            largest_size = s
        end
    end
    p largest_coord
    p largest_power
    p largest_size
end


serial = 2568
# serial = 18
# serial = 42

part1(serial)
part2(serial)