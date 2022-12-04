let choiceScore = { 'X': 1, 'Y': 2, 'Z': 3};
let outcomeScores = 
{
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3
    }
}

import * as fs from 'node:fs';
import * as readline from 'node:readline/promises';

const inputStream = fs.createReadStream('AoC2022/Day 02/input.txt');
const lineRead = readline.createInterface({ input: inputStream});

let totalScore = 0;
for await (const line of lineRead){
    let [oppChoice, myChoice] = line.trim().split(' ');
    totalScore += outcomeScores[oppChoice][myChoice] + choiceScore[myChoice];
}
console.log(totalScore);