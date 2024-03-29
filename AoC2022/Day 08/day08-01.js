import * as fs from 'fs';

const lines = fs.readFileSync('AoC2022/Day 08/input.txt','utf-8').split(/\r?\n/);
lines.pop(); // removing last empty line from array

const trees = [];
for (let y = 0; y < lines.length; y++) {
    trees[y] = lines[y].split('').map(Number);
    console.log(trees[y]);
}

const visible = [];
const sideLen = trees.length;
for (let y = 0; y < sideLen; y++) {
    let currHrowLeft = -1;
    let currHrowRight = -1;

    visible[y] = Array(sideLen).fill(false);

    for (let x = 0; x < sideLen; x++) {

        if (trees[y][x] > currHrowLeft) {
            visible[y][x] = true;
            currHrowLeft = trees[y][x];
        }

        if (trees[y][sideLen - x - 1] > currHrowRight) {
            visible[y][sideLen - x - 1] = true;
            currHrowRight = trees[y][sideLen - x - 1];
        }
    }
}

for (let x = 0; x < sideLen; x++) {
    let currHrowTop = -1;
    let currHrowBottom = -1;

    for (let y = 0; y < sideLen; y++) {

        if (trees[y][x] > currHrowTop) {
            visible[y][x] = true;
            currHrowTop = trees[y][x];
        }

        if (trees[sideLen - y - 1][x] > currHrowBottom) {
            visible[sideLen - y - 1][x] = true;
            currHrowBottom = trees[sideLen - y - 1][x];
        }
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

