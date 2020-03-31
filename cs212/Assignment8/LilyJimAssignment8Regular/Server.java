import java.io.*;
import java.net.*;
import java.util.ArrayList;

public class Server{
    
    @SuppressWarnings("unchecked")
    public static void main(String[] args) throws Exception{
        //Create welcoming socket
        ServerSocket welcomeSocket = new ServerSocket(6789);
        //Create ArrayLists
        ArrayList<Integer> list = new ArrayList<Integer>();
        ArrayList<Integer> primeList = new ArrayList<Integer>();
        
        while(true){
            //Wait on welcoming socket for contact by client
            Socket connectionSocket = welcomeSocket.accept();
            //Create input stream, attached to socket
            ObjectInputStream inFromClient = new ObjectInputStream(connectionSocket.getInputStream());
            //Create output stream, attached to socket
            ObjectOutputStream outToClient = new ObjectOutputStream(connectionSocket.getOutputStream());
            
            //Get list from socket
            list = (ArrayList<Integer>) inFromClient.readObject();
            
            //Have empty prime list
            primeList.clear();
            
            //Add to prime list
            for(int i = 0; i < list.size(); i++){
                if(isPrime(list.get(i))){
                    primeList.add(list.get(i));
                }
            }
            
            //Send prime list to socket
            outToClient.writeObject(primeList);
            
        }
        
    }
    
    
    //Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101...
    private static boolean isPrime(int num){
        if(num == 1 || num == 0){
            return false;
        }
        
        for(int i = 2; i < num; i++){
            if((num % i) == 0){
                return false;
            }
        }
        
        return true;
        
    }
    
    
}