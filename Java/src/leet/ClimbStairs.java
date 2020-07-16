package leet;

public class ClimbStairs {

    public int climbStairs(int n) {
        int[]target = new int[n + 1];

        if(n < 3) return n;

        target[1] = 1;
        target[2] = 2;

        for(int i = 3; i <= n; i++){
            target[i] = target[i-1] + target[i - 2];
        }

        return target[n];
    }

    public static void main(String[] args){
        ClimbStairs cs = new ClimbStairs();
        System.out.println(cs.climbStairs(1));
    }
}
