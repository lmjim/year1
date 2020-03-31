import java.util.*;
import java.util.concurrent.*;

public class Producer implements Runnable{
    LinkedBlockingQueue<String> queue;
    static boolean finished = false;
    private int count = 0;
    
    public Producer(LinkedBlockingQueue<String> q){
        this.queue = q;
    }
    
    
    public void run(){
        
        for(int i = 0; i < 1000; i++){
            
            try{
                
                //Wait if queue is full
                while(queue.size() == 100){
                    Thread.sleep(10);
                }
                
                //Produces new queue entry
                Double random = Math.random();
                String randomString = Double.toString(random);
                queue.put(randomString);
                count++;
                
                //Prints producer updates
                if((count % 100) == 0){
                System.out.println("Producer 1: " + count + " events produced");
                }
                
            }catch(InterruptedException e){
                Thread.currentThread().interrupt();
            }
            
        }
        
        finished = true;
        
    }
    
    
    public int getCount(){
        return count;
    }
    
    
}