//Debugging createArray:
        for (int i = 0; i < arrayLength; i++){
            System.out.println(array[i]);
        }


//Debugging createArrayList:
        for (int i=0; i < arrayList.size(); i++){
            int[] list = arrayList.get(i);
            for (int n=0; n<2; n++){
                System.out.println(list[n]);
            }
        }