#!/usr/bin/env ruby

def cycle(p)
    newpoly = ""
    i = 0
    while i < p.length
        # Check if chars at i and i+1 annihilate each other
        if p[i + 1] && p[i].downcase == p[i + 1].downcase && p[i] != p[i + 1]
            # If so skip next char
            # puts "annihilating #{p[i]} and #{p[i + 1]}"
            i += 1
        else
            newpoly += p[i]
        end
        i += 1
    end
    newpoly
end

def react(p)
    loop_count = 0
    poly_change = 1
    while poly_change != 0
        loop_count += 1
        puts "Loop: #{loop_count}" if loop_count % 10 == 0
        orig_len = p.length
        p = cycle(p)
        # p polymer
        poly_change = orig_len - p.length
    end
    return p
end

def part1(file)
    polymer = IO.readlines(file)[0].strip

    rxn_poly = react(polymer)
    puts "part 1: #{rxn_poly.length}"
end

def part2(file)
    polymer = IO.readlines(file)[0].strip

    red_sizes = Array.new
    pairs = ("a".."z").zip("A".."Z")
    pairs.each do |pair|
        puts "Starting: #{pair}"
        red_poly = polymer
        red_poly = red_poly.gsub(pair[0], "")
        red_poly = red_poly.gsub(pair[1], "")
        # p red_poly
        red_sizes.push(react(red_poly).length)
    end
    p red_sizes
    puts "Min: #{red_sizes.min}"
end

# input = "05_test.txt"
input = "05_input.txt"

part1(input)
part2(input)