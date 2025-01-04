import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.*;
import java.io.File;
import java.util.ArrayList;
import java.util.stream.Collectors;

public class Metody {
   static ArrayList<JButton[][]> lista = new ArrayList<JButton[][]>();
   static int licz = -1;
   static AudioInputStream audioInputStream;
   static  Clip clip;

    public static void dodaj(JButton[][] stan) {

        lista.add(copy(stan));                                                    // dodaje do listy kopie stanow listy
        licz++;
        System.out.println("Dodaje " + lista.get(lista.size()-1)[0][1].getIcon());

       for (int a = 0; a<lista.size(); a++) {
           System.out.println("zawartosc... " + lista.get(a)[0][1].getIcon());
       }

    }

    public static void wyzeruj() {
        licz = lista.size()-1;                 //ustawia odpowiedni indeks, ktory jest rowny dlugosci listy -1
    }

    public static JButton[][] cofnij() {                // zmniejsza licznik  i pobiera wczesniejszy obrazek (o jakims indeksie) ktory byl w tej kopii
        if (licz>0) {
            licz--;
            JButton[][] a = lista.get(licz);

            return a.clone();
        } else
       return lista.get(0);
    }


    public static JButton[][] ponow() {
        if (licz<lista.size()-1) {
            licz++;
            JButton[][] a = lista.get(licz);              // zwieksza licznik  i pobiera pozniejszy obrazek ( o jakims indeksie) ktory byl w tej kopii

            return a.clone();
        } else
            return lista.get(lista.size()-1);
    }

    public static JButton[][] copy(JButton[][] listprz) {                            //tworzy kopie stanu
        JButton[][] tymczasowa = new JButton[listprz.length][listprz[0].length];

        for (int i = 0; i < listprz.length; i++) {
            for (int j = 0; j < listprz[0].length; j++) {
                tymczasowa[i][j] = new JButton(listprz[i][j].getIcon());
            }
        }
        return tymczasowa;
    }

    public static void grajMuzyke (String m) {

        try {
            audioInputStream = AudioSystem.getAudioInputStream(new File(m).getAbsoluteFile());
           if ((clip != null) && (clip.isRunning())) {                   // jezeli nie jest pusty i jednoczesnie gra to wtedy zatrzymany
               clip.stop();
           }
            clip = AudioSystem.getClip();
            clip.open(audioInputStream);
            clip.start();
        } catch (Exception ex) {

        }

    }

    public static void stopMuzyka() {
        if (clip != null) if (clip.isRunning()) clip.stop();              // a tu zatrzymujemy muzyke ( tego uzywamy juz w przycisku)
    }
}