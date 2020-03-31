import java.util.ArrayList;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileOutputStream;
import java.io.PrintWriter;


public class Main{
    
    public static void main(String[] args){
        ArrayList<Phonebook> original = readFile("phonebook_test.txt");
        ArrayList<Phonebook> output = newFile(original, "new");
        output = reverseList(output);
        ArrayList<ArrayList<Phonebook>> sortedLists = sortingTime(original);
        ArrayList<Phonebook> selectionSorted = sortedLists.get(0);
        ArrayList<Phonebook> mergeSorted = sortedLists.get(1);
        boolean selectionOrdered = checkSorting(selectionSorted);
        boolean mergeOrdered = checkSorting(mergeSorted);
    }
    
    
    public static ArrayList<Phonebook> readFile(String fileName){
        ArrayList<Phonebook> original = new ArrayList<>();
        try{
        BufferedReader br = new BufferedReader(new FileReader (fileName));
        String line = br.readLine();
        
        while(line != null){
            String number = line.substring(0,9);
            String name = line.substring(10, line.length());
            Phonebook entry = new Phonebook(name, number);
            original.add(entry);
            line = br.readLine();
        }
        
        br.close();
            
        }catch(IOException e){
            System.out.println("Error reading file");
        }
        
        return original;
    }
    
    
    public static ArrayList<Phonebook> newFile(ArrayList<Phonebook> original, String find){
        ArrayList<Phonebook> output = new ArrayList<>();
        try{
        FileOutputStream fos = new FileOutputStream("Output.txt", false);
        PrintWriter pw = new PrintWriter(fos);
        
        for(Phonebook entry: original){
            String name = entry.getName();
            if (name.contains(find)){
                output.add(entry);
                pw.println(entry.getNumber() + " " + name);
            }
        }
        
        pw.close();
        }catch(IOException e){
            System.out.println("Error writing file");
        }
        
        return output;
    }
    
    
    public static ArrayList<Phonebook> reverseList(ArrayList<Phonebook> list){
        if(list.size() <= 1){
            return list;
        }
        
        ArrayList<Phonebook> reversedList = new ArrayList<>();
        int lastEntry = list.size() - 1;
        reversedList.add(list.get(lastEntry));
        ArrayList<Phonebook> newList = new ArrayList<Phonebook>(list.subList(0, lastEntry));
        reversedList.addAll(reverseList(newList));
        
        return reversedList;
    }
    
    
    public static ArrayList<Phonebook> selectionSort(ArrayList<Phonebook> original){
        ArrayList<Phonebook> sorted = new ArrayList<Phonebook>(original);
        int size = original.size();
        
        ArrayList<String> names = new ArrayList<>();
        for(int entry=0; entry < size; entry++){
            names.add(original.get(entry).getLastName());
        }
        
        for(int entry=0; entry < size; entry++){
            int minimum = entry;
            for(int remaining=(entry + 1); remaining < size; remaining++){
                String name1 = names.get(minimum);
                String name2 = names.get(remaining);
                int comparison = name1.compareTo(name2);
                if(comparison > 0){
                    minimum = remaining;
                }
                
            }
            if(entry != minimum){
                sorted = swap(sorted, entry, minimum);
                names = swapNames(names, entry, minimum);
            }
        }
        return sorted;
    }
    
    
    public static ArrayList<Phonebook> swap(ArrayList<Phonebook> list, int i, int j){
        Phonebook temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
        return list;
    }
    
    
    public static ArrayList<String> swapNames(ArrayList<String> list, int i, int j){
        String temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
        return list;
    }
    
    
    public static ArrayList<Phonebook> mergeSort(ArrayList<Phonebook> list){
        int size = list.size();
        if(size <= 1){
            return list;
        }
        else{
            int splitSize = size / 2;
            ArrayList<Phonebook> left = new ArrayList<Phonebook>(list.subList(0, splitSize));
            ArrayList<Phonebook> right = new ArrayList<Phonebook>(list.subList(splitSize, size));
            return mergeSortCombine(mergeSort(left), mergeSort(right));
        }
    }
    
    
    public static ArrayList<Phonebook> mergeSortCombine(ArrayList<Phonebook> left, ArrayList<Phonebook> right){
        ArrayList<Phonebook> sorted = new ArrayList<Phonebook>();
        int indexLeft = 0;
        int indexRight = 0;
        while( (left.size() > indexLeft) && (right.size() > indexRight)){
            Phonebook left1 = left.get(indexLeft);
            Phonebook right2 = right.get(indexRight);
            String name1 = left1.getLastName();
            String name2 = right2.getLastName();
            
            if(name1.compareTo(name2) < 0){
                sorted.add(left1);
                indexLeft++;
                
            }
            else if(name1.compareTo(name2) > 0){
                sorted.add(right2);
                indexRight++;
            }
            else{
                sorted.add(left1);
                sorted.add(right2);
                indexLeft++;
                indexRight++;
            }
            
        }
        if(left.size() > indexLeft){
            sorted.addAll(left.subList(indexLeft, left.size()));
        }
        if(right.size() > indexRight){
            sorted.addAll(right.subList(indexRight, right.size()));
        }
         
        return sorted;
    }
    
    
    public static boolean checkSorting(ArrayList<Phonebook> list){
        for(int entry=0; entry < (list.size()-1); entry++){
            String name1 = list.get(entry).getLastName();
            String name2 = list.get(entry+1).getLastName();
            int comparison = name1.compareTo(name2);
            if(comparison > 0){
                return false;
            }
            
        }
        
        return true;
    }  
    
    
    public static ArrayList<ArrayList<Phonebook>> sortingTime(ArrayList<Phonebook> list){
        long startTime2 = System.nanoTime();
        ArrayList<Phonebook> mSorted = mergeSort(list);
        long endTime2 = System.nanoTime();
        double mergeTime = (endTime2 - startTime2) / 1000000000.0;
        System.out.println("Merge Sort: " + mergeTime);
        
        long startTime1 = System.nanoTime();
        ArrayList<Phonebook> sSorted = selectionSort(list);
        long endTime1 = System.nanoTime();
        double selectionTime = (endTime1 - startTime1) / 1000000000.0;
        System.out.println("Selection Sort: " + selectionTime);
        
        ArrayList<ArrayList<Phonebook>> sortedLists = new ArrayList<>();
        sortedLists.add(sSorted);
        sortedLists.add(mSorted);
        
        return sortedLists;
    }
    
}
