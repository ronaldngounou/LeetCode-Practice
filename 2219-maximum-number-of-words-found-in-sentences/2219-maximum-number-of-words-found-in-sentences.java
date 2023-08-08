class Solution {
    public int mostWordsFound(String[] sentences) {
        
        int max = Integer.MIN_VALUE;
        for (String sentence : sentences){
            String[] words = sentence.split(" ");
            
            int count = 0;
            for (String word : words){
                count++;
            }
            if (count > max)
                max = count;

        }

        return max;
        
    }
}