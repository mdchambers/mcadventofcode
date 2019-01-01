#!/usr/bin/env ruby

class Fabric
    DIM = 1000
    def initialize
        @grid = Array.new(DIM) { Array.new(DIM,0)}
        # self.display
    end

    # Adds a claim
    def addClaim(claim)
        # claim.display
        # ((claim.y)...(claim.y + claim.height)).each { |i| puts i}
        # puts "From #{claim.x} to #{claim.x + claim.width - 1}"
        # ((claim.y)...(claim.y + claim.height)).each{ |row|
        #     puts "Row: #{row}"
        #     puts "Cols: #{claim.x} #{claim.width}"
        #     @grid[row][claim.x, claim.width] = @grid[row][claim.x, claim.width].map { |i| i += 1}
        # }
        ((claim.y)...(claim.y + claim.height)).each{ |x|
            ((claim.x)...(claim.x + claim.width)).each{ |y|
                # puts "#{x} #{y}"
                @grid[x][y] += 1
            }
        }
    end

    def overlapsAny?(claim)
        ((claim.y)...(claim.y + claim.height)).each{ |x|
            ((claim.x)...(claim.x + claim.width)).each{ |y|
                if @grid[x][y] > 1
                    return true
                end
            }
        }       
        return false
    end

    def countOverlaps
        positions = @grid.flatten.select { |i| i > 1}
        positions.length
    end

    def display
        @grid.each{ |c|
            puts c.join(" ")
        }
    end
end

class Claim
    # def initialize(id, left, top, width, height)
    #     @id = id
    #     @x = left
    #     @y = top
    #     @width = width
    #     @height = height
    # end
    def initialize(line)
        # puts line
        nums = line.scan /\d+/
        nums = nums.map{ |i| i.to_i }
        # puts nums.join(", ")
        @id, @x, @y, @width, @height = nums
        @overlaps = false
    end

    def overlapsAny?(carr)
        f = Fabric.new
        carr.each { |c| f.addClaim(c)}
        orig_overlaps = f.overlaps
        f.addClaim(self)
        new_overlaps = f.overlaps
        if orig_overlaps == new_overlaps
            return false
        else
            return true
        end
    end

    def area
        @width * @height
    end

    def display
        puts "Claim #{@id}: #{@x} #{@y} #{@width} #{@height}"
    end

    def x
        @x
    end

    def y
        @y
    end

    def width
        @width
    end

    def height
        @height
    end

    def id
        @id
    end

    def overlaps=(val)
        puts "overlaps called"
        @overlaps = val
    end

    def overlaps
        @overlaps
    end
end

def part1(file)
    claims = Array.new
    IO.foreach(file){ |line|
        claims.push(Claim.new(line))
    }

    # claims.each{ |i| i.display}
    # puts claims.length
    fab = Fabric.new
    claims.each{ |c|
        fab.addClaim(c)
    }
    # fab.display
    print "Overlaps: "
    puts fab.countOverlaps

end

def part2(file)
    claims = Array.new
    IO.foreach(file){ |line|
        claims.push(Claim.new(line))
    }

    # claims.each{ |i| i.display}
    # puts claims.length
    fab = Fabric.new
    claims.each{ |c|
        fab.addClaim(c)
    }

    claims.each{ |i|
        if !fab.overlapsAny?(i)
            puts "Claim #{i.id} didn't overlap"
        end
    }

 
end

input = "03_input.txt"
# input = "03_test.txt"
part1(input)
part2(input)