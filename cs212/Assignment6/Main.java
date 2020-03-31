public class Main{
    
    public static void main(String[] args){
        
        //intSet provided by project spec
        //intSet should output [1, 5, 3]
        OccurrenceSet<Integer> intSet = new OccurrenceSet<Integer>();
        intSet.add(1);
        intSet.add(3);
        intSet.add(5);
        intSet.add(5);
        intSet.add(3);
        intSet.add(3);
        intSet.add(3);
        System.out.println(intSet);
        
        //stringSet provided by project spec
        //stringSet should output [here, hello, world]
        OccurrenceSet<String> stringSet = new OccurrenceSet<String>();
        stringSet.add("hello");
        stringSet.add("hello");
        stringSet.add("world");
        stringSet.add("world");
        stringSet.add("world");
        stringSet.add("here");
        System.out.println(stringSet);
        
        //doubleSet should output [80.0, 10.8, 10.3, 5.5, 10.4]
        OccurrenceSet<Double> doubleSet = new OccurrenceSet<Double>();
        for(int i = 0; i < 6; i++){
            doubleSet.add(10.4);
        }
        for(int i = 0; i < 5; i++){
            doubleSet.add(5.5);
        }
        doubleSet.add(10.3);
        doubleSet.add(10.3);
        doubleSet.add(10.3);
        doubleSet.add(10.8);
        doubleSet.add(10.8);
        doubleSet.add(80.0);
        System.out.println(doubleSet);
        
        /*largeSet should output with 0 and the integers divisible by 10 at the end, 
        the remaining integers divisble by 5 before that, 
        the remaining even integers before that, 
        and the remaining odd integers before that (at the beginning)*/
        OccurrenceSet<Integer> largeSet = new OccurrenceSet<Integer>();
        for(int i = 0; i < 50; i++){
            largeSet.add(i);
        }
        for(int i = 0; i < 50; i += 2){
            largeSet.add(i);
        }
        for(int i = 0; i < 50; i += 5){
            largeSet.add(i);
            largeSet.add(i);
        }
        System.out.println(largeSet);

    }
    
}