class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = max(candies);

        List<Boolean> result = new ArrayList<Boolean>(candies.length);

        for (int i = 0; i < candies.length; i++){
            if ((candies[i] + extraCandies) >= max)
                result.add(true);
            else
                result.add(false);
        }

        return result;

    }

    private static int max(int[] array){
        int max = Integer.MIN_VALUE;
        for (int num : array){
            if (num > max)
                max = num;
        }

        return max;

    }
}