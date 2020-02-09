package bkj.java;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class P1149 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		RGB rgb = new RGB();
		rgb.calcPrice();
	}

}

class RGB{
	int n;
	int colorPrice[][];
	int payValue[][];
	int MIN_VALUE = 99999;
	
	public RGB() throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		colorPrice = new int[n][3];
		payValue = new int[n][3];
		
		for(int i = 0; i < n; i++) {
			String[] values = br.readLine().split(" ");
			for(int j = 0; j < 3; j++) {
				colorPrice[i][j] = Integer.parseInt(values[j]);
				payValue[i][j] = MIN_VALUE;
			}
		}
		
		br.close();
	}
	
	public void calcPrice() {
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < 3; j++) {
				if(i - 1 < 0) {
					payValue[i][j] = Math.min(payValue[i][j], colorPrice[i][j]);
				} else {
					for(int k = 0; k < 3; k++) {
						if(j != k)
							payValue[i][k] = Math.min(payValue[i][k], payValue[i-1][j] + colorPrice[i][k]);
					}
				}
			}
		}
		
		int min = MIN_VALUE;
		for(int i = 0; i < 3; i++) {
			min = Math.min(min, payValue[n-1][i]);
		}
		
		System.out.println(min);
	}
}
