// See https://aka.ms/new-console-template for more information

using System.Text;

internal class Program
{
    static string test = @"...846................132.49........308..........................=............50.....*..............*........+.....+...............59.......A";
    static string[] linesTest = [
        @"........................................................862...........20.............453...619......58........694...312.................292.",
        @"...846................132.49........308..........................=............50.....*..............*........+.....+...............59.......",
        @"........../46....140.......*............735......852&..706.....860...............297.459..........998................661..418.883.......+..."
    ];
    static char[] numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    static char[] numsAndDot = numbers.Append('.').ToArray();
    private static void Main2(string[] args)
    {
        (int num, int endIdx) = GetNextNumber(linesTest[1], 26);
        Console.WriteLine(IsAdjacentToSymbol(linesTest, 1, endIdx - num.ToString().Length, endIdx));
    }
    private static void Main(string[] args)
    {
        var lines = File.ReadAllLines(@"..\..\..\input3.txt");
        Console.WriteLine(lines.Length);
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
        while (currIdx < line.Length &&
               numbers.Any(n => n == line[currIdx])) 
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