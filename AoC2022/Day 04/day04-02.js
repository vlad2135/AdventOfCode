import * as fs from 'node:fs';
import * as readline from 'node:readline/promises';

const inputStream = fs.createReadStream('AoC2022/Day 04/input.txt');
const lineRead = readline.createInterface({ input: inputStream });

let overlapCount = 0;
for await (const line of lineRead) {
    let [range1, range2] = line.trim().split(',');
    let [r1start, r1end] = range1.split('-').map(s => Number(s));
    let [r2start, r2end] = range2.split('-').map(s => Number(s));

    if ((r1start >= r2start && r1start <= r2end) ||
        (r2start >= r1start && r2start <= r1end)) {
            overlapCount++;
        }
}
console.log(overlapCount);