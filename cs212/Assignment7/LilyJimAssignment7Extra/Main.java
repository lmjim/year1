import java.util.*;
import java.util.concurrent.*;

public class Main{
    
    public static void main(String[] args) throws InterruptedException {
        
        LinkedList<String> queue = new LinkedList<String>();
        Object update = new Object();
        
        //Create Multiple Producers and Multiple Consumers
        Producer producer1 = new Producer(queue, 1, update);
        Producer producer2 = new Producer(queue, 2, update);
        Producer producer3 = new Producer(queue, 3, update);
        Producer producer4 = new Producer(queue, 4, update);
        Consumer consumer1 = new Consumer(queue, 1, update);
        Consumer consumer2 = new Consumer(queue, 2, update);
        Consumer consumer3 = new Consumer(queue, 3, update);
        Consumer consumer4 = new Consumer(queue, 4, update);
        Consumer consumer5 = new Consumer(queue, 5, update);
        Consumer consumer6 = new Consumer(queue, 6, update);
        
        //Run Multiple Producers and Multiple Consumers
        ExecutorService e = Executors.newCachedThreadPool();
        e.execute(producer1);
        e.execute(producer2);
        e.execute(producer3);
        e.execute(producer4);
        e.execute(consumer1);
        e.execute(consumer2);
        e.execute(consumer3);
        e.execute(consumer4);
        e.execute(consumer5);
        e.execute(consumer6);
        e.shutdown();
        e.awaitTermination(1, TimeUnit.MINUTES);
        
        //Print Summary of Production and Consumption
        System.out.println("Summary:");
        System.out.println("Producer 1 produces " + producer1.getCount() + " events.");
        System.out.println("Producer 2 produces " + producer2.getCount() + " events.");
        System.out.println("Producer 3 produces " + producer3.getCount() + " events.");
        System.out.println("Producer 4 produces " + producer4.getCount() + " events.");
        System.out.println("Consumer 1 consumes " + consumer1.getCount() + " events.");
        System.out.println("Consumer 2 consumes " + consumer2.getCount() + " events.");
        System.out.println("Consumer 3 consumes " + consumer3.getCount() + " events.");
        System.out.println("Consumer 4 consumes " + consumer4.getCount() + " events.");
        System.out.println("Consumer 5 consumes " + consumer5.getCount() + " events.");
        System.out.println("Consumer 6 consumes " + consumer6.getCount() + " events.");
        
    }
    
    
}