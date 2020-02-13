
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class P14501 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Leave l = new Leave();
		l.calcMaxPrice();
	}

}

class Leave{
	int n;
	int[] t;
	int[] p;
	
	public Leave() throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		t = new int[n];
		p = new int[n];
		
		for(int i = 0; i < n; i++) {
			String[] values = br.readLine().split(" ");
			
			t[i] = Integer.parseInt(values[0]);
			p[i] = Integer.parseInt(values[1]);
		}
		
		br.close();
	}
	
	public void calcMaxPrice() {
		int dp[] = new int[n];
		int max = -1;
		
		for(int i = 0; i < n; i++) {
			if(i + t[i] - 1 < n) {
				dp[i] = Math.max(dp[i],  p[i]);
				
				for(int j = i + t[i] ; j < n; j++) {
					if(j + t[j] -1 < n)
						dp[j] = Math.max(dp[j], dp[i] + p[j]);
				}
			}
			max = Math.max(max, dp[i]);
		}
		
		System.out.println(max);
	}
}