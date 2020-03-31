import java.util.*;
import java.util.concurrent.*;

public class Producer implements Runnable{
    LinkedList<String> queue;
    private int id;
    private int count;
    static boolean finished = false;
    static int produced = 0;
    private Object update;
    
    public Producer(LinkedList<String> q, int number, Object update){
        this.queue = q;
        this.id = number;
        this.update = update;
    }
    
    
    public void run(){
        Random random = new Random();
        
        while(true){
            
            try{
                synchronized(update){

                    //If production is not done
                    if(produced < 1000){
                        
                        //If queue is not full
                        if(queue.size() < 100){
                            
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
                        
                        //Wait before producing more
                        update.wait();
                        
                    }else{
                        //If production is done
                        break;
                    }
                }
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