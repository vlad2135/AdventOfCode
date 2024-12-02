var lines = await File.ReadAllLinesAsync(@"..\..\..\input.txt");
var list1 = new List<int>();
var list2 = new List<int>();
foreach (var line in lines)
{
    var parts = line.Split(" ", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
    list1.Add(Int32.Parse(parts[0]));
    list2.Add(Int32.Parse(parts[1]));
}
list1.Sort();
list2.Sort();

int dist = 0;

for (int i = 0; i < list1.Count; i++)
{
    dist += Math.Max(list1[i], list2[i]) - Math.Min(list1[i], list2[i]);
}
Console.WriteLine(dist);