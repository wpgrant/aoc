const fs = require('fs')
const lines = fs
  .readFileSync("1.txt", { encoding: "utf-8" })
  .split("\n")
  .filter((x) => Boolean(x))
  .map((x) => parseInt(x))

let cnt = 0
let prevVal = 0
for (line of lines) {
  if (line > prevVal) {
    cnt++
  }
  prevVal = line
}
// Don't count the first one
cnt--
console.log(cnt)
