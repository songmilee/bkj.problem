package bkj.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class P10814 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());
		
		List<Info> people = new ArrayList<Info>();
		for(int i = 0; i < testCase; i++) {
			String[] values = br.readLine().split(" ");
			
			people.add(new Info(i, Integer.parseInt(values[0]), values[1]));
		}
		
		Collections.sort(people);
		
		for(Info i : people) {
			i.getInfo();
		}
		
		br.close();

	}

}

class Info implements Comparable<Info>{
	private int num;
	private int age;
	private String name;
	
	public Info(int num, int age, String name) {
		this.num = num;
		this.age = age;
		this.name = name;
	}
	
	public void getInfo() {
		System.out.println(this.age+" "+this.name);
	}

	@Override
	public int compareTo(Info o) {
		// TODO Auto-generated method stub
		if(this.age < o.age)
			return -1;
		else if(this.age > o.age)
			return 1;
		else if(this.age == o.age) {
			if(this.num < o.num)
				return -1;
			else
				return 1;
		}
		return 0;
	}
	
	
	
	
}
