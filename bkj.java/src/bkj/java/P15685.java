package bkj.java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;


/*
 * 
3
3 3 0 1
4 2 1 3
4 2 2 1
---
4

4
3 3 0 1
4 2 1 3
4 2 2 1
2 7 3 4
---
11

 * */
public class P15685 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Solution s = new Solution();
		s.cntSquare();
		System.out.println(s.getResult());
	}

}

class Solution{
	private int n;
	private int cnt = 0;
	private int dir[][] = {
			{1, 0},
			{0, -1},
			{-1, 0},
			{0, 1}
	};
	private List<Point> dcList = new ArrayList<Point>();
	
	public Solution() throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n; i++) {
			String values[] = br.readLine().split(" ");
			Point p = new Point(Integer.parseInt(values[0]), Integer.parseInt(values[1]));
			createPointList(p, Integer.parseInt(values[2]), Integer.parseInt(values[3]));
		}
		
		br.close();

	}
	
	public void createPointList(Point p, int direction, int generation) {
		int pointSize = (int)(Math.pow(2, generation));

		Point[] pointList = new Point[pointSize + 1];
		pointList[pointSize] = p;

		int curDir = direction;
		visitPoint(pointList[pointSize]);

		for(int i = pointSize - 1; i >=0; i--) {
			Point prevp = pointList[i + 1];
			int x = prevp.x + dir[curDir][0];
			int y = prevp.y + dir[curDir][1];
	
			pointList[i] = new Point(x, y);
			System.out.println(i+" "+x+" "+y);
			switch(curDir) {
			case 0:
				curDir = 3;
				break;
			case 1:
				curDir = 0;
				break;
			case 2:
				curDir = 3;
				break;
			case 3:
				curDir = 2;
				break;
			}
			
			visitPoint(pointList[i]);
		}
		
	}
	
	public void visitPoint(Point p) {
		if(p.x > 100 || p.y > 100 || p.x < 0 || p.y < 0) return;
		
		if(!dcList.contains(p))
			dcList.add(p);		
	}
	
	public void cntSquare() {
		int squDir[][] = {
				{-1, 0},
				{0, 1},
				{-1, 1}
		};
		

		for(int i = 0; i < dcList.size(); i++) {
			Point cur = dcList.get(i);
			System.out.println(cur.x+" "+cur.y);
			boolean isIn = true;
			for(int k = 0; k < 3; k++) {
				int x = cur.x + squDir[k][0];
				int y = cur.y + squDir[k][1];
				
				Point testPoint = new Point(x, y);
				boolean isContain = dcList.contains(testPoint);
				if(x < 0 || y < 0 || x > 100 || y > 100 || !isContain) {
					isIn = false;
					break;
				}
			}
			
			if(isIn) cnt++;
		}
		
	}
	
	public int getResult() {
		return cnt;
	}
}

class Point{
	int x, y;
	
	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	@Override
	public boolean equals(Object v) {
		boolean result = false;
		
		if(v instanceof Point) {
			Point temp = (Point)v;
			if(temp.x == this.x && temp.y == this.y)
				result = true;
		}
		return result;
		
	}
}