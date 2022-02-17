//luukaksen celsius - fahrenheit convertteri mutta javalla

public class Main {
	
	static int fahr, celsius;
	static int lower;
	static int upper;
	static int step;
	
	public static void main(String[] args) {
		lower = 0; //alin mahdollinen
		upper = 300; //ylin mahdollinen
		step = 20; //askelväli
		fahr = lower;
		
		while (fahr <= upper && fahr >= lower) {
			celsius = 5 * (fahr-32) / 9;
			System.out.println(fahr + "   " + celsius);	
			fahr = fahr + step;
		}
	}
}
