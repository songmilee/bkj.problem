import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P10872 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		Factorial f = new Factorial(Integer.parseInt(br.readLine()));
		f.getResult();
		
		br.close();

	}

}

class Factorial{
	int n;
	
	public Factorial(int n) {
		this.n = n;
	}
	
	public int calcFact(int val) {
		if(val < 1) return 1;
		
		return val * calcFact(val - 1);
	}
	
	public void getResult() {
		long result = calcFact(n);
		
		System.out.println(result);
	}
}
