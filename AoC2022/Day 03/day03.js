import * as fs from 'node:fs';
import * as readline from 'node:readline/promises';

const inputStream = fs.createReadStream('AoC2022/Day 03/input.txt');
const lineRead = readline.createInterface({ input: inputStream});

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

for await (const line of lineRead){
    let rucksack = line.trim();
    let comp1 = rucksack.substring(0, rucksack.length / 2);
    let comp2 = rucksack.substring(rucksack.length / 2);
    let comp1Set = new Set();
    for (let c of comp1) {
        comp1Set.add(c);
    }
    let duplicateType = '';
    for (let c of comp2) {
        if (comp1Set.has(c)) {
            duplicateType = c;
            break;
        }
    }
    prioritySum += getPriority(duplicateType);
}

console.log(prioritySum);