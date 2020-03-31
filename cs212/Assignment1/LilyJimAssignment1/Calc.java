import java.util.Scanner;

class Calc{
    
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int sum = 0;
        
        while (true)
        {
            //Get user command:
            System.out.println("Enter p to print, r to reset, q to quit, and i to add an integer:");
            String command = input.next();
            
            //Do something if command is p, r, q, or i (or restart loop/ask for command again)
            if(command.equals("q"))  // Print current sum and Quit program
            {
                System.out.println("Sum: " + sum);
                break;
            }
            else if(command.equals("i"))  // Ask for input and Add input to current sum
            {
                System.out.println("Enter the integer:");
                int i = input.nextInt();
                sum += i;
            }
            else if(command.equals("p"))  // Print current sum
            {
                System.out.println("Sum: " + sum);
            }
            else if(command.equals("r"))  // Reset sum to 0 and Print
            {
                sum = 0; 
                System.out.println("Sum: " + sum);
            }
            else
            {
                continue;
            }
            
        }
    }
}
