import java.util.*;
import java.util.concurrent.*;

public class Main{
    
    public static void main(String[] args) throws InterruptedException{
        //Create Queue with Capacity for 100 Entries
        LinkedBlockingQueue<String> queue = new LinkedBlockingQueue<String>(100);
        
        //Create Producer and Multiple Consumers
        Producer producer = new Producer(queue);
        Consumer consumer1 = new Consumer(queue, 1);
        Consumer consumer2 = new Consumer(queue, 2);
        Consumer consumer3 = new Consumer(queue, 3);
        Consumer consumer4 = new Consumer(queue, 4);
        
        //Run Producer and Multiple Consumers
        ExecutorService e = Executors.newCachedThreadPool();
        e.execute(producer);
        e.execute(consumer1);
        e.execute(consumer2);
        e.execute(consumer3);
        e.execute(consumer4);
        e.shutdown();
        e.awaitTermination(30, TimeUnit.SECONDS);
        
        //Print Summary of Production and Consumption
        System.out.println("Summary:");
        System.out.println("Producer 1 produces " + producer.getCount() + " events.");
        System.out.println("Consumer 1 consumes " + consumer1.getCount() + " events.");
        System.out.println("Consumer 2 consumes " + consumer2.getCount() + " events.");
        System.out.println("Consumer 3 consumes " + consumer3.getCount() + " events.");
        System.out.println("Consumer 4 consumes " + consumer4.getCount() + " events.");
        
    }
    
}