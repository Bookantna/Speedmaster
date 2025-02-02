import java.util.Comparator;

public class DescendingOrderComparator implements Comparator<Integer> {

    @Override
    public int compare(Integer a, Integer b) {
        return a-b;
    }
}
