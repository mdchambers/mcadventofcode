#!/usr/bin/env ruby

class Pots

    attr_reader :state, :grow, :kill, :origin

    def initialize(initial, file)
        # @state = "." * offset + initial + "." * offset
        @state = initial
        @origin = 1
        # @rules = {}
        @grow, @kill = [], []
        IO.foreach(file) do |line|
            ld = line.strip.scan(/\S+/)
            # p ld
            # puts ld[2] == "#"
            @grow.push(ld[0]) if ld[2] == "#"
            @kill.push(ld[0]) if ld[2] == "."
            # p line
            # p ld
            # @rules[ld[0]] = ld[0][0..1] + ld[2] + ld[0][3..5]
        end
        # puts "grow"
        # p @grow
        # puts "kill"
        # p @kill
    end

    def expand
        if @state[0,5].include?("#")
            @state = "." * 5 + @state
            @origin += 5
        end
        if @state[-5,5].include?("#")
            @state = @state + "." * 5
        end
        # puts @state
    end

    def cycle
        self.expand
        to_grow, to_kill = [], []
        (2 .. (@state.length - 3)).each do |pos|
            @grow.each do |pattern|
                to_grow.push(pos) if @state[(pos -2)..(pos + 2)] == pattern
            end
            @kill.each do |pattern|
                to_kill.push(pos) if @state[(pos -2)..(pos + 2)] == pattern
            end
        end
        to_grow.each do |pos|
            @state[pos] = "#"
        end
        to_kill.each do |pos|
            @state[pos] = "."
        end
    end

    def plantSum
        pmatch = []
        @state.gsub("#") { pmatch.push($~) }
        ppos = pmatch.map { |m| m.offset(0)[1] - @origin}
        # p ppos
        ppos.sum
    end


    # def display
    #     puts @state.join('')
    # end

end

def part1(initial, file)
    pots = Pots.new(initial, file)
    # p pots.state
    # p pots.grow
    # p pots.kill
    21.times do |cycle|
        puts "#{cycle} #{pots.state} #{pots.plantSum}"
        # p pots.plantSum
        pots.cycle
    end
end

def part2(initial, file, cycles)
    pots = Pots.new(initial, file)
    # p pots.state
    # p pots.grow
    # p pots.kill
    curr_total = 0
    diff = 0
    (500).times do |cycle|
        pots.cycle
        diff = pots.plantSum - curr_total
        puts "Cycle: #{cycle} Sum: #{pots.plantSum} Diff: #{diff}"
        curr_total = pots.plantSum
    end   

    # curr_total contains the total at cycle 500, diff contains the diff per cycle (it stabilizes well before 500 cycles)

    final = curr_total + (50e9 - 500) * diff
    puts final
    

end

# test_initial = "#..#.#..##......###...###"
# test_file = "12_test.txt"
# part1(test_initial, test_file)

initial = "#.#.#..##.#....#.#.##..##.##..#..#...##....###..#......###.#..#.....#.###.#...#####.####...#####.#.#"
file = "12_input.txt"
part1(initial, file)
# 1798 => too low
# 1917

part2(initial, file, cycles = 10000)
# 1250000000991