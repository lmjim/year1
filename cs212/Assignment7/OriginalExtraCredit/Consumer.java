import java.util.*;
import java.util.concurrent.*;

public class Consumer implements Runnable{
    LinkedList<String> queue;
    private int id;
    private int count;
    
    public Consumer(LinkedList<String> q, int number){
        this.queue = q;
        this.id = number;
    }
    
    
    public void run(){
        Random random = new Random();
        
            while((!Producer.finished) || (queue.size() > 0)){
                
                //Wait for queue to have entries
                while((!Producer.finished) && (queue.size()==0)){

                    try{
                        Thread.sleep(10);
                    }catch(InterruptedException e){
                        Thread.currentThread().interrupt();
                    }

                }

                synchronized(queue){
                    //Consumes queue entry
                    String poll = queue.poll();
                    if(poll != null){
                        count++;

                        //Prints consumption updates
                        if((count % 100) == 0){
                            System.out.println("Consumer " + id + ": " + count + " events consumed");
                        }
                    }
                }
                
                //Wait before consuming more
                try{
                    int sleepTime = random.nextInt(10); //[0,10)
                    Thread.sleep(sleepTime);

                }catch(InterruptedException e){
                    Thread.currentThread().interrupt();
                }
        
        }
        
    }
    
    
    public int getID(){
        return id;
    }
    
    
    public int getCount(){
        return count;
    }
    
}