// See https://aka.ms/new-console-template for more information
bool IsSafe(int[] levels)
{
    int incrOrDecr = 0;
    bool isSafe = true;
    for (int i = 1; i < levels.Length; i++)
    {
        int delta = Math.Abs(levels[i] - levels[i-1]);
        if (delta > 3 || delta < 1) {
            isSafe = false;
            break;
        };
        int currIncrOrDecr = levels[i] > levels[i - 1] ? 1 : -1;
        if (incrOrDecr == 0)
        {
            incrOrDecr = currIncrOrDecr;
        }
        else
        {
            if (currIncrOrDecr != incrOrDecr)
            {
                isSafe = false;
                break;
            }
        }
    }
    return isSafe;
}

var lines = await File.ReadAllLinesAsync(@"..\..\..\input.txt");
int safeCnt = 0;
foreach (var line in lines)
{
    int[] levels = line.Split(' ').Select(Int32.Parse).ToArray();

    bool isSafe = IsSafe(levels);
    if (isSafe)
    {
        safeCnt++;
    }
    else
    {
        for (int i = 0; i < levels.Length; i++)
        {
            List<int> tmp = levels.ToList();
            tmp.RemoveAt(i);
            int[] dampened = tmp.ToArray();
            if (IsSafe(dampened))
            {
                safeCnt++;
                break;
            }
        }
    }
}
Console.WriteLine(safeCnt);