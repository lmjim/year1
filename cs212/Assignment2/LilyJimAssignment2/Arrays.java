import java.util.Scanner;
import java.util.ArrayList;
import java.util.Random;

class Arrays{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter Array Length:");
        int arrayLength = input.nextInt();
        while (arrayLength <= 0){
            System.out.printf("%s%n%s%n", "Length must be a positive value.", "Please re-enter Array Length:");
            arrayLength = input.nextInt();
        }
        
        System.out.println("Enter Density:");
        double density = input.nextDouble();
        while ((density < 0.0) || (density > 1.0)){
            System.out.printf("%s%n%s%n", "Density must be within range [0.0,1.0].", "Please re-enter Density:");
            density = input.nextDouble();
        } 
        
        int[] denseArray = createArray(arrayLength, density);
        ArrayList<int[]> convertedDenseArray = convertDenseArray(denseArray);
        
        ArrayList<int[]> sparseArray = createArrayList(arrayLength, density);
        int[] convertedSparseArray = convertSparseArray(sparseArray, arrayLength);
        
        arrayMax(denseArray);
        arrayListMax(sparseArray);
        
    }
    
    
    public static int[] createArray(int arrayLength, double density){
        long startTime = System.nanoTime();
        int[] array = new int[arrayLength];
        for (int counter=0; counter < arrayLength; counter++){
            Random random = new Random();
            if (random.nextDouble() <= density){
                array[counter] = random.nextInt((1000000 -1) +1);
            } else{
                array[counter] = 0;
            } 
        }
        long endTime = System.nanoTime();
        double elapsedTime = (endTime - startTime) / 1000000.0;
        System.out.printf("%s%d%s%f%n", "Create Dense: length: ", array.length, " time: ", elapsedTime);
        return array;
    }
    
    
    public static ArrayList<int[]> createArrayList(int arrayLength, double density){
        long startTime = System.nanoTime();
        ArrayList<int[]> arrayList = new ArrayList<int[]>();
        for (int counter=0; counter < arrayLength; counter++){
            Random random = new Random();
            if (random.nextDouble() <= density){
                int[] list = new int[2];
                list[0] = counter;
                list[1] = random.nextInt((1000000 -1) +1);
                arrayList.add(list);
            }
        }
        long endTime = System.nanoTime();
        double elapsedTime = (endTime - startTime) / 1000000.0;
        System.out.printf("%s%d%s%f%n", "Create Sparse: length: ", arrayList.size(), " time: ", elapsedTime);
        return arrayList; 
    }
    
    
    public static ArrayList<int[]> convertDenseArray(int[] denseArray){
        long startTime = System.nanoTime();
        ArrayList<int[]> arrayList = new ArrayList<int[]>();
        for (int counter=0; counter < denseArray.length; counter++){
            int value = denseArray[counter];
            if (value != 0){
                int[] list = new int[2];
                list[0] = counter;
                list[1] = value;
                arrayList.add(list);
            }
        }
        long endTime = System.nanoTime();
        double elapsedTime = (endTime - startTime) / 1000000.0;
        System.out.printf("%s%d%s%f%n", "Convert to Sparse: length: ", arrayList.size(), " time: ", elapsedTime);
        return arrayList;
    }
    
    
    public static int[] convertSparseArray(ArrayList<int[]> sparseArray, int arrayLength){
        long startTime = System.nanoTime();
        int[] array = new int[arrayLength];
        for (int counter=0; counter < sparseArray.size(); counter++){
            int[] list = sparseArray.get(counter);
            array[list[0]] = list[1];
        }
        long endTime = System.nanoTime();
        double elapsedTime = (endTime - startTime) / 1000000.0;
        System.out.printf("%s%d%s%f%n", "Convert to Dense: length: ", array.length, " time: ", elapsedTime);
        return array;
    }
    
    
    public static void arrayMax(int[] denseArray){
        long startTime = System.nanoTime();
        int max = 0;
        int index = 0;
        for (int counter=0; counter < denseArray.length; counter++){
            if (denseArray[counter] > max){
                max = denseArray[counter];
                index = counter;
            }
        }
        long endTime = System.nanoTime();
        double elapsedTime = (endTime - startTime) / 1000000.0;
        System.out.printf("%s%d%s%d%n", "Find Max (Dense): ", max, " at: ", index);
        System.out.println("Dense Find time: " + elapsedTime);
    }
    
    
    public static void arrayListMax(ArrayList<int[]> sparseArray){
        long startTime = System.nanoTime();
        int max = 0;
        int index = 0;
        for (int counter=0; counter < sparseArray.size(); counter++){
            if (sparseArray.get(counter)[1] > max){
                max = sparseArray.get(counter)[1];
                index = sparseArray.get(counter)[0];
            }
        }
        long endTime = System.nanoTime();
        double elapsedTime = (endTime - startTime) / 1000000.0;
        System.out.printf("%s%d%s%d%n", "Find Max (Sparse): ", max, " at: ", index);
        System.out.println("Sparse Find time: " + elapsedTime);
    }
    
    
}


/*Results for various combinations:
With a large array length and a large density, 
creating an array and finding the maximum value is faster using the dense array format. 
Converting to a dense array is also a lot quicker than converting to a sparse array in this case.

With a large array length and a small density, 
creating or converting to a sparse array is slightly faster than a dense array. 
When trying to find the maximum within an array like this, 
the sparse array is a lot quicker.

With a small array length and either a large or small density, 
creating a sparse array is quicker. 
However, converting to a dense array and finding the maximum 
in a dense array is quicker than sparse arrays.

The following are examples of these findings:

Enter Array Length:
10000000
Enter Density:
.99
Create Dense: length: 10000000 time: 1508.284878
Convert to Sparse: length: 9899753 time: 10251.091733
Create Sparse: length: 9899982 time: 16579.257245
Convert to Dense: length: 10000000 time: 2751.195097
Find Max (Dense): 999999 at: 588266
Dense Find time: 23.652976
Find Max (Sparse): 999999 at: 135640
Sparse Find time: 92.561243

Enter Array Length:
10000000
Enter Density:
.01
Create Dense: length: 10000000 time: 1302.610365
Convert to Sparse: length: 100497 time: 42.801415
Create Sparse: length: 99847 time: 1167.219546
Convert to Dense: length: 10000000 time: 46.079652
Find Max (Dense): 999992 at: 5032546
Dense Find time: 33.810903
Find Max (Sparse): 999998 at: 7272880
Sparse Find time: 15.881722

Enter Array Length:
100
Enter Density:
.99
Create Dense: length: 100 time: 1.578316
Convert to Sparse: length: 99 time: 0.254092
Create Sparse: length: 100 time: 1.052210
Convert to Dense: length: 100 time: 0.085765
Find Max (Dense): 978984 at: 51
Dense Find time: 0.0064
Find Max (Sparse): 999504 at: 19
Sparse Find time: 0.044802

Enter Array Length:
100
Enter Density:
.01
Create Dense: length: 100 time: 1.463110
Convert to Sparse: length: 2 time: 0.073603
Create Sparse: length: 0 time: 0.502425
Convert to Dense: length: 100 time: 0.002560
Find Max (Dense): 700159 at: 23
Dense Find time: 0.008961
Find Max (Sparse): 0 at: 0
Sparse Find time: 0.017921
*/
