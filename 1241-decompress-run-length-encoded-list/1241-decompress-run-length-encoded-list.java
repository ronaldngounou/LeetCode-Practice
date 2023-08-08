class Solution {
    public int[] decompressRLElist(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i += 2){
            count += nums[i];
        }

        int[] result = new int[count];
        int index = 0;
        for (int i = 0; i < nums.length; i += 2){
            int freq = nums[i];
            int val = nums[i + 1];
            for (int j = 0; j < freq; j++){
                result[index++] = val;
            }
        }

        return result;
    }
}