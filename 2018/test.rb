
class Foo

    attr_reader :y, :x


    def initialize
        @x = 2 
    end

    def run
        @@methods.each do |m|
            puts method(m).call
        end
    end

    def one; @x + 1; end
    def two; @x + 2; end
    def three; @x + 3; end

    @@methods = [:one, :two, :three]

end

y = Foo.new
y.run
