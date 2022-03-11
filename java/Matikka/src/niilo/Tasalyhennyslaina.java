package niilo;

public class Tasalyhennyslaina {
    public static double lainapaaoma = 120000;
    public static double laina = 120000;
    public static double korkokanta = 0.0205;
    public static double lyhennyksia = 240;
    public static double lyhennys_euroina = lainapaaoma /lyhennyksia;

    public static void main(String[] args){
        System.out.println("Lyhennys euroina on: " + lyhennys_euroina);

        /*
        for(int i = 0; i < lyhennyksia; i++){
            System.out.println(laina);
            laina = laina - lyhennys_euroina;
            System.out.println(laina);
        }
        */
        System.out.println(korkokanta*laina);
        for(int i = 0; i < lyhennyksia; i++){
            korkokanta = korkokanta * (1 - korkokanta);
            System.out.println(korkokanta*laina);
        }
    }

}
