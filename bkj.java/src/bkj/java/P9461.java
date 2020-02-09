package bkj.java;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class P9461 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());
		
		while(testCase > 0) {
			int n = Integer.parseInt(br.readLine());
			Wave w = new Wave(n);
			w.calcPn();
			System.out.println(w.getResult());
			testCase--;
		}
		
		br.close();
	}
}

class Wave{
	int n;
	long pn[];
	
	public Wave(int n) {
		this.n = n;
		pn = new long[n + 1];
	}
	
	public void calcPn() {
		pn[1] = 1;
		if(n >= 2)
			pn[2] = 1;
		if(n >= 3)
			pn[3] = 1;
		if(n >= 4)
			pn[4] = 2;
		if(n >= 5)
			pn[5] = 2;
		if(n >= 6)
			pn[6] = 3;
		
		for(int i = 7; i <= n; i++) {
			pn[i] = pn[i - 3] + pn[i - 2];
		}
	}
	
	public long getResult() {
		return pn[n];
	}
}