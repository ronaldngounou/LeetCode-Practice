class Solution {
    public String restoreString(String s, int[] indices) {
        char[] chars = s.toCharArray();
        char[] result = new char[s.length()];

        for (int i = 0; i < indices.length; i++){
            result[indices[i]] = chars[i];
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++)
            sb.append(result[i]);

        return sb.toString();

    }
}