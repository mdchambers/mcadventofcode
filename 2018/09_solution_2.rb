#!/usr/bin/env ruby

class MarbleGame
    def initialize(players, last_marble)
        @players = players
        @scores = [0] * @players
        @last_marble = last_marble
        @turn = 0
    end

    def currentPlayer
        @turn % @players
    end

    def play
        @current_marble = Marble.new(0)
        while @current_marble.val < @last_marble
            # puts @current_marble.val
            self.turn
            # self.display
        end
        @scores
    end

    def turn
        @turn += 1
        # puts "Turn: #{@turn}" if @turn % 1000 == 0
        if @turn % 23 == 0 && @turn != 0
            # p @current_marble
            # puts "Adding #{@current_marble} to score for player #{self.currentPlayer}"
            @scores[self.currentPlayer] += @turn
            7.times { @current_marble = @current_marble.prev_marble}
            # puts "Adding #{@current_marble.val} to score"
            @scores[self.currentPlayer] += @current_marble.val
            @current_marble.delete
            @current_marble = @current_marble.next_marble
        else
            @current_marble = @current_marble.next_marble
            # puts "adding marble #{@turn}"
            @current_marble.insert_after(@turn)
            @current_marble = @current_marble.next_marble
            # puts @current_marble.val
        end
    end

    def display
        # p @scores
        # p @board
        init = @current_marble
        print "#{init.val} "
        curr = init
        loop do
            curr = curr.next_marble
            break if curr == init
            print "#{curr.val} "
        end
        print "\n"
    end
        
end

class Marble
    
    attr_accessor :val, :prev_marble, :next_marble

    def initialize(val, prev_marble = self, next_marble = self)
        @val = val
        @prev_marble = prev_marble
        @next_marble = next_marble
    end

    def insert_after(val)
        new_marble = Marble.new(val, self, @next_marble)
        # p new_marble.val
        @next_marble.prev_marble = new_marble
        @next_marble = new_marble
    end
        
    def delete
        @prev_marble.next_marble = @next_marble
        @next_marble.prev_marble = @prev_marble
    end
end





def part1(players, last_marble)
    mg = MarbleGame.new(players, last_marble)
    scores = mg.play
    p scores.max
end

# Real data
players, last_marble = 476, 71657

# 32
# players, last_marble = 9, 25 

# 8317
# players, last_marble = 10, 1618 

puts "Part 1"
part1(players, last_marble) # 386018
puts "Part 2"
# Apparently array inserts/rotates are very slow in Ruby; should use linked lists
part1(players, last_marble * 100) # 3085518618