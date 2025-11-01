public class InsertionSorter extends Sorter {

    public long sort(int[] nums){
        long start = System.nanoTime();
        int len = nums.length;

            for (int currently_sorting=1; currently_sorting<len;currently_sorting++){
                for (int spot_to_check=0;spot_to_check < currently_sorting; spot_to_check++){
                    if (nums[currently_sorting]<nums[spot_to_check]) {
                        int value=nums[currently_sorting];
                        for (int moving_position = currently_sorting-1; moving_position>=spot_to_check;moving_position--){
                            nums[moving_position+1]=nums[moving_position];
                        }

                        nums[spot_to_check]=value;
                        break;
                    }
                }
            }

        long end = System.nanoTime();
        long elapsed = end-start;
        return elapsed;
    }
}


   //             while (nums[s+1]< nums[s]){
        //                 p++;
        //             }
        //             int temp=nums[s-p];
        //             nums[s-p]=nums[s+1];
        //             while (i<p) {
        //                 nums[(s-p)+i]=temp;
        //                 temp=nums[(s-p)+i];
        //             }
        //         }
        //     }

        // // }
