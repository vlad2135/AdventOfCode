// See https://aka.ms/new-console-template for more information


using System.ComponentModel;

var lines = await File.ReadAllLinesAsync(@"..\..\..\input.txt");
// var lines = await File.ReadAllLinesAsync(@"..\..\..\input_test.txt");
int row = 0, col =0;
for (row = 0; row < lines.Length; row++)
{
    col = lines[row].IndexOf('^');
    if (col > -1) 
    {
        break;
    }
}

Direction dir = Direction.Up;
while (true)
{
    lines[row] = lines[row][..col] + "X" + lines[row][(col+1)..];

    (int nextRow, int nextCol) = GetNextPos(lines, row, col, dir);
    if (nextRow < 0 || nextRow >= lines.Length ||
       nextCol < 0 || nextCol >= lines[0].Length)
    {
        break;
    }
    if (lines[nextRow][nextCol] == '#')
    {
        dir = TurnRight(dir);
    }
    else
    {
        row = nextRow;
        col = nextCol;
    }
}

long visited = 0;
foreach (var line in lines)
{
    foreach (var c in line)
    {
        if (c == 'X')
        {
            visited++;
        }
    }
}
Console.WriteLine(visited);

(int nextRow, int nextCol) GetNextPos(string[] lines, int row, int col, Direction dir)
{
    return dir switch {
        Direction.Up => (row - 1, col),
        Direction.Down => (row + 1, col),
        Direction.Left => (row, col - 1),
        Direction.Right => (row, col + 1),
        _ => throw new InvalidEnumArgumentException()
    };
}

Direction TurnRight(Direction dir)
{
    return dir switch {
        Direction.Up => Direction.Right,
        Direction.Down => Direction.Left,
        Direction.Left => Direction.Up,
        Direction.Right => Direction.Down,
        _ => throw new InvalidEnumArgumentException()
    };
}

enum Direction
{
    Up,
    Down,
    Left,
    Right,
}