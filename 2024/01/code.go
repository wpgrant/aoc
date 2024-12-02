package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func fileToArray(aFile *os.File) []string {
	fileScanner := bufio.NewScanner(aFile)
	fileScanner.Split(bufio.ScanLines)
	var fileLines []string

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	aFile.Close()

	return fileLines
}

func processFileA(fileLines []string) {
	// Parse lines into 2 slices, sort them, and find distances and add
	left := []int{}
	right := []int{}
	for _, line := range fileLines {
		nums := strings.Split(line, " ")
		leftInt, _ := strconv.Atoi(nums[0])
		rightInt, _ := strconv.Atoi(nums[1])
		left = append(left, leftInt)
		right = append(right, rightInt)
	}
}

func main() {
	aFile, err := os.Open("01a.txt")
	if err != nil {
		fmt.Println(err)
	}
	aLines := fileToArray(aFile)
	processFileA(aLines)
}
