public class SortTester {
    public boolean sorted(int[] nums){
        int len = nums.length;
        for (int i = 0; i < len-1; i++){
            if (nums[i] > nums[i+1]){
                    return false;
            }
        }
        return true;
    }
}
