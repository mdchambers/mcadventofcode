package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	fmt.Printf("Hello go\n")

	x := "10"

	if y, err := strconv.Atoi(x); err == nil {
		fmt.Printf("%s %d\n", x, y)
	}

	input, err := ioutil.ReadFile("static/day01.txt")
	if err != nil {
		panic("Could not open file")
	}
	lines := strings.Split(string(input), "\n")

	for _, val := range lines {
		fmt.Printf("Val: %s\n", val)
	}

}
