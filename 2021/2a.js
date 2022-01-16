const fs = require('fs')
const moves = fs
  .readFileSync("2.txt", { encoding: "utf-8" })
  .split("\n")
  .filter((x) => Boolean(x))

let horiz = 0 // fw +
let depth = 0 // down +, up -

for (move of moves) {
  let [dir, num] = move.split(' ')
  num = parseInt(num)
  if (dir === 'forward') {
    horiz += num
  } else 
    depth += (dir === 'down' ? num : -num)
}

console.log(horiz * depth)
