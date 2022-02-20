/*
author of the idea: Tarmomymman
author of source java conversion: Nicodemus
original source code by: Tarmomymman
*/

package kalkyl;

import java.util.Scanner;
import java.lang.Math;

@SuppressWarnings("unused")
public class Kalkyl {
	
	//answer variables
	public static String nj = "nj";
	public static String k = "k";
	public static String sin ="sin";
	public static String cos = "cos";
	public static String tan = "tan";
	public static String ar = "ar";
	public static String ra = "ra";
	
	//factorial method
    static int factorial(int n)
    {
        int res = 1, i;
        for (i=2; i<=n; i++)
            res *= i;
        return res;
    }


	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Tämä on monimutkainen laskin."
				+ "\n"
				+ "Aloita valitsemalla toiminto: \n"
				+ "[nj] = neliöjuuri\n"
				+ "[k] = kertoma\n"
				+ "[sin] = sini\n"
				+ "[cos] = kosini\n"
				+ "[tan] = tangentti\n"
				+ "[ar] = asteet radiaaniksi\n"
				+ "[ra] = radiaanit asteiksi");
		String in = sc.nextLine();
		
		//if else method shitfest
		if (in.equals(nj)) {
			System.out.println("Syötä luku, jonka neliöjuuren haluat.");
			double in1 = sc.nextDouble();
			double njD = Math.sqrt(in1);
			System.out.println(njD);
		} else if (in.equals(k)) {
			System.out.println("Syötä luku, jonka kertoman haluat.");
			int in1 = sc.nextInt();
			double kD = factorial(in1);
			System.out.println(kD);
		} else if (in.equals(sin)) {
			System.out.println("Syötä luku, jonka sinin haluat.");
			double in1 = sc.nextDouble();
			double sinD = Math.sin(in1);
			System.out.println(sinD);
		} else if (in.equals(cos)) {
			System.out.println("Syötä luku, jonka kosinin haluat.");
			double in1 = sc.nextDouble();
			double cosD = Math.cos(in1);
			System.out.println(cosD);
		} else if (in.equals(tan)) {
			System.out.println("Syötä luku, jonka tangentin haluat.");
			double in1 = sc.nextDouble();
			double tanD = Math.tan(in1);
			System.out.println(tanD);
		} else if (in.equals(ar)) {
			System.out.println("Syötä asteluku, jonka haluat radiaaneiksi.");
			double in1 = sc.nextDouble();
			double ar = Math.toRadians(in1);
			System.out.println(ar);
		} else if (in.equals(ra)) {
			System.out.println("Syötä radiaanit, jotka haluat asteiksi.");
			double in1 = sc.nextDouble();
			double ra = Math.toDegrees(in1);
			System.out.println(ra);
		}
		else System.out.println("Wrong input");
		
		
		sc.close();
	}

}
