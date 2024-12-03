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
  sort.Ints(left)
  sort.Ints(right)

  diffTotal := 0
  for i:=0; i<len(left); i++ {
    diff := abs(left[i] - right[i])
    diffTotal += diff
  }
  fmt.Println(diffTotal)
}

func abs[T float64 | int](x T) T {
  if x < 0 {
    return -x
  }
  return x
}

func main() {
  aFile, err := os.Open("01a.txt")
  if err != nil {
    fmt.Println(err)
  }
  aLines := fileToArray(aFile)
  processFileA(aLines)
}
