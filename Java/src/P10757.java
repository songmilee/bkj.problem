import java.io.BufferedReader;
import java.io.InputStreamReader;

public class P10757 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BigNumber bn = new BigNumber();
		bn.add();
	}

}

class BigNumber {
	String val1 = null;
	String val2 = null;
	
	public BigNumber() throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().split(" ");
		
		if(temp[0].length() > temp[1].length()) {
			val1 = temp[0];
			val2 = temp[1];
		} else {
			val1 = temp[1];
			val2 = temp[0];
		}
		
		br.close();
	}
	
	public void add() {
		StringBuilder sb = new StringBuilder();
		int val2Size = val2.length(); //길이 짧은 것
		int val1Size = val1.length(); //길이 긴 것
		
		int upValue = 0;
		
		//작은 사이즈 먼저 계산
		int j = val1Size -1;
		for(int i = val2Size -1; i >= 0; i--, j--) {
			int temp = Character.getNumericValue(val2.charAt(i)) + Character.getNumericValue(val1.charAt(j)) + upValue;
			
			if(temp >=10) {
				upValue = (int) temp / 10;
				temp = temp % 10;
			} else {
				upValue = 0;
			}
			
			sb.append(temp);
			
		}
		
		for(int i = j ; i >=0; i--) {
			int temp = upValue + Character.getNumericValue(val1.charAt(i));
			
			if(temp >= 10) {
				upValue = (int) temp / 10;
				temp = temp % 10;
			} else { upValue = 0; }
			
			sb.append(temp);
		}
		
		if(upValue != 0)
			sb.append(upValue);
		
		System.out.println(sb.reverse().toString());
	}
}
