import * as fs from 'fs';

const lines = fs.readFileSync('AoC2022/Day 07/input.txt','utf-8').split(/\r?\n/);
lines.pop(); // removing last empty line from array

const fsRoot = { name: '/', content: [] };

const fsRoot2 = {
    '/': {
        content: {
        'drblq': { content: {}, parent: 'link to parent folder object', size: 100 },
        'fjf': { size: 133789 }
        },
        parent: '',
        size: 100
    }
}
let linePos = 1;

function getFolderSizeAndFillUnder100k(name, lines, dirsUnder100k) {
    if (lines[linePos] != '$ ls') {
        console.error(`Broken source data at line ${linePos}, value is not equal to $ ls!`);
        process.exit(1);
    }
    let folderSize = 0;
    linePos++;
    const subFolders = {};
    while (lines[linePos] != '$ cd ..' && linePos < lines.length) {
        let val1, val2, val3;
        [val1, val2, val3] = lines[linePos].split(' ');
        switch (val1) {
            case 'dir':
                subFolders[val2] = 0;
                break;
            case '$':
                if (val2 != 'cd') {
                    console.error(`Error in algorithm on line ${linePos}, expected $ cd, but found ${lines[linePos]}!`);
                    process.exit(1);
                }
                linePos++;
                folderSize += getFolderSizeAndFillUnder100k(val3, lines, dirsUnder100k);
                break;
            default:
                folderSize += Number(val1);
        }
        linePos++;
    }

    if (folderSize <= 100000) {
        dirsUnder100k.push(folderSize);
    }

    return folderSize;
}

const dirsUnder100k = [];


const rootSize = getFolderSizeAndFillUnder100k('/', lines, dirsUnder100k);

console.log(dirsUnder100k.reduce((a,b) => a+b, 0));

