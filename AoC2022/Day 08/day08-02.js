import * as fs from 'fs';

const lines = fs.readFileSync('AoC2022/Day 08/input.txt','utf-8').split(/\r?\n/);
lines.pop(); // removing last empty line from array

const trees = [];
for (let y = 0; y < lines.length; y++) {
    trees[y] = lines[y].split('').map(Number);
    console.log(trees[y]);
}

const sideLen = trees.length;
for (let y = 1; y < sideLen - 1; y++) {

    for (let x = 1; x < sideLen - 1; x++) {
    }
}

// console.log(visible.reduce((a,v) => a + v.reduce((ia, iv) => ia + iv ? 1: 0, 0), 0));
let totalVis = 0;
for (let y = 0; y < sideLen; y++) {
    // console.log(visible[y].map(b => b == true ? '1': '0').join(''));
    let currVis = visible[y].reduce((a,v) => a + (v ? 1: 0), 0);
    // console.log(currVis);
    totalVis += currVis;
}
console.log(totalVis);

