using System;
using System.Collections.Generic;
class Temperature
{
    public static int Main(string[] args)
    {
        int[] T = new int[] {73, 74, 75, 71, 69, 72, 76, 73};   // Sample input to test the logic
        int[] Ans = new int[T.Length];
        Stack<int> stack = new Stack<int>();
        stack.Push(T.Length-1);
        Ans[T.Length-1] = 0;    // This is always true last element in the ans array will be 0
        for(int i=T.Length-1;i>=0;i--) {
            while(stack.Count>0) {
                int index = stack.Peek();     // Peek gets you the top element without removing it from the stack
                if(T[i]>=T[index]) {
                    stack.Pop();
                }
                else {
                    Ans[i] = index - i;
                    break;
                }
            }
            stack.Push(i);
        }
        // Array.ForEach(Ans, System.Console.WriteLine);    // prints the array element in new line
        System.Console.WriteLine("[{0}]", string.Join(", ", Ans));  // prints the array element in single line as list
        return 0;
    }
}


/*
To run this code install .net framework and add csc compiler to your system path
goto Temperature.cs path
csc Temperature.cs
Temperature

*/