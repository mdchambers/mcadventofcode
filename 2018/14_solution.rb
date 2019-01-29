#!/usr/bin/env ruby

def part1(rnum)
    recipes = "3710"
    pos1 = 0
    pos2 = 1

    # output = ""
    while true
        # input = gets.strip
        # exit if input == "q"
        # calculate new recipe and append to recipes
        new_recipe = recipes[pos1].to_i + recipes[pos2].to_i
        recipes += new_recipe.to_s

        # Move each elf
        pos1_move = 1 + recipes[pos1].to_i
        pos2_move = 1 + recipes[pos2].to_i
        pos1 = (pos1 + pos1_move) % recipes.length
        pos2 = (pos2 + pos2_move) % recipes.length

        # puts "#{pos1} #{pos2} #{recipes}"

        # puts recipes.length
        if recipes.length >= rnum + 10
            return recipes[rnum, 10]
        end
    end
end

def part2(seq)
    seq = seq.to_s
    recipes = "3710"
    pos1 = 0
    pos2 = 1

    # output = ""
    while true
        # input = gets.strip
        # exit if input == "q"
        # calculate new recipe and append to recipes
        puts "Beginning round #{recipes.length}"
        10000.times do
            new_recipe = recipes[pos1].to_i + recipes[pos2].to_i
            recipes << new_recipe.to_s
            # Move each elf
            pos1 = (pos1 + recipes[pos1].to_i + 1) % recipes.length
            pos2 = (pos2 + recipes[pos2].to_i + 1) % recipes.length
            # puts recipes
            # input = gets
        end

        if recipes =~ /#{seq}/
            puts $~.begin(0)
            exit
        end
        # puts recipes.length if recipes.length % 10000 == 0
    end
end

# [5, 9, 18, 2018, 293801].each do |i|
#     puts i
#     puts part1(i)
# end

# 3147574107
# [51589, "01245", 92510, 59414].each do |i|
#     puts i
#     puts part2(i)
# end

# part2(ARGV[0])
part2("293801")
# Ans: 20280190 in 1m 1s