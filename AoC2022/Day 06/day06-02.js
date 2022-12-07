import * as fs from 'fs';

const chars = fs.readFileSync('AoC2022/Day 06/input.txt','utf-8').trim().split('');
// const chars  = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'.split('');

const last14 = [];
let readChars = 0;

for (let c of chars) { 
    readChars++;
    if (last14.push(c) < 14) 
        continue;

    const set = new Set(last14);
    if (set.size == 14) {
        console.log(readChars);
        break;
    }
    last14.shift();
}