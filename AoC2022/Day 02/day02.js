let choiceScore = { 'rock': 1, 'paper': 2, 'scissors': 3};
let outcomeScore = { 'X': 0, 'Y': 3, 'Z': 6};
let choise2win = 
{
    'A': { 
        'X': 'scissors',
        'Y': 'rock',
        'Z': 'paper'
    },
    'B': {
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissors'
    },
    'C': {
        'X': 'paper',
        'Y': 'scissors',
        'Z': 'rock'
    }
}

import * as fs from 'node:fs';
import * as readline from 'node:readline/promises';

const inputStream = fs.createReadStream('AoC2022/Day 02/input.txt');
const lineRead = readline.createInterface({ input: inputStream});

let totalScore = 0;
for await (const line of lineRead){
    let [oppChoice, outcome] = line.trim().split(' ');
    totalScore += choiceScore[choise2win[oppChoice][outcome]] + outcomeScore[outcome];
}
console.log(totalScore);