package bkj.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P4948 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = 0;
		while(true) {
			n = Integer.parseInt(br.readLine());
			
			if(n == 0) break;
			
			FindPrime fp = new FindPrime(n);
			fp.calcPrimeCount();
			fp.getResult();
			
		}
		
		br.close();
	}

}

class FindPrime{
	private int n;
	private int numberList[];
	private int result = 0;
	
	public FindPrime(int n) {
		this.n = n;
		numberList = new int[n];
		
		int index = 0;
		for(int i = n+1; i <= 2 * n; i++) {
			numberList[index++] = i;
		}
		
	}
	
	public void calcPrimeCount() {
		for(int i = 2; i <= Math.sqrt(2*n); i++) {
			for(int j = 0; j < n; j++) {
				if(numberList[j] == -1 || numberList[j] == i) continue;
				else if(numberList[j] % i == 0) numberList[j] = -1;
			}
		}
	}
	
	public void getResult() {
		for(int i = 0; i < n; i++) {
			if(numberList[i] == -1 || numberList[i] == 1) continue;
			result++;
		}
		
		System.out.println(result);
	}
}