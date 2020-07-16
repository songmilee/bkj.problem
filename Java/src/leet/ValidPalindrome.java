package leet;

public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        boolean result = true;

        s = s.replaceAll("[^A-Za-z0-9]+", "").toLowerCase();
        int size = s.length() - 1;
        System.out.println(s);
        if(size < 1) return result;
        for(int i = 0; i <= size/2 ; i++){
            if(s.charAt(i) != s.charAt(size - i)){
                result = false;
                break;
            }
        }

        return result;
    }

    public static void main(String[] args){
        ValidPalindrome vp = new ValidPalindrome();
        boolean result = vp.isPalindrome("0P");
        System.out.println(result);
    }
}
