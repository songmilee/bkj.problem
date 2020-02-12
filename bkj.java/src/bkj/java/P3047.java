package bkj.java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;

public class P3047 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String values[] = br.readLine().split(" ");
		String orders = br.readLine();
		
		int[] list = new int[3];
		for(int i = 0; i < 3; i++)
			list[i] = Integer.parseInt(values[i]);
		
		Arrays.sort(list);
		
		for(int i = 0; i < 3; i++) {
			Character order = orders.charAt(i);
			System.out.print(list[order-'A']+" ");
			
		}
		
		br.close();

	}

}
