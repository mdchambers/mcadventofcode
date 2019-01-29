#!/usr/bin/env ruby
require 'pp'
require 'matrix'

$logging = true

class Game
    
    ADJ = [ Vector[-1,0], Vector[1,0], Vector[0,-1], Vector[0,1]]

    def initialize(file, elf_attack = 3)
        @grid = []
        @characters = []
        @elf_attack = elf_attack
        @status = :initialized
        IO.foreach(file) do |line|
            line.chomp!
            @grid << []
            line.chars.each do |c|
                @grid.last << c
            end
        end
        # Replace E/G with "." and generate characters
        @grid.each_index do |x|
            @grid[x].each_index do |y|
                if @grid[x][y] == "E"
                    @characters << Character.new(x, y, @grid[x][y], elf_attack)
                    @grid[x][y] = "."
                elsif @grid[x][y] == "G"
                    @characters << Character.new(x,y, @grid[x][y])
                    @grid[x][y] = "."
                end
            end
        end
    end

    # Runs simulation to its conclusion
    def simulate
        @status = :simulating
        @round_num = 0
        while true
            @round_num += 1
            # puts "Round: #{@round_num}"
            self.round()
            return if gameOver?
        end
    end

    # Runs simulation until first death
    def simulateUntilDeath
        @round_num = 0
        starting_elves = @characters.filter { |c| c.type == "E"}.length
        until gameOver?
            @round_num += 1
            puts "round: #{@round_num}"
            self.round
            # End game if an elf dies
            # puts @characters.filter { |c| c.type == "E"}
            if @characters.filter { |c| c.type == "E"}.length != starting_elves
                puts "Elf death @ round #{@round_num} hp #{@elf_attack}"
                return [@round_num, totalHP, false]
            end
        end
        return [@round_num, totalHP, true ]
    end

    # Completes one round
    def round
        # Sort characters by action order
        @characters = Game.sortCharactersbyPos(@characters)
        @characters.each do |c|
            # Skip if died this round
            next if c.dead?
            # puts "Character: #{c.to_s}" if $logging
            
            # Move if no adjacent enemy
            unless (ac = c.adjacentEnemies(@characters - [c]))
                # Generate list of all attack positions
                possible_targets = enemies(c)
                pp = adjacentSpaces(possible_targets)
                # Calculate distance to each position
                mypaths = pp.map { |s| Path.new(c.pos, s, maskedGrid)}
                # Filer for valid paths only
                mypaths.reject! { |i| i.shortest.nil?}

                # Choose shortest length paths
                min_distance = mypaths.map(&:length).min
                min_paths = mypaths.select { |i| i.length == min_distance }

                # If multiple equal length paths, choose read-order path
                # i.e. path to first read-order destination
                if min_paths.length > 1
                    # Sort min length paths by ending position
                    # puts "\n*******\nTIE\n#{c}"
                    # min_paths.each { |mp| puts "#{mp.shortest}" }
                    sorted_paths = min_paths.sort do |a,b|
                        aend = a.shortest.last
                        bend = b.shortest.last
                        aend[0] == bend[0] ? aend[1] <=> bend[1] : aend[0] <=> bend[0]
                    end
                    
                    selected_path = sorted_paths.first
                    # puts "Selected path: #{selected_path.shortest}"
                    # displayBoard
                    # puts "********\n"
                    # input = gets.chomp
                    # exit if input == "q"
                else
                    selected_path = min_paths.first
                end

                # If no path available, go to next character
                if selected_path.nil?
                    # puts "Move: none available" if $logging
                    next 
                end
                # puts "Select: #{selected_path.shortest}"
                
                # Take step
                # puts "Move: #{selected_path.shortest[1]}" if $logging
                c.pos = selected_path.shortest[1]
            end

            # Attack if adjacent enemy
            if ( ac = c.adjacentEnemies( @characters - [ c ] ) )
                # puts "Attack: #{ac[0].to_s}" if $logging
                c.attack(ac[0])
                if ac[0].dead?
                    remaining = @characters.filter(&:alive?)
                    # puts "removing #{ac[0]}"
                    if remaining.map { |c| c.type == "G" }.all? || remaining.map { |c| c.type == "E" }.all?
                        puts "GAME OVER"
                        hp_sum = remaining.reduce(0) {|s, c| s += c.hp} 
                        if c == remaining.last
                            @round_num += 1 
                            puts "death at end of round"
                        end
                        puts "#{@round_num - 1} #{hp_sum} #{(@round_num -1) * hp_sum}"
                        @status = :ended
                        # displayBoard
                        # return
                    end
                end
            end
            # puts "" if $logging
        end
        
        # Remove dead characters from active list
        @characters.filter! &:alive?
    end

    # Return list of adjacent spaces to each character in carr
    def adjacentSpaces(carr)
        spaces = []
        carr.each do |c|
            ADJ.each do |a|
                # puts "evaluating space: #{c.pos + a}"
                if isClear?(c.pos + a)
                    # puts "adding space"
                    spaces << (c.pos + a) 
                end
            end
        end
        # puts spaces
        spaces
    end

    # Return array of enemy characters to c
    # i.e. different type, not self, and not dead
    def enemies(c)
        @characters.reject { |d| d.type == c.type || d == c || d.dead? }
    end

    def totalHP
        @characters.reduce(0) { |s, c| s += c.hp}
    end

    def isClear?(pos)
        # puts pos
        # puts "pos: #{@grid[pos[9]]}"
        # puts @grid[pos[0]][pos[1]]
        char_pos = @characters.filter(&:alive?).map(&:pos)
        @grid[pos[0]][pos[1]] == "." && ! char_pos.include?(pos)
    end

    def gameOver?; @status == :ended end

    def self.sortCharactersbyPos(carr)
        carr.sort { |a,b| (a.pos[0] == b.pos[0]) ? a.pos[1] <=> b.pos[1] : a.pos[0] <=> b.pos[0]}
    end

    # Sort array of characters by hp and position in reading order
    def self.sortCharactersByHPandPos(carr)
        carr.sort{ | a, b |
            if a.hp != b.hp
                a.hp <=> b.hp
            else
                (a.x == b.x) ? (a.y <=> b.y) : (a.x <=> b.x)
            end
        }
    end

    # Outputs the board layout
    def displayBoard(characters = true)
        # output = "  " + (0...(@grid[0].length)).to_a.join('') + "\n"
        output = "\n"
        @grid.each_with_index do |val, idx|
            # line = idx.to_s + " " + val.join('')
            line = val.join('')
            if characters
                carr_toprint = Game.sortCharactersbyPos(@characters)
                carr_toprint.each do |c| 
                    if c.pos[0] == idx
                        line[c.pos[1]] = c.type 
                        line += " (#{c.type}:#{c.hp})"
                    end
                end
            end
            output << line + "\n"
        end
        puts output
    end

    def maskedGrid
        masked = @grid.map &:dup
        @characters.filter(&:alive?).each do |c|
            masked[c.x][c.y] = "#"
        end
        masked
    end
end

class Character

    attr_accessor :pos, :type, :hp

    ADJ = [ Vector[-1,0], Vector[1,0], Vector[0,-1], Vector[0,1]]

    def initialize(x, y, type, power = 3)
        @pos = Vector[x, y]
        @type = type
        @power = power
        @hp = 200
    end

    def x; @pos[0] end
    def y; @pos[1] end

    def attack(toAttack)
        toAttack.hp -= @power
    end

    def dead?; @hp <= 0 end

    def alive?; @hp > 0 end

    def isEnemy?(char) @type != char.type; end

    # Returns array of adjacent enemies (sorted by attack-first to attack-last) or nil if no adjacent enemies
    def adjacentEnemies(carr)
        # puts "Character: #{self.to_s}"
        enemies = []
        carr.each do |c|
            # If adjacent, enemy, and alive, add to list
            if self.adjacent?(c.pos) && self.isEnemy?(c) && c.alive?
                # puts "Adjacent: #{c.to_s}"
                enemies << c
            end
        end
        # Sort enemies by health, then read order (health => x => y)
        enemies = Game.sortCharactersByHPandPos(enemies)
        if enemies.length >= 1
            return enemies
        else
            return nil
        end
    end

    def adjacent?(qpos)
        ADJ.each do |a|
            if self.pos + a == qpos
                return true
            end
        end
        return false
    end

    def to_s
        "X: #{@pos[0]} Y: #{@pos[1]} HP: #{@hp} Type #{@type}"
    end
end

class Path

    ADJ = [ Vector[-1,0], Vector[1,0], Vector[0,-1], Vector[0,1]]

    attr_accessor :shortest, :spos, :epos

    def initialize(spos, epos, state)
        @spos = spos
        @epos = epos
        @state = state
        @valid = true
        @shortest = self.calculateShortest
    end

    def steps; end

    def calculateShortest(counter = 0)
        # Calculate path grid
        queue = {}
        queue[@epos] = 0

        curr_pos = -1
        while true
            break if queue.has_key?(@spos)
            curr_pos += 1
            # puts "curr pos: #{curr_pos}"
            queue_pos = queue.keys[curr_pos]
            # puts "queue pos: #{queue_pos}"
            queue_counter = queue[queue_pos]
            # puts "queue counter: #{queue[queue_pos]}"
            # Generate hash with adjacent squares and incremented counter
            to_add = {}
            ADJ.each do |a|
                to_add[queue_pos + a] = queue_counter + 1
            end
            # puts to_add
            # Remove from list if space is blocked
            to_add.delete_if { |add_pos, add_counter| !isMoveable?(add_pos) && add_pos != @spos }
            # Remove from list if already present in queue with lower counter
            to_add.delete_if do |add_pos, add_counter|
                queue.has_key?(add_pos) && queue[add_pos] <= add_counter
            end
            # puts to_add

            # If this position is last in the queue and did not result in any additional steps,
            # then no path is possible. Return nil
            if to_add.length == 0 && queue_pos == queue.keys.last
                # puts "No path available"
                # displayCounters(queue)
                return nil
            end
            queue.merge!(to_add)
            # puts "Queue: #{queue}"
        end

        # displayCounters(queue)
        
        # puts "Final: #{queue}"
        # puts queue
        # Generate path(s) from path grid
        steps = [ @spos ]
        until steps.last == @epos
            # Get adjacent positions
            adj_pos = ADJ.map {|a| a + steps.last }
            # Select adjacent position queue entries
            adj_queue = queue.slice *adj_pos
            min_val = adj_queue.values.min
            next_steps = adj_queue.keep_if {|k,v| v == min_val}.keys
            # Choose reading-order step if multiple steps have equal value
            if next_steps.length > 1
                # pp next_steps
                next_steps.sort! { |a, b| (a[0] == b[0]) ? a[1] <=> b[1] : a[0] <=> b[0] }
            end
            next_steps = next_steps.first
            steps << next_steps
            # puts steps
        end
        # pp "Path: #{steps}"
        steps
    end

    def displayCounters(queue)
        ng = @state.map &:dup
        queue.each do |k, v|
            ng[k[0]][k[1]] = v.to_s
        end
        output = "  " + (0...(ng[0].length)).to_a.join('') + "\n"
        ng.each_with_index do |val, idx|
            line = idx.to_s + " " + val.join('')
            output << line + "\n"
        end
        puts output
    end

    def isMoveable?(pos)
        # puts @state[pos[0]][pos[1]]
        @state[pos[0]][pos[1]] == "."
    end

    def length; @shortest.length end

end

def part1(input)
    g = Game.new(input)
    puts "Round: 0"
    g.displayBoard
    # puts "Board only:"
    # g.displayBoard(false)
    # puts "Simulate:"
    # g.maskedGrid
    g.simulate
end

def part2(input)
    elf_attack = 3
    while true
        puts "ATK: #{elf_attack}"
        elf_attack += 1
        g = Game.new(input, elf_attack)
        outcome = g.simulateUntilDeath
        puts "ATK: #{elf_attack} ROUND: #{outcome[0]} HP: #{outcome[1]}"
        break if outcome[2]
    end
end

# part1(ARGV.first)

part2(ARGV.first)

# Part 1: Answer Submissions
# 185594 => too low (71 2614)
# 188208 => too low (72 2614)
# Fixed error with selection of correct path (was not choosing read-order first end position when paths were of equal length)
# 184884 => too low (71 2604)
# Fixed bug where dead enemies were still being included when masking grid for pathfinding
# Didn't change anything
# Issue is choosing the correct path. Apparent discrepancy during very first turn 