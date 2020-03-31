import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;
import java.util.Random;

public class Client{
    
    @SuppressWarnings("unchecked")
    public static void main(String[] args) throws Exception{
        //Create input stream
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        //Create list
        ArrayList<Integer> list = new ArrayList<Integer>();
        //Create random
        Random random = new Random();
        
        //Main loops
        boolean running = true;
        while(running){
            System.out.println("Enter '!' to start and stop, '#' to quit:");
            String input = inFromUser.readLine();
            if(input.equals("#")){
                running = false;
            }
            if(input.equals("!")){
                while(true){
                    //Randomly generate list of 5 integers [2,100)
                    list.clear();
                    for(int i = 0; i < 5; i++){
                        int num = random.nextInt(98) + 2;
                        list.add(num);
                    }
                    
                    //Create client socket, connect to server
                    Socket clientSocket = new Socket("localhost", 6789);
                    //Create output stream attached to socket
                    ObjectOutputStream outToServer = new ObjectOutputStream(clientSocket.getOutputStream());
                    //Create input stream attached to socket
                    ObjectInputStream inFromServer = new ObjectInputStream(clientSocket.getInputStream());

                    //Send list to server and print
                    outToServer.writeObject(list);
                    System.out.println("Send: " + list.toString());

                    //Get prime list from server and print
                    ArrayList<Integer> primeList = new ArrayList<Integer>();
                    primeList = (ArrayList<Integer>) inFromServer.readObject();
                    System.out.println("Receive: " + primeList.toString());

                    //Close socket
                    clientSocket.close();
                    
                    //Check for new input
                    if(inFromUser.ready()){
                        String next = inFromUser.readLine();
                        if(next.equals("#")){
                            running = false;
                            break;
                        }
                        if(next.equals("!")){
                            break;
                        }
                    }

                    //Sleep for one second before repeating
                    TimeUnit.SECONDS.sleep(1);
                }
            }
        }
    }
        
}