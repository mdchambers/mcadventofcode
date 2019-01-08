#!/usr/bin/env ruby
class Network
    
    def initialize(file)
        @steps = Hash.new { |h, k| h[k] = [] }
        IO.foreach(file) do |line|
            words = line.scan(/\w+/)
            @steps[words[7]].push(words[1])
        end
        self.allsteps.each do |s|
            @steps[s] = [] if ! @steps.has_key?(s)
        end
        @performed = []
    end

    def display
        p @steps
    end

    def allsteps
        all = @steps.values.flatten | @steps.keys
        all.uniq.sort
    end

    # Returns all performable steps
    def performable
        perf = []
        @steps.each do |k, v|
            # Check if all prerequesites have been performed
            # p @performed
            perf << k if (v - @performed).empty?
        end
        # p perf.sort
        # p @performed
        # perf = perf - @performed
        # p perf.sort
        perf.sort
    end

    def run
        while @performed.length < @steps.length
            available = self.performable - @performed
            @performed.push (available[0])
            p @performed
        end
        @performed.join("")
    end

end

class Worker

    attr_reader :target

    def initialize(offset = 4)
        @target = ""
        @time = 0
        @offset = offset
    end

    def working?
        @target != ""
    end

    def start(target)
        @target = target
        # "A".ord = 65, so subtract 4 to get 61
        # "A".ord = 65, so subtract 64 to get 1
        @time = target.ord - @offset
    end

    # Update time left on step. If step complete, return step. Else, return nil
    def update
        @time += -1
        if @time == -1
            done = @target
            @target = ""
            return done
        end
        return nil
    end
end

class TimedNetwork
    
    attr_reader :steps, :workers

    def initialize(file, worker_num = 5, offset = 4)
        # Load network from file
        @steps = Hash.new { |h, k| h[k] = [] }
        IO.foreach(file) do |line|
            words = line.scan(/\w+/)
            @steps[words[7]].push(words[1])
        end
        # Ensure any steps with no preqs are entered in the @steps hash
        self.allsteps.each do |s|
            @steps[s] = [] if ! @steps.has_key?(s)
        end
        # Set the set of performed steps to empty
        @performed = []
        # Set of currently working steps
        @performing = []
        # Set up the workers for the network
        @workers = Array.new(worker_num) {Worker.new(offset)}
    end

    def display
        p @steps
    end

    def allsteps
        all = @steps.values.flatten | @steps.keys
        all.uniq.sort
    end

    # Returns all performable steps
    def performable
        perf = []
        @steps.each do |k, v|

            # Check if all prerequesites have been performed && not already performed && not currently performing by another worker
            perf << k if (v - @performed).empty? && ! @performed.include?(k) && ! @performing.include?(k)
        end
        # p perf.sort
        # p @performed
        # perf = perf - @performed
        # puts "Performed: #{@performed}"
        # puts "Performing: #{@performing}"
        # puts "Performable: #{perf.sort}"
        perf.sort
    end

    def updateWorkers
        # p @workers
        @workers.each do |w|
            # Update worker
            done = w.update
            if done
                # puts "Ending #{done}"
                @performed.push(done)
                @performing = @performing - [ done ]
            end
            # If worker idle and steps available, assign step and add to performing 
            if ! w.working? && self.performable.length > 0
                # puts "Starting #{self.performable[0]}"
                # p self.performable
                w.start(self.performable[0])
                w.update
                @performing.push self.performable[0]
                # puts "Performing #{@performing}"
            end
        end
    end

    def none_working?
        @workers.map(&:working?).none?
    end

    def run
        curr_time = 0
        while true
            self.updateWorkers
            # p @performed
            targets = self.workers.map &:target
            out_tab = [ curr_time ] + targets
            p out_tab
            curr_time += 1
            if self.none_working?
                return @performed.join("")
            end
        end
    end

end

def part1(file)
    net = Network.new(file)

    net.display
    # p net.allsteps
    p net.run
end

def part2(file)
    # net = TimedNetwork.new(file, 2, 64)
    net = TimedNetwork.new(file, 5, 4)
    p net.steps
    p net.run
end


input = "07_input.txt"
# input = "07_test.txt"

# part1(input)
part2(input)

# Not LRVAGPZHFOTCKWENBXIMSUD
# Not LRVAGPZHFOTCKWENBXIMSUDJQY 937
# It's 936