#!/usr/bin/env ruby


def part_1(file)
    freq = 0
    IO.foreach(file) { |line|
        freq += line.to_i
    }
    puts "Part 1: #{freq}"
end

def part_2(file)
    freqs = [0]
    while true do
        IO.foreach(file) { |line|
            new_freq = freqs.last + line.to_i
            if freqs.include? new_freq
                puts "Part 2: #{new_freq}"
                return
            else
                freqs.push(new_freq)
                # puts new_freq
            end
        }
    end
end

input_file = "01_input.txt"
# input_file = "01_test.txt"
part_1(input_file)
part_2(input_file)