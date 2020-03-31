import java.util.*;
import java.util.concurrent.*;

public class Producer implements Runnable{
    LinkedList<String> queue;
    private int id;
    private int count;
    static boolean finished = false;
    static int produced = 0;
    
    public Producer(LinkedList<String> q, int number){
        this.queue = q;
        this.id = number;
    }
    
    
    public void run(){
        Random random = new Random();
        
        while(true){
                
            //Waits if queue is full
            while(queue.size() == 100){
                try{
                    Thread.sleep(10);
                }catch(InterruptedException e){
                    Thread.currentThread().interrupt();
                }
            }
                
            synchronized(queue){
                //If queue is not full
                if(produced < 1000){
                    //Produces new queue entry
                    Double random2 = Math.random();
                    String randomString = Double.toString(random2);
                    queue.add(randomString);
                    count++;
                    produced++;

                    //Prints producer updates
                    if((count % 100) == 0){
                    System.out.println("Producer " + id + ": " + count + " events produced");
                    } 
                }
                else{
                    break;
                }
            }
                
            //Wait before producing more
            try{
                int sleepTime = random.nextInt(10);
                Thread.sleep(sleepTime);
            }catch(InterruptedException e){
                Thread.currentThread().interrupt();
            }
            
        }
        
        finished = true;
        
    }
    
    
    public int getID(){
        return id;
    }
    
    
    public int getCount(){
        return count;
    }
    
    
}