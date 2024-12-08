// See https://aka.ms/new-console-template for more information

var lines = await File.ReadAllLinesAsync(@"..\..\..\input.txt");
// var lines = await File.ReadAllLinesAsync(@"..\..\..\input_test.txt");
char[][] letters = new char[lines.Length][];
for (int i = 0; i < lines.Length; i++)
{
    letters[i] = lines[i].ToCharArray();
}
int occurrences = 0;

for (int row = 0; row < lines.Length; row++)
{
    for (int col = 0; col < lines[0].Length; col++)
    {
        if (lines[row][col] != 'X')
        {
            continue;
        }

        if (IsMAS(lines, row, col, Direction.Up))
        {
            occurrences++;
        }
        if (IsMAS(lines, row, col, Direction.Down))
        {
            occurrences++;
        }
        if (IsMAS(lines, row, col, Direction.Left))
        {
            occurrences++;
        }
        if (IsMAS(lines, row, col, Direction.Right))
        {
            occurrences++;
        }
        if (IsMAS(lines, row, col, Direction.UpLeft))
        {
            occurrences++;
        }
        if (IsMAS(lines, row, col, Direction.DownLeft))
        {
            occurrences++;
        }
        if (IsMAS(lines, row, col, Direction.UpRight))
        {
            occurrences++;
        }
        if (IsMAS(lines, row, col, Direction.DownRight))
        {
            occurrences++;
        }
    }
}

Console.WriteLine(occurrences);

bool IsMAS(string[] lines, int row, int col, Direction dir)
{
    switch (dir)
    {
        case Direction.Down:
            if (row > lines.Length - 4)
            {
                return false;
            }
            return lines[row+1][col] == 'M' && 
                lines[row+2][col] == 'A' && 
                lines[row+3][col] == 'S';
        case Direction.Up:
            if (row < 3)
            {
                return false;
            }
            return lines[row-1][col] == 'M' && 
                lines[row-2][col] == 'A' && 
                lines[row-3][col] == 'S';
        case Direction.Left:
            if (col < 3)
            {
                return false;
            }
            return lines[row][col-1] == 'M' && 
                lines[row][col-2] == 'A' && 
                lines[row][col-3] == 'S';
        case Direction.Right:
            if (col > lines[0].Length - 4)
            {
                return false;
            }
            return lines[row][col+1] == 'M' && 
                lines[row][col+2] == 'A' && 
                lines[row][col+3] == 'S';
        case Direction.DownRight:
            if (row > lines.Length - 4 || col > lines[0].Length - 4)
            {
                return false;
            }
            return lines[row+1][col+1] == 'M' && 
                lines[row+2][col+2] == 'A' && 
                lines[row+3][col+3] == 'S';
        case Direction.DownLeft:
            if (row > lines.Length - 4 || col < 3)
            {
                return false;
            }
            return lines[row+1][col-1] == 'M' && 
                lines[row+2][col-2] == 'A' && 
                lines[row+3][col-3] == 'S';
        case Direction.UpRight:
            if (row < 3 || col > lines[0].Length - 4)
            {
                return false;
            }
            return lines[row-1][col+1] == 'M' && 
                lines[row-2][col+2] == 'A' && 
                lines[row-3][col+3] == 'S';
        case Direction.UpLeft:
            if (row < 3 || col < 3)
            {
                return false;
            }
            return lines[row-1][col-1] == 'M' && 
                lines[row-2][col-2] == 'A' && 
                lines[row-3][col-3] == 'S';

        default:
            throw new InvalidOperationException();

    }
}

enum Direction {
    Up,
    Down,
    Left,
    Right,
    DownRight,
    DownLeft,
    UpRight,
    UpLeft,
}
