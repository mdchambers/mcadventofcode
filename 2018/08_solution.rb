#!/usr/bin/env ruby

class Node
    attr_reader :num_children, :num_meta
    attr_writer :children, :metadata

    def initialize(num_children, num_meta)
        @num_children = num_children
        @num_meta = num_meta

        @children = []
        @metadata = []
    end

    def addChild(c)
        @children.push(c)
    end

    def addMetadata(m)
        @metadata.push(m)
    end

    def metadataSum
        @metadata.sum + @children.map(&:metadataSum).sum
    end

    def valueSum
        vsum = 0
        @metadata.each do |m|
            # puts m
            if @children.length == 0
                vsum += m
            elsif m > 0 && @children[m - 1]
                vsum += @children[m - 1].valueSum
            end
        end
        return vsum
    end

end

class TreeReader
    def initialize(file)
        dat = IO.read(file)
        @stream = dat.split(" ").map(&:to_i)
        # p dat
    end

    # Returns a Tree based on the input stream data
    def generate
        # Generate the current node
        currNode = Node.new(@stream.shift, @stream.shift)
        children_remaining = currNode.num_children

        # Generate child nodes recursively
        while children_remaining > 0
            currNode.addChild(self.generate)
            children_remaining += -1
        end
        meta_remaining = currNode.num_meta

        # Add metadata
        while meta_remaining > 0
            currNode.addMetadata(@stream.shift)
            meta_remaining += -1
        end
        return currNode
    end
end

def part1(file)
    nr = TreeReader.new(file)
    tree = nr.generate
    
    puts tree.metadataSum
end

def part2(file)
    nr = TreeReader.new(file)
    tree = nr.generate
    # p tree
    puts tree.valueSum
end 

input = "08_input.txt"
# input = "08_test.txt"

part1(input) #36627
part2(input) #16695