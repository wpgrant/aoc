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
	totSafe := 0
	for _, line := range fileLines {
		nums := strings.Split(line, " ")
		bSuccess, _ := testLevel(nums)
		if bSuccess {
			totSafe += 1
		}
	}
	fmt.Println("a:", totSafe)
}

func processFileB(fileLines []string) {
	totSafe := 0
	for _, line := range fileLines {
		nums := strings.Split(line, " ")
		bSuccess, failedLevel := testLevel(nums)
		if bSuccess {
			totSafe += 1
		} else {
			// Test levels with 1) first removed, previous removed, and current removed
			// First
			testCombined := nums[1:]
			bSuccess, _ := testLevel(testCombined)
			if bSuccess {
				totSafe += 1
			} else {
				// Previous
				testNums := nums[0 : failedLevel-1]
				testRest := nums[failedLevel:]
				testCombined := append([]string{}, testNums...)
				testCombined = append(testCombined, testRest...)
				bSuccess, _ := testLevel(testCombined)
				if bSuccess {
					totSafe += 1
				} else {
					// Current
					testNums := nums[0:failedLevel]
					testRest := nums[failedLevel+1:]
					testCombined := append([]string{}, testNums...)
					testCombined = append(testCombined, testRest...)
					bSuccess, _ := testLevel(testCombined)
					if bSuccess {
						totSafe += 1
					}
				}
			}
		}
	}
	fmt.Println("b:", totSafe)
}

func testLevel(nums []string) (success bool, levelFailed int) {
	lastNum := -1
	lastChange := 0
	lastDirection := 0
	bSafe := true
	for i := 0; i < len(nums); i++ {
		iNum := atoi(nums[i])
		if lastNum == -1 {
			// First number, just accept it
			lastNum = iNum
		} else {
			lastChange = iNum - lastNum
			// Check if change is a good size
			if abs(lastChange) >= 1 && abs(lastChange) <= 3 {
				bSafe = true
			} else {
				bSafe = false
			}
			// Check if change is right direction
			if bSafe && (lastChange*lastDirection >= 0) {
				bSafe = true
			} else {
				bSafe = false
			}
			// if safe, keep checking; if not, break
			if bSafe {
				lastDirection = lastChange
				lastNum = iNum
			} else {
				return false, i
			}
		}
	}
	return true, -1
}

func atoi(s string) int {
	value, _ := strconv.Atoi(s)
	return value
}

func abs[T float64 | int](x T) T {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	aFile, err := os.Open("02.txt")
	if err != nil {
		fmt.Println(err)
	}
	theLines := fileToArray(aFile)
	processFileA(theLines)
	processFileB(theLines)
}
