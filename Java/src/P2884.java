import java.io.BufferedReader;
import java.io.InputStreamReader;

public class P2884 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String time[] = br.readLine().split(" ");
		int H = Integer.parseInt(time[0]);
		int M = Integer.parseInt(time[1]);
		
		if(M < 45) {
			if(H == 0) H = 23;
			else H-= 1;
			
			M += 15;
		} else {
			M -= 45;
		}
		
		System.out.println(H+" "+M);
		
		br.close();
	}

}
