import java.util.*;

public class Testing{
    
    //Testing Iterator Method
    public static <T> void iterateTest(OccurrenceSet<T> set){
        Iterator<T> iterate = set.iterator();
        while(iterate.hasNext()){
            T item = iterate.next();
            System.out.println(item);
        }
    }

    //Testing All Other Methods
    public static <T> void methodsTest(){
        System.out.println();
        System.out.println("Testing the other functions: ");
        OccurrenceSet<String> testSet = new OccurrenceSet<String>();
        System.out.println("Is Empty: " + testSet.isEmpty());
        
        List<String> list = Arrays.asList("iPhone", "Android", "Nintendroid", "Windows", "Mac OS X", "Ubuntu");
        testSet.addAll(list);
        System.out.println("Add All Set: " + testSet);
        System.out.println("Is Empty: " + testSet.isEmpty());
        
        List<String> removeList = Arrays.asList("iPhone", "Android", "Windows");
        testSet.removeAll(removeList);
        System.out.println("Remove All Set: " + testSet);
        
        testSet.addAll(list);
        System.out.println("Add All Set: " + testSet);
        
        List<String> retainList = Arrays.asList("Nintendroid");
        testSet.retainAll(retainList);
        System.out.println("Retain All Set: " + testSet);
        
        testSet.addAll(list);
        testSet.remove("Ubuntu");
        testSet.remove("Mac OS X");
        System.out.println("Remove Set: " + testSet);
        
        System.out.println("Contains List 1: " + testSet.containsAll(removeList));
        System.out.println("Contains List 2: " + testSet.containsAll(list));
        System.out.println("Contains Nintendroid: " + testSet.contains("Nintendroid"));
        System.out.println("Contains Mac OS X: " + testSet.contains("Mac OS X"));
        
        System.out.println("Size: " + testSet.size());
        testSet.clear();
        System.out.println("Size after Clear: " + testSet.size());
        
        testSet.addAll(list);
        testSet.addAll(removeList);
        testSet.add("Nintendroid");
        testSet.add("Nintendroid");
        System.out.println();
        System.out.println("Current Set: ");
        System.out.println(testSet);
        
        System.out.println();
        System.out.println("Object[]: ");
        Object[] array1 = testSet.toArray();
        for (int i = 0; i < array1.length; i++){
            System.out.println(array1[i]);
        }
        
        System.out.println();
        System.out.println("T[]: ");
        String[] array2 = new String[testSet.size()];
        array2 = testSet.toArray(array2);
        for (int i = 0; i < array2.length; i++){
            System.out.println(array2[i]);
        }
        
        System.out.println();
        System.out.println("T[] That's too small: ");
        String[] array3 = new String[0];
        array3 = testSet.toArray(array3);
        for (int i = 0; i < array3.length; i++){
            System.out.println(array3[i]);
        }
        
    }
    
}

