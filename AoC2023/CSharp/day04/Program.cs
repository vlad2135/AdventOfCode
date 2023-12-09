string[] lines = File.ReadAllLines(@"..\..\..\input4.txt");

long wonCardsCnt = 0;
int[] applyCount = new int[lines.Length];
Array.Fill(applyCount, 1);

for (int i = 0; i < lines.Length; i++) {
    var line = lines[i];
    var p = line.Split(':', StringSplitOptions.TrimEntries); 

    var numbers = p[1].Split('|', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);

    var winNums = numbers[0].Split(' ', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries).Select(Int32.Parse).ToList();

    var myNums = numbers[1].Split(' ', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
    List<int> sortedMyNums = myNums.Select(Int32.Parse).ToList();
    sortedMyNums.Sort();

    int winCount = 0;
    foreach (int winNum in winNums) {
        if (sortedMyNums.BinarySearch(winNum) >= 0) {
            winCount++;
        }
    }

    if (winCount > 0)
    {
        for (int j = i+1; j < i+1+winCount; j++)
        {
            applyCount[j] = applyCount[j]*2;
        }
        Console.WriteLine($"Card N{i} has {winCount} wins * {applyCount[i]} times");
        wonCardsCnt += winCount * applyCount[i];
    }
    else {
        Console.WriteLine($"Card N{i+1} did not won anything");
    }
}

Console.WriteLine(wonCardsCnt + lines.Length);