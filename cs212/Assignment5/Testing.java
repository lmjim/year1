import java.util.ArrayList;
import java.util.List;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileOutputStream;
import java.io.PrintWriter;

public class Testing{
    
    public static void createFile(String fileName, List<Phonebook> phonebook){
        try{
        FileOutputStream fos = new FileOutputStream(fileName, false);
        PrintWriter pw = new PrintWriter(fos);
        
        for(Phonebook entry: phonebook){
            pw.println(entry.getNumber() + " " + entry.getName());
        }
        
        pw.close();
        }catch(IOException e){
            System.out.println("Error writing file");
        }
        
    }
 
    
    /*
    public String getLastName(){
        String[] lastfirst = name.split(",");
        String lastName = lastfirst[0];
        return lastName;
    }
    
    
    
    public static void main(String[] args){
        ArrayList<Phonebook> original = readFile("phonebook_test.txt");
        ArrayList<Phonebook> output = newFile(original, "new");
        ArrayList<Phonebook> reversed = reverseList(output);
        ArrayList<ArrayList<Phonebook>> sortedLists = sortingTime(original);
        ArrayList<Phonebook> selectionSorted = sortedLists.get(0);
        ArrayList<Phonebook> mergeSorted = sortedLists.get(1);
        boolean selectionOrdered = checkSorting(selectionSorted);
        boolean mergeOrdered = checkSorting(mergeSorted);
        
        //Testing:
        Testing.createFile("ReverseTest.txt", reversed);
        Testing.createFile("SelectionSort.txt", selectionSorted);
        Testing.createFile("MergeSort.txt", mergeSorted);
        System.out.println("Selection Ordered: " + selectionOrdered);
        System.out.println("Merge Ordered: " + mergeOrdered);
    }
    */
}