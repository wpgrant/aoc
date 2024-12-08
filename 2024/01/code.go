package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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
	left, right := createLists(fileLines)
	sort.Ints(left)
	sort.Ints(right)

	diffTotal := 0
	for i := 0; i < len(left); i++ {
		diff := abs(left[i] - right[i])
		diffTotal += diff
	}
	fmt.Println("a: ", diffTotal)
}

func processFileB(fileLines []string) {
	// Parse lines into 2 slices, for each number on left count instances, multiply and add
	left, right := createLists(fileLines)
	mapOcc := map[int]int{}
	total := 0
	for i := 0; i < len(left); i++ {
		if mapOcc[left[i]] == 0 {
			newCnt := countVals(right, left[i])
			mapOcc[left[i]] = newCnt
			if newCnt >= 0 {
				total += left[i] * newCnt
			}
		} else if mapOcc[left[i]] > 0 {
			total += left[i] * mapOcc[left[i]]
		}
	}
	fmt.Println("b: ", total)
}

func countVals(theSlice []int, theNum int) int {
	cnt := 0
	for i := 0; i < len(theSlice); i++ {
		if theSlice[i] == theNum {
			cnt += 1
		}
	}
	if cnt > 0 {
		return cnt
	} else {
		// Populate it with -1 so it's ignored later
		return -1
	}
}

func createLists(fileLines []string) ([]int, []int) {
	// Parse lines into 2 slices, sort them, and find distances and add
	left := []int{}
	right := []int{}
	for _, line := range fileLines {
		nums := strings.Split(line, "   ")
		leftInt, err := strconv.Atoi(nums[0])
		if err != nil {
			fmt.Println(err)
		}
		rightInt, err := strconv.Atoi(nums[1])
		if err != nil {
			fmt.Println(err)
		}
		left = append(left, leftInt)
		right = append(right, rightInt)
	}
	return left, right
}

func abs[T float64 | int](x T) T {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	aFile, err := os.Open("01.txt")
	if err != nil {
		fmt.Println(err)
	}
	aLines := fileToArray(aFile)
	processFileA(aLines)
	processFileB(aLines)
}
