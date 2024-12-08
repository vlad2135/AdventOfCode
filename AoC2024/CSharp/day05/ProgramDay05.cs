// See https://aka.ms/new-console-template for more information
bool is1stPart = true;
Dictionary<int, (HashSet<int> before, HashSet<int> after)> rules = new Dictionary<int, (HashSet<int>, HashSet<int>)>();
int addedMiddleNumbers = 0;
// await foreach (var line in File.ReadLinesAsync(@"..\..\..\input_test.txt"))
await foreach (var line in File.ReadLinesAsync(@"..\..\..\input.txt"))
{
    if (string.IsNullOrWhiteSpace(line))
    {
        is1stPart = false;
        continue;
    }

    if (is1stPart) {
        var values = line.Split("|").Select(Int32.Parse);
        AddToRules(values.First(), values.Last());
    }
    else
    {
        // addedMiddleNumbers += GetMiddleOfCorrectUpdate(line.Split(",").Select(Int32.Parse).ToList());
        var update = line.Split(",").Select(Int32.Parse).ToList();
        if (IsInCorrectOrder(update))
        {
            continue;
        }
        addedMiddleNumbers += GetMiddleOfCorrectedUpdate(update);
    }
}

Console.WriteLine(addedMiddleNumbers);

void AddToRules(int before, int after)
{
    if (!rules.TryGetValue(before, out var _))
    {
        rules[before] = new (new HashSet<int>(), new HashSet<int>());
    }
    rules[before].after.Add(after);

    if (!rules.TryGetValue(after, out var _))
    {
        rules[after] = new (new HashSet<int>(), new HashSet<int>());
    }
    rules[after].before.Add(before);
}

int GetMiddleOfCorrectUpdate(List<int> update)
{
    return IsInCorrectOrder(update) ? update[update.Count / 2] : 0;
}

bool IsInCorrectOrder(List<int> update)
{
    bool isRightOrder = true;
    for (int i = 0; i < update.Count; i++)
    {
        if (rules[update[i]].before.Intersect(update.GetRange(i, update.Count - i)).Any())
        {
            isRightOrder = false;
            break;
        }
        if (rules[update[i]].after.Intersect(update.GetRange(0, i)).Any())
        {
            isRightOrder = false;
            break;
        }
    }
    return isRightOrder;
}

int GetMiddleOfCorrectedUpdate(List<int> update)
{
    do {
        List<int> nextIterUpdate = update.ToList();
        for (int i = 0; i < update.Count; i++)
        {
            var moveFromAfterToBefore = rules[update[i]].before.Intersect(update.GetRange(i, update.Count - i));
            foreach (var number in moveFromAfterToBefore)
            {
                nextIterUpdate.Remove(number);
                nextIterUpdate.Insert(0, number);
            }
            if (moveFromAfterToBefore.Any())
            {
                break;
            }
            var moveFromBeforeToAfter = rules[update[i]].after.Intersect(update.GetRange(0, i));
            foreach (var number in moveFromBeforeToAfter)
            {
                nextIterUpdate.Remove(number);
                nextIterUpdate.Add(number);
                break;
            }
            if (moveFromBeforeToAfter.Any())
            {
                break;
            }
        }
        update = nextIterUpdate;
    } while (!IsInCorrectOrder(update));

    return update[update.Count / 2];
}