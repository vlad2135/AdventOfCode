string[] lines = File.ReadAllLines(@"..\..\..\input4.txt");

long points = 0;

foreach (var line in lines) {
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
        points += (int)Math.Pow(2, winCount - 1);
    }
}

Console.WriteLine(points);