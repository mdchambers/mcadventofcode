#!/usr/bin/env ruby

# Operation class with operator logic and for assigning possible categories
class Operation

    attr_reader :opcode

    @@ops = [:addr, :addi, :mulr, :muli, :banr, :bani, :borr, :bori, :setr, :seti, :gtir, :gtri, :gtrr, :eqir, :eqri, :eqrr]

    def initialize(before, inst, after)
        @before = before.dup
        @inst = inst.dup
        @after = after.dup
        @opcode = @inst.first
        @res = Hash[ @@ops.product([false]) ]
    end

    def self.readFromFile(file)
        ops = []
        tmp = []
        IO.foreach(file) do |line|
            next if line.length <= 1
            line.chomp!
            if line =~ /Before/ && ! tmp.empty?
                ops << Operation.new(*tmp)
                tmp.clear 
            end
            tmp << line.scan(/\d+/).map(&:to_i)
        end
        ops << Operation.new(*tmp)
        ops
    end

    def diagnose
        @res.each do |k, v|
            result = method(k).call(*@inst[1,3])
            if @after == result
                @res[k] = true
            end
        end
    end

    def possibles
        pos = @res.filter { |k,v| v}
        pos.keys
    end

    def addr(a, b, c)
        result = @before.dup
        result[c] = result[a] + result[b]
        result
    end

    def addi(a, b, c)
        result = @before.dup
        result[c] = result[a] + b
        result
    end

    def mulr(a, b, c)
        result = @before.dup
        result[c] = result[a] * result[b]
        result
    end

    def muli(a, b, c)
        result = @before.dup
        result[c] = result[a] * b
        result
    end

    def banr(a,b,c)
        result = @before.dup
        result[c] = result[a] & result[b]
        result
    end

    def bani(a,b,c)
        result = @before.dup
        result[c] = result[a] & b
        result
    end

    def borr(a,b,c)
        result = @before.dup
        result[c] = result[a] | result[b]
        result
    end

    def bori(a,b,c)
        result = @before.dup
        result[c] = result[a] | b
        result
    end

    def setr(a, b, c)
        result = @before.dup
        result[c] = result[a]
        result
    end
    
    def seti(a, b, c)
        result = @before.dup
        result[c] = a
        result
    end

    def gtir(a,b,c)
        result = @before.dup
        a > result[b] ? result[c] = 1 : result[c] = 0
        result
    end

    def gtri(a,b,c)
        result = @before.dup
        result[a] > b ? result[c] = 1 : result[c] = 0
        result
    end

    def gtrr(a,b,c)
        result = @before.dup
        result[a] > result[b] ? result[c] = 1 : result[c] = 0
        result
    end

    def eqir(a,b,c)
        result = @before.dup
        a == result[b] ? result[c] = 1 : result[c] = 0
        result
    end

    def eqri(a,b,c)
        result = @before.dup
        result[a] == b ? result[c] = 1 : result[c] = 0
        result
    end

    def eqrr(a,b,c)
        result = @before.dup
        result[a] == result[b] ? result[c] = 1 : result[c] = 0
        result
    end   

    
    def to_s
        "B: #{@before} S: #{@inst} A: #{@after}"
    end
end

class Program
    def initialize(file, op_mapping)
        @registers = [0,0,0,0]
        @instructions = []
        @mapping = op_mapping
        IO.foreach(file) do |line|
            @instructions << line.scan(/\d+/).map(&:to_i)
        end
    end

    def run
        @instructions.each do |i|
            op = method(@mapping[i[0]])
            op.call(*i[1,3])
            pp @registers
        end
    end

    def addr(a,b,c)
        @registers[c] = @registers[a] + @registers[b]
    end

    def addi(a,b,c)
        @registers[c] = @registers[a] + b
    end

    def mulr(a,b,c)
        @registers[c] = @registers[a] * @registers[b]
    end

    def muli(a,b,c)
        @registers[c] = @registers[a] * b
    end

    def banr(a,b,c)
        @registers[c] = @registers[a] & @registers[b]
    end

    def bani(a,b,c)
        @registers[c] = @registers[a] & b
    end

    def borr(a,b,c)
        @registers[c] = @registers[a] | @registers[b]
    end

    def bori(a,b,c)
        @registers[c] = @registers[a] | b
    end

    def setr(a,b,c)
        @registers[c] = @registers[a]
    end
    
    def seti(a,b,c)
        @registers[c] = a
    end

    def gtir(a,b,c)
        a > @registers[b] ? @registers[c] = 1 : @registers[c] = 0
    end

    def gtri(a,b,c)
        @registers[a] > b ? @registers[c] = 1 : @registers[c] = 0
    end

    def gtrr(a,b,c)
        @registers[a] > @registers[b] ? @registers[c] = 1 : @registers[c] = 0
    end

    def eqir(a,b,c)
        a == @registers[b] ? @registers[c] = 1 : @registers[c] = 0
    end

    def eqri(a,b,c)
        @registers[a] == b ? @registers[c] = 1 : @registers[c] = 0
    end

    def eqrr(a,b,c)
        @registers[a] == @registers[b] ? @registers[c] = 1 : @registers[c] = 0
    end
end

def part1(input)
    ops = Operation.readFromFile(input)

    ops.each do |o|
        o.diagnose

    end
    # Find how many behave like three or more opcodes
    three = 0
    ops.each do |o|
        three += 1 if o.possibles.length >= 3
    end
    puts "Part 1: #{three}"
end


def genrateMapping(input)
    ops = Operation.readFromFile(input)

    ops.each do |o|
        o.diagnose
    end

    opcodes = {}
    (0..15).each { |i| opcodes[i] = []}
    ops.each do |o|
        opcodes[o.opcode] << o.possibles
    end
    minset = Hash.new
    opcodes.each do |k, v|
        mset = v.reduce :&
        minset[k] = mset
    end

    final = minset.filter { |k,v| v.length == 1}
    while true
        # Remove finalized ops from list
        final.each do |k,v|
            minset.each do |xk, xv|
                minset[xk] = xv - v
            end
        end
        final.merge!( minset.filter {|k,v| v.length == 1} )
        break if final.length == 16
    end
    # Values are single-element arrays; un-array
    final.transform_values! { |v| v.first}
    final
end

def part2(input1, input2)
    opmap = genrateMapping(input1)

    prog = Program.new(input2, opmap)
    prog.run
end

part1(ARGV.first)
# 508 => too high
# 500 => correct

part2(ARGV[0], ARGV[1])
# 533