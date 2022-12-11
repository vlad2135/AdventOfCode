import * as fs from 'fs';

const lines = fs.readFileSync('AoC2022/Day 08/input_train.txt','utf-8').split(/\r?\n/);
lines.pop(); // removing last empty line from array

const trees = [];
for (let y = 0; y < lines.length; y++) {
    trees[y] = lines[y].split('').map(Number);
    console.log(trees[y]);
}

const visible = [];
const sideLen = trees.length;
for (let y = 0; y < trees.length; y++) {
    let currHrowLeft = -1;
    let currHrowRight = -1;
    let currHrowTop = -1;
    let currHrowBottom = -1;

    visible[y] = Array(sideLen).fill(false);
    if (visible[sideLen - y - 1] === undefined) {
        visible[sideLen - y - 1] = Array(sideLen).fill(false);
    }

    let stopOnLeft = false;
    let stopOnRight = false;
    let stopOnTop = false;
    let stopOnBottom = false;
    for (let x = 0; x < sideLen; x++) {

        if (!stopOnLeft && trees[y][x] > currHrowLeft) {
            visible[y][x] = true;
            currHrowLeft = trees[y][x];
        }
        else { stopOnLeft = true; }

        if (!stopOnRight && trees[y][sideLen - x - 1] > currHrowRight) {
            visible[y][sideLen - x - 1] = true;
            currHrowRight = trees[y][sideLen - x - 1];
        }
        else { stopOnRight = true; }

        // vertical direction, using the fact that field is square
        if (!stopOnTop && trees[x][y] > currHrowTop) {
            visible[x][y] = true;
            currHrowTop = trees[x][y];
        }
        else { stopOnTop = true; }

        if (!stopOnBottom && trees[sideLen - x - 1][y] > currHrowBottom) {
            visible[sideLen - x - 1][y] = true;
            currHrowBottom = trees[sideLen - x - 1][y];
        }
        else { stopOnBottom = true; }

        if (stopOnLeft && stopOnRight && stopOnTop && stopOnBottom) {
            break;
        }
    }
}
// console.log(visible.reduce((a,v) => a + v.reduce((ia, iv) => ia + iv ? 1: 0, 0), 0));
for (let y = 0; y < sideLen; y++) {
    console.log(visible[y].map(b => b == true ? '1': '0').join(''));
    // console.log(visible[y].reduce((a,v) => a + (v ? 1: 0), 0));
}

