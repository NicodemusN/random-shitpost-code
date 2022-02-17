package nicodemus;
import java.lang.Math;
import java.util.Scanner;

public class Skeld {
	public static int crewmates = 8;
	public static int tasks = 5;
	
	public static void playerRole() {
		
		double role = Math.random();
		if(role > 0.5) {
			crewmate();
		} else impostor();
	}

	private static void impostor() {
		
		if(tasks <= 10) {
			System.out.println("You are the impostor!"
					+ "\n" +
					"Kill all the crewmates and fake tasks."
					+ "\n" +
					"Crewmates remaining: " + crewmates + "\n" +
					"Tasks remaining: " + tasks + "\n"
					);
			System.out.println("Press [t] to fake tasks or [k] to kill.");
			Scanner scanner1 = new Scanner(System.in);
			String cont = scanner1.nextLine();
			scanner1.close();
			
			if(cont.equals("t")) {
				tasking();
			} else if(cont.equals("k")) {
				killing();
			} else {
				System.out.println("Your input is SUS. You get thrown out to the space now.");
				System.exit(1);
			}
		} else {
			System.out.println("Your tasks became too many. You were revealed as the impostor.");
			System.exit(1);
		}
	}

	private static void killing() {
		double isSuccess = Math.random();
		if(isSuccess > 0.5) {
			crewmates = crewmates-1;
			System.out.println("Crewmates remaining; " + crewmates);
		} else {
			System.out.println("You failed. Tasks have increased. Repeat your choices.");
			tasks = tasks+1;
			impostor();
		}
	}

	private static void tasking() {
		double isSuccess = Math.random();
		if(isSuccess > 0.5) {
			tasks = tasks-1;
			System.out.println("Tasking success. Remaining task: " + tasks);
		} else {
			System.out.println("You failed. Tasks have increased. Repeat your choices.");
			tasks = tasks+1;
			impostor();
		}
	}

	private static void crewmate() {

	}

}
