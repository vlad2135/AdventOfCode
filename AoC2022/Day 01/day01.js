import * as fs from 'node:fs';
import * as readline from 'node:readline/promises';

const inputStream = fs.createReadStream('AoC2022/Day 01/input.txt');
const lineRead = readline.createInterface({ input: inputStream});

let calories = 0;
let caloriesArr = [];

for await (const line of lineRead){
    if (line) {
        calories += Number(line);
    }
    else {
        caloriesArr.push(calories)
        calories = 0;
    }
}
caloriesArr.sort((a,b) => b -a);
console.log(caloriesArr.slice(0,3).reduce((a,b) => a+b, 0));