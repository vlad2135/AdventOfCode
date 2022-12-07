import * as fs from 'fs';

const chars = fs.readFileSync('AoC2022/Day 06/input.txt','utf-8').trim().split('');
// const chars  = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'.split('');

const last4 = [];
let readChars = 0;

for (let c of chars) { 
    readChars++;
    if (last4.push(c) < 4) 
        continue;

    const set = new Set(last4);
    if (set.size == 4) {
        console.log(readChars);
        break;
    }
    last4.shift();
}