import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Client{
    
    @SuppressWarnings("unchecked")
    public static void main(String[] args) throws Exception{
        //Create input stream
        Scanner inFromUser=new Scanner(System.in);
        //Create client socket, connect to server
        Socket clientSocket = new Socket("localhost", 6789);
        //Create output stream attached to socket
        ObjectOutputStream outToServer = new ObjectOutputStream(clientSocket.getOutputStream());
        //Create input stream attached to socket
        ObjectInputStream inFromServer = new ObjectInputStream(clientSocket.getInputStream());
        
        //Get integers from user
        ArrayList<Integer> list = new ArrayList<Integer>();
        while(true){
            System.out.println("Enter an integer ('!' to send):");
            String input = inFromUser.next();
            if(input.equals("!")){
                break;
            }
            Integer entry = Integer.valueOf(input);
            list.add(entry);
        }
        
        //Send list to server
        outToServer.writeObject(list);
        System.out.println("Send: " + list.toString());
        
        //Get list from server
        ArrayList<Integer> primeList = new ArrayList<Integer>();
        primeList = (ArrayList<Integer>) inFromServer.readObject();
        System.out.println("Receive: " + primeList.toString());
        
        //Close socket
        clientSocket.close();
        
    }
    
}