import * as fs from 'node:fs';
import * as readline from 'node:readline/promises';

const inputStream = fs.createReadStream('AoC2022/Day 01/input.txt');
const lineRead = readline.createInterface({ input: inputStream});

let elfNumber = 1;
let calories = 0;
let maxCalories = calories;
let elfWithMaxCalories = elfNumber;

for await (const line of lineRead){
    if (line) {
        calories += Number(line);
    }
    else {
        if (calories > maxCalories) {
            elfWithMaxCalories = elfNumber
            maxCalories = calories
        };
        calories = 0;
        elfNumber++;
    }
}
console.log(`Elf # with max calories = ${elfWithMaxCalories}`);
console.log(`He carries this much calories = ${maxCalories}`);