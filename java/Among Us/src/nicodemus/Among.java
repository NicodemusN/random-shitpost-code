package nicodemus;

import java.util.Scanner;

public class Among {
	public static void among() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Welcome to Among Us. Press [y] to start.");
		String start = scanner.nextLine();
		
		if(start.equals("y")) {
			Skeld.playerRole();
			scanner.close();
		} else System.out.println("Invalid input.");
	}
}