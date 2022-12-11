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

function getFolderSize(name, lines, dirSizes) {
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
                folderSize += getFolderSize(val3, lines, dirSizes);
                break;
            default:
                folderSize += Number(val1);
        }
        linePos++;
    }

    dirSizes.push(folderSize);

    return folderSize;
}

const dirSizes = [];


const usedSpace = getFolderSize('/', lines, dirSizes);
const requiredCleanupSize = 30000000 - (70000000 - usedSpace);

dirSizes.sort((a,b) => b - a);
for (let size of dirSizes) {
    if (size >= requiredCleanupSize) {
        console.log(size);
        break;
    }
}

