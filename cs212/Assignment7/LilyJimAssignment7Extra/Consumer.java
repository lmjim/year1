import java.util.*;
import java.util.concurrent.*;

public class Consumer implements Runnable{
    LinkedList<String> queue;
    private int id;
    private int count;
    private Object update;
    static int consumed;
    
    public Consumer(LinkedList<String> q, int number, Object update){
        this.queue = q;
        this.id = number;
        this.update = update;
    }
    
    
    public void run(){
        Random random = new Random();
        
        while(true){

            try{
                
                //Wait before consuming more
                int sleepTime = random.nextInt(10); //[0,10)
                Thread.sleep(sleepTime);
                
                synchronized(update){
                    
                    //If producer is done and the queue is empty
                    if((Producer.finished) && (queue.size()==0)){
                        update.notifyAll();
                        break;
                    }
                    
                    //Consume queue entry
                    String poll = queue.poll();
                    
                    //If queue is not empty
                    if(poll != null){
                        count++;
                        consumed++;

                        //Prints consumption updates
                        if((count % 100) == 0){
                            System.out.println("Consumer " + id + ": " + count + " events consumed");
                        }
                        
                    }else{
                        //If queue was empty
                        update.notify();
                    }
                }

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