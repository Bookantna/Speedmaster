import java.util.ArrayList;
import java.util.Arrays;

class Main {
    public static void main(String[] args){
        Integer[] array = new Integer[11];
        for(int i=0;i<11;i++){
            array[i] = i+1;
        }

        Arrays.sort(array, new DescendingOrderComparator());
        Display d = new Display();
        d.display(array);
    }
}

class Display {
    public void display(Integer[] array) {
        for (Integer i : array) {
            System.out.print(i + " "); // Print each element followed by a space
        }
        System.out.println(); // Move to the next line after printing all elements
    }
}
