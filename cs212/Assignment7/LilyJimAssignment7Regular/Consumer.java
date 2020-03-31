import java.util.*;
import java.util.concurrent.*;

public class Consumer implements Runnable{
    LinkedBlockingQueue<String> queue;
    private int id;
    private int count = 0;
    
    public Consumer(LinkedBlockingQueue<String> q, int number){
        this.queue = q;
        this.id = number;
    }
    
    public void run(){
        Random random = new Random();
        
        while(true){
            
            try{
                //Wait before consuming
                int sleepTime = random.nextInt(10);
                Thread.sleep(sleepTime); //[0,10) milliseconds
                
                //Consumes queue entry
                String poll = queue.poll(2, TimeUnit.SECONDS);
                
                //If queue was not empty
                if(poll != null){
                    count++;
                    
                    //Prints consumption updates
                    if((count % 100) == 0){
                        System.out.println("Consumer " + id + ": " + count + " events consumed");
                    }

                }else if((Producer.finished)){
                    //If queue was empty and Producer finished
                    break;
                }
                
            }catch(InterruptedException e){
                Thread.currentThread().interrupt();
            }
            
        }
        
    }
    
    
    public int getCount(){
        return count;
    }
    
    public int getID(){
        return id;
    }
    
}