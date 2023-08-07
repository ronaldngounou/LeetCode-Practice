class Solution {
    public int finalValueAfterOperations(String[] operations) {
        
        int result = 0;
        for (String operation : operations){
            int val = 0;
            if (operation.equals("++X") || operation.equals("X++")){
                val = 1;
                result = result + val; 
            }
            else if (operation.equals("--X") || operation.equals("X--")){
                val = -1;
                result = result - 1;
            }
                                
        }
        return result;
    }
}