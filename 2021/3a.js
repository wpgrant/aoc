const fs = require('fs')
const lines = fs
  .readFileSync("3.txt", { encoding: "utf-8" })
  .split("\n")
  .filter((x) => Boolean(x))

let sums = new Array(lines[0].length).fill(0)
for (line of lines) {
  let chars = line.split('')
  for (let i = 0; i < chars.length; i++) {
    sums[i] += parseInt(chars[i])
  }
}
cntHalfLines = lines.length * .5
let gamma = new Array()
let epsilon = new Array()
for (let i = 0; i < sums.length; i++) {
  gamma[i] = (sums[i] >= cntHalfLines ? 1 : 0)
  epsilon[i] = (sums[i] < cntHalfLines ? 1 : 0)
}
gammaBinaryString = gamma.join("")
gammaNumber = parseInt(gammaBinaryString, 2)
epsilonBinaryString = epsilon.join("")
epsilonNumber = parseInt(epsilonBinaryString, 2)
console.log(gammaNumber*epsilonNumber)
