// See https://aka.ms/new-console-template for more information
using System.Text.RegularExpressions;

var lines = await File.ReadAllLinesAsync(@"..\..\..\input.txt");
// string[] lines = [@"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"];
// string[] lines = [@"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"];

Regex mulRx = new Regex(@"mul\((\d{1,3}),(\d{1,3})\)", RegexOptions.Compiled);
Regex dontDoRx = new Regex(@"don't\(\).+?(do\(\)|$)", RegexOptions.Compiled);

long sum = 0;

File.Delete(@"..\..\..\input_cut.txt");
string line = "";

for (int i = 0; i < lines.Length; i++)
{
    line += lines[i];
}
    line = dontDoRx.Replace(line, "!!!");
    File.AppendAllLines(@"..\..\..\input_cut.txt", [line]);

    var match = mulRx.Match(line); 

    while (match.Success)
    {
        Console.WriteLine(match.Groups[0].Value);
        long m1 = Int64.Parse(match.Groups[1].Value);
        long m2 = Int64.Parse(match.Groups[2].Value);
        sum = sum + (m1 * m2);

        match = match.NextMatch();
    }

Console.WriteLine(sum);