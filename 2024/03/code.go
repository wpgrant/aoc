package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func processFileA(theString string) {
	re := regexp.MustCompile(`mul\(\d+,\d+\)`)
	theMults := re.FindAll([]byte(theString), -1)
	tot := 0
	for _, mult := range theMults {
		theMult := string(mult)
		re2 := regexp.MustCompile(`(\d+),(\d+)`)
		match := re2.FindStringSubmatch(theMult)
		if match != nil {
			tot += atoi(match[1]) * atoi(match[2])
		}
	}
	fmt.Println("a: ", tot)
}

func atoi(s string) int {
	value, _ := strconv.Atoi(s)
	return value
}

func main() {
	aFile, err := os.ReadFile("03.txt")
	if err != nil {
		fmt.Println(err)
	}

	str := string(aFile)

	processFileA(str)
}
