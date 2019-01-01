#!/usr/bin/env ruby

def part1(file)
    twos = 0
    threes = 0
    # Read each id
    IO.foreach(file) { |line|
        line = line.strip
        char_counts = line.chars.reduce(Hash.new(0)) { | h, v | h[v] += 1; h}
         twos += 1 if char_counts.values.include? 2
         threes += 1 if char_counts.values.include? 3 
    }
    puts "Twos: #{twos}\nThrees: #{threes}\nChecksum: #{ twos * threes }"
end

def differByOne?(s1, s2)
    pairs = s1.chars.zip(s2.chars)
    diffs = 0
    pairs.each{ |p|
        diffs += 1 if p[0] != p[1]
    }
    if diffs == 1
        return true
    else
        return false
    end
end

def getCommonLetters(l1, l2)
    pairs = l1.chars.zip(l2.chars)
    common = Array.new
    pairs.each { |p|
        if p[0] == p[1]
            common.push(p[0])
        end
    }
    return common.join
end

def part2(file)
    lines = IO.readlines(file)
    lines.each { |l|
        lines.each { |j|
            if differByOne?(l, j)
                puts l.strip + " " + j.strip
                common = getCommonLetters(l, j)
                puts "Common: " + common
            end
        }
    }
end

# input = "02_test.txt"
input = "02_input.txt"
part1(input)
part2(input)