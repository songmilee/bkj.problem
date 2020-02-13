import java.io.BufferedReader;
import java.io.InputStreamReader;

public class P2577 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Long multi = 1L;
		
		for(int i = 0; i < 3; i++) {
			int val = Integer.parseInt(br.readLine());
			multi *= val;
		}
		
		int[] cnt = new int[10];
		
		String result = multi.toString();
		for(int i = 0; i < result.length() ; i++) {
			cnt[result.charAt(i) - '0']++;
		}
		
		for(int i = 0; i < 10; i++) {
			System.out.println(cnt[i]);
		}
		
		br.close();
	}

}
