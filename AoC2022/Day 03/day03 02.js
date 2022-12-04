import * as fs from 'node:fs';
import * as readline from 'node:readline/promises';

const inputStream = fs.createReadStream('AoC2022/Day 03/input.txt');
const lineRead = readline.createInterface({ input: inputStream });

let prioritySum = 0;

function getPriority(c) {
    const lowerCaseBase = 96;
    const upperCaseBase = 64;

    if (c == c.toLowerCase()) {
        return c.charCodeAt(0) - lowerCaseBase
    }
    else {
        return c.charCodeAt(0) - upperCaseBase + 26;
    }
}

let rucksackSets = [];
let currCnt = 1;
let set = new Set();

for await (const line of lineRead) {
    set = new Set();
    if (currCnt < 4) {
        let currLineArr = [...line.trim()];
        currLineArr.forEach(set.add.bind(set));
        rucksackSets.push(set);
        currCnt++;
        continue;
    }

    let crossOfSet12 = new Set();
    for (let c of rucksackSets[0]) {
        if (rucksackSets[1].has(c)) {
            crossOfSet12.add(c)
        }
    }

    for (let c of rucksackSets[2]) {
        if (crossOfSet12.has(c)) {
            prioritySum += getPriority(c);
            break;
        }
    }

    // 1st step of next group of 3
    rucksackSets = [];
    [...line.trim()].forEach(set.add.bind(set));
    rucksackSets.push(set);
    currCnt = 2;
}

let crossOfSet12 = new Set();
for (let c of rucksackSets[0]) {
    if (rucksackSets[1].has(c)) {
        crossOfSet12.add(c)
    }
}

for (let c of rucksackSets[2]) {
    if (crossOfSet12.has(c)) {
        prioritySum += getPriority(c);
        break;
    }
}

console.log(prioritySum);