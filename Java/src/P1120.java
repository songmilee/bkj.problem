
import java.io.BufferedReader;
import java.io.InputStreamReader;
/**
 adaabc aababbc
 * */

public class P1120 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String values[] = br.readLine().split(" ");
		br.close();
		
		int min = 999999;
		int aSize = values[0].length();
		int bSize = values[1].length();
		for(int i = 0; i <= bSize - aSize; i++) {
			int cnt = 0;
			for(int j = 0; j < aSize; j++) {
				char aValue = values[0].charAt(j);
				char bValue = values[1].charAt(i + j);
				if(aValue != bValue) {
					cnt++;
				}
			}
			
			min = Math.min(min, cnt);
		}
		
		System.out.println(min);				
	}

}

