public class BubbleSorter extends Sorter {
    /* BubbleSorter implements the bubble sort algorithm
     */
    public long sort(int[] nums){
        long start = System.nanoTime();
        int len = nums.length;
        boolean madeit = false;
        /* made it is set to true the first time that
        the for loop runs and no number is larger than the
        one before it
         */
        while (!madeit){
            int changes = 0;
            for (int s = 0; s < len - 1; s++){
                if (nums[s] > nums[s+1]){
                    int temp = nums[s+1];
                    nums[s+1] = nums[s];
                    nums[s] = temp;
                    changes++;
                }
            }
            if (changes == 0){
                madeit = true;
            }

        }
        long end = System.nanoTime();
        long elapsed = end-start;
        return elapsed;
    }
}
