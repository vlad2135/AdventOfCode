// See https://aka.ms/new-console-template for more information

using System.Text;

internal class Program
{
    static char[] numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    static char[] numsAndDot = numbers.Append('.').ToArray();
    private static void Main2(string[] args)
    {
        // (int num, int endIdx) = GetNextNumber(linesTest[1], 26);
        // Console.WriteLine(IsAdjacentToSymbol(linesTest, 1, endIdx - num.ToString().Length, endIdx));
        PrintANumber(@"...156...", 5);
        PrintANumber(@"...156", 5);
        PrintANumber(@"156", 0);
        PrintANumber(@"156..", 0);
        PrintANumber(@"156", 1);
        PrintANumber(@"156..", 1);
        PrintANumber(@"156", 2);
    }

    private static void PrintANumber(string str, int pos) {
        Console.WriteLine($"For line '{str}' and pos '{pos}' number is '{GetNumberFromPos(str, pos)}'.");
    }
    private static void Main(string[] args)
    {
        var lines = File.ReadAllLines(@"..\..\..\input3.txt");
        long gearRatioSum = 0;
        // Is there a faster way to iterate through line NUMBERS?
        for (int lineNum = 0; lineNum < lines.Length; lineNum++) {
            foreach (int gearIdx in GetGearIndexes(lines[lineNum]))
            {
                int[] adjacentPartNums = GetAjacentPartNums(lines, lineNum, gearIdx);
                if (adjacentPartNums.Length != 2) {
                    continue;
                }
                gearRatioSum += adjacentPartNums[0] * adjacentPartNums[1];
            }
        }
        Console.WriteLine(gearRatioSum); 

    }

    private static int[] GetAjacentPartNums(string[] lines, int lineNum, int gearIdx)
    {
        List<int> adjacentPartNums = new List<int>();

        for (int lNum = Math.Max(lineNum - 1, 0); lNum <= Math.Min(lineNum + 1, lines.Length-1); lNum++)
        {
            bool isNeedDotOrAsterisk = false;
            for (int idx = Math.Max(gearIdx - 1, 0); idx <= Math.Min(gearIdx+1, lines[lNum].Length-1); idx++) {
                if (lNum == lineNum && idx == gearIdx)
                {
                    isNeedDotOrAsterisk = false;
                    continue;
                }

                if (!isNeedDotOrAsterisk && numbers.Contains(lines[lNum][idx])) {
                    adjacentPartNums.Add(GetNumberFromPos(lines[lNum], idx));
                    isNeedDotOrAsterisk = true;
                }
                else if (lines[lNum][idx] == '.') {
                    isNeedDotOrAsterisk = false;
                }
            }
        }

        return adjacentPartNums.ToArray();
    }

    private static int GetNumberFromPos(string line, int idx)
    {
        int startIdx = idx;
        while (--startIdx >=0 && numbers.Contains(line[startIdx]));
        startIdx++;
        int endIdx = startIdx;
        while (++endIdx < line.Length && numbers.Contains(line[endIdx]));
        endIdx--;

        return Int32.Parse(line.Substring(startIdx, endIdx-startIdx+1));
    }

    private static IEnumerable<int> GetGearIndexes(string str)
    {
        for (int i = 0; i < str.Length; i++)
        {
            if (str[i] == '*') {
                yield return i;
            }
        }
    }

    private static void MainPart1(string[] args)
    {
        var lines = File.ReadAllLines(@"..\..\..\input3.txt");
        int partNumSum = 0;

        for (int i = 0; i < lines.Length; i++)
        {
            var line = lines[i];
            (int partNum, int endIdx) = GetNextNumber(line, 0);
            while (endIdx > -1)
            {
                if (IsAdjacentToSymbol(lines, i,
                        endIdx - partNum.ToString().Length + 1,
                        endIdx)) {
                    partNumSum += partNum;
                }

                if (endIdx + 1 < line.Length)
                    (partNum, endIdx) = GetNextNumber(line, endIdx + 1);
                else
                    break;
            }
        }

        Console.WriteLine(partNumSum);
    }


    static (int partNum, int endIdx) GetNextNumber(string line, int startIdx)
    {
        int numStartIdx = line.IndexOfAny(numbers, startIdx);
        if (numStartIdx == -1) {
            return (-1, -1); 
        }

        StringBuilder sb = new StringBuilder();
        sb.Append(line[numStartIdx]);
        int currIdx = numStartIdx + 1;
        while (currIdx < line.Length && numbers.Contains(line[currIdx])) 
        {
            sb.Append(line[currIdx++]);
        }

        return (Int32.Parse(sb.ToString()), currIdx - 1);
    }

    static bool IsAdjacentToSymbol(string[] lines, int lineNum, int startIdx, int endIdx)
    {
        for (int lNum = Math.Max(lineNum -1, 0); lNum <= Math.Min(lineNum + 1, lines.Length-1); lNum++)
        {
            for (int idx = Math.Max(startIdx - 1, 0); idx <= Math.Min(endIdx+1, lines[lNum].Length-1); idx++) {
                if (!numsAndDot.Contains(lines[lNum][idx]))
                {
                    return true;
                }

            }
        }

        return false;
    }
}