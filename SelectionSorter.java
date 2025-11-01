public class SelectionSorter extends Sorter {

    public long sort(int[] nums){
        long start = System.nanoTime();
        int len = nums.length;
        boolean madeit = false;


            while (!madeit){
            int changes = 0;
            int priorIndex=0;
            int order=0;
            int smallest = nums[1];

            for (int current=0; current<len;current++){
                 changes++;
                 if (smallest > nums[priorIndex]){
                    smallest=nums[priorIndex];
                    priorIndex++;
                    }
                    if (smallest<nums[priorIndex]){
                        int temp = nums[order];
                        nums[order]=smallest;
                        smallest=temp;
                        order++;
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
