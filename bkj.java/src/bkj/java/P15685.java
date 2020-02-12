package bkj.java;
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
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

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
			{1, 0}, // 0
			{0, -1}, // 1
			{-1, 0}, // 2
			{0, 1}, // 3
	};
	private boolean board[][] = new boolean[101][101];
		
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
				
		List<Integer> roDir = new ArrayList<Integer>();
		roDir.add(direction);
		for(int i = 0; i < generation; i++) {
			for(int j = roDir.size() - 1; j >= 0; j--) {
				roDir.add((roDir.get(j) + 1) % 4);
			}
		}

		int x = p.x;
		int y = p.y;
		visitPoint(x, y);
		for(int i = 1; i <= pointSize; i++) {
			x += dir[roDir.get(i - 1)][0];
			y += dir[roDir.get(i - 1)][1];
			visitPoint(x, y);
				
		}
		
	}
	
	public void visitPoint(int x, int y) {
		if(x > 100 || y > 100 || x < 0 || y < 0) return;
		
		board[x][y]= true; 	
//		System.out.println(x+" "+y);
	}
	
	public void cntSquare() {
		
		for(int i = 0; i <= 100; i++) {
			for(int j = 0; j <= 100; j++) {
				if(i -1 >=0 && i -1 <= 100 && j-1 >= 0 && j <= 100)
					if(board[i][j] && board[i - 1][j] && board[i][j -1] && board[i-1][j-1])
						cnt++;
			}
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