import * as fs from 'fs';

const lines = fs.readFileSync('AoC2022/Day 05/input.txt','utf-8').split(/\r?\n/);

let stacks = [[],[],[],[],[],[],[],[],[]];

for (let i = 7; i >= 0; i--) {
    let crates = lines[i].split('');
    if (crates[1] != ' ') stacks[0].push(crates[1]);
    if (crates[5] != ' ') stacks[1].push(crates[5]);
    if (crates[9] != ' ') stacks[2].push(crates[9]);
    if (crates[13] != ' ') stacks[3].push(crates[13]);
    if (crates[17] != ' ') stacks[4].push(crates[17]);
    if (crates[21] != ' ') stacks[5].push(crates[21]);
    if (crates[25] != ' ') stacks[6].push(crates[25]);
    if (crates[29] != ' ') stacks[7].push(crates[29]);
    if (crates[33] != ' ') stacks[8].push(crates[33]);
}

for (let ln = 10; ln < lines.length; ln++) {
    let cmdParts = lines[ln].split(' ');
    let cnt = cmdParts[1];
    let from = cmdParts[3] - 1;
    let to = cmdParts[5] - 1;

    for (let move = 1; move <= cnt; move++) {
        stacks[to].push(stacks[from].pop());
    }
}

console.log(stacks.map(s => s.pop() ?? ' ').join(''))