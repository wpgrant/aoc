const fs = require('fs')
const lines = fs
  .readFileSync("1.txt", { encoding: "utf-8" })
  .split("\n")
  .filter((x) => Boolean(x))
  .map((x) => parseInt(x))

let cnt = 0
prev = lines[0] + lines[1] + lines[2]
for (let i = 3; i < lines.length; i++) {
  current = lines[i-2] + lines[i-1] + lines[i]
  if (current > prev) {
    cnt++
  }
  prev = current
}
console.log(cnt)
