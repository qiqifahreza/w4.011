
import java.util.Scanner;

public class anjay{
    public static void main(String[] args) {
    
        Scanner OBJ = new Scanner(System.in);
        double PanjangPP;
        double LebarPP;
        double LuasPP;
        String Myname;

        System.out.println("Masukkan nama: ");
        Myname = OBJ.nextLine();
        
        
        System.out.println("masukkan angka panjangPP: ");
        PanjangPP = OBJ.nextDouble();

        System.out.println("masukkan angka lebarPP");
        LebarPP = OBJ.nextDouble();

        LuasPP = PanjangPP * LebarPP;
        System.out.println("Username: ");
        System.out.println("Luas Persegi Panjang adalah " + LuasPP);
        }
}