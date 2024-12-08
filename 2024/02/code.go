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
		lastNum := -1
		lastChange := 0
		lastDirection := 0
		bSafe := true
		for _, num := range nums {
			iNum := atoi(num)
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
					break
				}
			}
		}
		if bSafe {
			totSafe += 1
		}
	}
	fmt.Println("a:", totSafe)
}

func processFileB(fileLines []string) {
	totSafe := 0
	for _, line := range fileLines {
		nums := strings.Split(line, " ")
		lastNum := -1
		lastChange := 0
		lastDirection := 0
		bSafe := true
		bSkippedOne := false
		for _, num := range nums {
			iNum := atoi(num)
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
					// Check if we skipped a level yet
					if !bSkippedOne {
						bSkippedOne = true
						bSafe = true
					} else {
						break
					}
				}
			}
		}
		if bSafe {
			totSafe += 1
		}
	}
	fmt.Println("b:", totSafe)
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
