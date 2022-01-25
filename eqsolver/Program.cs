Console.WriteLine("A -> ");
int a = Int32.Parse(Console.ReadLine());
Console.WriteLine("B -> ");
int b = Int32.Parse(Console.ReadLine());
Console.WriteLine("C -> ");
int c = Int32.Parse(Console.ReadLine());

int delta = ((int)Math.Pow(b, 2)) - 4 * a * c;

if (delta > 0)
{
    float x1 = (b + (float)Math.Sqrt(delta)) / (2 * a);
    float x2 = (b - (float)Math.Sqrt(delta)) / (2 * a);
    Console.WriteLine("X1 = " + x1);
    Console.WriteLine("X2 = " + x2);
}
else if (delta == 0)
{
    float x = (b + (float)Math.Sqrt(delta)) / (2 * a);
    Console.WriteLine("X = " + x);
}
else if (delta < 0)
{
    Console.WriteLine("Equazione impossibile.");
}