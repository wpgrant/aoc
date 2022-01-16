const fs = require('fs')
const moves = fs
  .readFileSync("2.txt", { encoding: "utf-8" })
  .split("\n")
  .filter((x) => Boolean(x))

let horiz = 0 // fw +x
let aim = 0 // down +x, up -x
let depth = 0 // when fw, aim * x

for (move of moves) {
  let [dir, num] = move.split(' ')
  num = parseInt(num)
  if (dir === 'forward') {
    horiz += num
    depth += num * aim
  } else 
    aim += (dir === 'down' ? num : -num)
}

console.log(horiz * depth)
