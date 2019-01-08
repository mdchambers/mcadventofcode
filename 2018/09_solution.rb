#!/usr/bin/env ruby

class MarbleGame
    def initialize(players, last_marble)
        @players = players
        @scores = [0] * @players
        @last_marble = last_marble
        @turn = -1
    end

    def currentPlayer
        @turn % @players
    end

    def play
        @current_marble = 0
        @pos = 0
        @board = [ 0 ]
        while @current_marble < @last_marble
            @current_marble += 1
            self.turn
            self.print
        end
        @scores
    end

    def turn
        @turn += 1
        puts "Turn: #{@turn}" if @turn % 1000 == 0
        if @current_marble % 23 != 0
            @board.rotate!(2)
            @board.unshift(@current_marble)
        else
            # puts "Adding #{@current_marble} and #{@board[-7]} to score for player #{self.currentPlayer}"
            @scores[self.currentPlayer] += @current_marble + @board[-7]
            @board.rotate!(-7)
            @board.shift
        end
    end

    def print
        # p @scores
        # p @board
    end
        
end

def part1(players, last_marble)
    mg = MarbleGame.new(players, last_marble)
    scores = mg.play
    puts scores.max
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
part1(players, last_marble * 100)