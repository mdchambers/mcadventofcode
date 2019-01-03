#!/usr/bin/env ruby

class Shift
    def initialize(guard)
        @guard = guard
        @year = nil
        @month = nil
        @day = nil
        @sleep = []
        @wake = []
    end
    
    def guard
        @guard
    end

    def guard=(guard)
        @guard = guard
    end

    def year
        @year
    end

    def month
        @month
    end

    def day
        @day
    end

    def addSleep(time)
        @sleep.push(time)
    end

    def addWake(time)
        @wake.push(time - 1)
    end

    def intervals
        return @sleep.zip(@wake)
    end

    def print
        p self
    end
end

# Returns an array of Shift obj from file
def processFile(file)
    lines = IO.readlines(file)
    lines.sort!

    shifts = Array.new
    newshift = false
    lines.each{ |line|
        nums = line.scan(/\d+/)
        nums.map! {|n| n.to_i}
        year, month, day, hour, minute, guard = nums
        if guard  
            shifts.push(Shift.new(guard))
        else
            if line =~ /wakes up/
                shifts.last.addWake(minute)
            elsif line =~ /asleep/
                shifts.last.addSleep(minute)
            end
        end      
    }
    return shifts
end

def guardTable(shifts)
    guards = Hash.new
    shifts.each{ |i|
        if ! guards.has_key?(i.guard)
            guards[i.guard] = Array.new(60, 0)
        end
        i.intervals.each{ |interval|
            guards[i.guard][(interval[0]..interval[1])] = guards[i.guard][(interval[0]..interval[1])].map { |v| v += 1 }
        }
    }
    return guards
end

def sleepiestGuard(gtable)
    sleep_max_key = gtable.keys.first
    gtable.each do |k, v|
        if v.sum > gtable[sleep_max_key].sum
            sleep_max_key = k
        end
    end
    return sleep_max_key
end

def sleepiestMinute(sarr)
    p sarr
    sleep_max_min = 0
    sarr.each_index do |index|
        # puts "compare #{sarr[index]} with #{sarr[sleep_max_min]}"
        if sarr[index] > sarr[sleep_max_min]
            sleep_max_min = index
        end
    end
    return sleep_max_min
end

def part1(file)
    shifts = processFile(file)
    # p shifts
    gtable = guardTable(shifts)
    # p gtable
    sleep_guard = sleepiestGuard(gtable)
    sleep_min = sleepiestMinute(gtable[sleep_guard])
    puts "Guard:#{sleep_guard} Min: #{sleep_min} Product: #{sleep_guard * sleep_min} "
end

def part2(file)
    shifts = processFile(file)
    gtable = guardTable(shifts)
    # p gtable
    sleep_max_val = 0
    sleep_max_min = 0
    sleep_max_id = 0
    gtable.each do |k, v|
        v.each_index do |i|
            if v[i] > sleep_max_val
                sleep_max_id = k
                sleep_max_min = i
                sleep_max_val = v[i]
            end
        end
    end
    puts "Guard: #{sleep_max_id} slept #{sleep_max_val} at min #{sleep_max_min}"
    puts "Part 2: #{sleep_max_id * sleep_max_min}"


end

input = "04_input.txt"
# input = "04_test.txt"
part1(input)
part2(input)


