//converts fahrenheits and celsius

import java.util.Scanner; //this comes with default jdk, no external libraries needed

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter [c] to convert celsius to fahrenheits"
				+ "\n"
				+ "or enter [f] to convert fahrenheits to celsius.");
		String in = sc.nextLine();
		
		if (in.equals("c")) {
			System.out.println("Enter celsius: ");
			int f = sc.nextInt();
			System.out.println(f + " celsius in fahrenheits is " + ((f * 1.8) + 32));
			
		} else if (in.equals("f")) {
			System.out.println("Enter fahrenheit: ");
			int c = sc.nextInt();
			System.out.println(c + " fahrenheits in celsius is " + ((c - 32) / 1.8));
			
		} else {
			System.out.println("Wrong input, restart.");
		}
	}
}
