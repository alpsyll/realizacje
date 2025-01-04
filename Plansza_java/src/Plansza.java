
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.*;

class Model {

    ArrayList<Integer> st = new ArrayList<Integer>();

}


class £am2 extends JFrame {

    private ImageIcon imObraz = new ImageIcon("obraz1.jpg");


    JButton dane = new JButton();

    £am2() {
        setTitle("£AMIG£ÓWKA 2");
        Container cp = getContentPane();
        cp.setLayout(new GridLayout(1, 1));

        cp.add(dane);
        dane.setIcon(imObraz);
        setVisible(true);
    }
}
class Lam1 extends JFrame {

    private ImageIcon imObraz = new ImageIcon("obraz2.jpg");

    JButton dane = new JButton();

    Lam1() {

        setTitle("£AMIG£ÓWKA 1");
        Container cp = getContentPane();
        cp.setLayout(new GridLayout(1, 1));

        cp.add(dane);
        dane.setIcon(imObraz);
        setVisible(true);
    }


}
class Instrukcja extends JFrame implements ActionListener {

    JTextArea tekst= new JTextArea(3,1);
    JButton zrozumialem = new JButton("Zrozumia³em!");
    ImageIcon buzka = new ImageIcon("35777.png"); // ³aduje obrazek buzki
    Image image = buzka.getImage(); // transform it
    Image buzka2 = image.getScaledInstance(20, 20,  java.awt.Image.SCALE_SMOOTH); // scale it the smooth way
    ImageIcon buzka3 = new ImageIcon(buzka2);

    Instrukcja() {

        setTitle("INSTRUKCJA");
        Container cp = getContentPane();
        cp.setLayout(new FlowLayout(FlowLayout.CENTER));
        cp.add(tekst);
        tekst.setBackground(new Color(190,242,164));
        tekst.setText("              W ka¿dej pustej kratce przy boku kwadratu nale¿y umieœciæ strza³kê wskazuj¹c¹ na diagram z cyframi.\n");
        tekst.append("Zwroty wszystkich strza³ek powinny byæ tak dobrane, aby ka¿da cyfra by³a wskazana przez tyle strza³ek, jaka jest wartoœæ tej cyfry");
        tekst.setFont(new Font("Comic Sans MS",Font.BOLD,15));
        setVisible(true);
        cp.add(zrozumialem);
        zrozumialem.addActionListener(this);
        zrozumialem.setIcon(buzka3);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Object z = e.getSource();
        if(z == zrozumialem) {
            Metody.stopMuzyka();
            dispose();
        }
    }
}






class X {
    JFileChooser plik1 = new JFileChooser();

    public void lamm(ArrayList lista) {                              //metoda, do ktorej wczytujemy liste i zapelnia sie ta lista zawartoscia z wybranego pliku
        if (plik1.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {    //wyswietla sie okienko zeby wybrac plik
            File file = plik1.getSelectedFile();
            try {
                Scanner sc2 = new Scanner(file);
                int[] t = new int[26];
                int i = 0;
                while (sc2.hasNextInt()) {                   //przechodze przez kazdy element pliku dopoki ma koniec

                    t[i] = sc2.nextInt();
                    lista.add(t[i]);                        // dodaje tekst do nowo utworzonej tablicy
                    i++;

                }
                sc2.close();
                System.out.println(lista);

            } catch (FileNotFoundException fileNotFoundException) {
                fileNotFoundException.printStackTrace();
            }

        }
    }
}






class Plansza extends JFrame {

    Model model = new Model();

    JButton tab[][] = new JButton[7][7];

    JButton sprawdz=new JButton("Poprawne rozwiazanie");
    JButton wczytaj=new JButton("WCZYTAJ PLIK");
    JButton help=new JButton("JAK GRAÆ?");
    JButton cofnij=new JButton("COFNIJ");
    JButton ponow =new JButton("PONÓW");
    JPanel plansza = new JPanel();
    JPanel sterowanie = new JPanel();
    JButton t = new JButton("GRA STRZA£KI");
    JButton t2 = new JButton();
    JButton tu =new JButton("Zapisz");
    JButton tu2 =new JButton("Odczytaj");



    public Plansza() {
        int i,j;
        Container cp = getContentPane();
        cp.setLayout(new GridLayout(1,2));
        cp.add(plansza); cp.add(sterowanie);
        sterowanie.setLayout(new GridLayout(9,1,10,10));
        sterowanie.add(t);
        t.setFont(t.getFont().deriveFont(30.0f));


        t.setEnabled(false);
        sterowanie.add(t2);
        t2.setText("Wybierz z pliku ³amig³ówê, któr¹ chcesz rozwi¹zaæ:");
        t2.setEnabled(false);

        t2.setFont(new Font("Comic Sans MS",Font.BOLD,20));

        sterowanie.add(wczytaj);

        sterowanie.add(sprawdz);
        sterowanie.add(cofnij);
        cofnij.addActionListener(new Cofnij());
        sterowanie.add(ponow);
        ponow.addActionListener(new Ponow());
        sprawdz.addActionListener(new Rozwiazanie());
        sterowanie.add(help);
        sterowanie.add(tu);
        sterowanie.add(tu2);
        tu.addActionListener(new Wczyt());
        tu2.addActionListener(new Wczyt2());
        help.setBackground(new Color(253,191,97));
        wczytaj.addActionListener(new Wczytaj());
        help.addActionListener(new Instr());
        plansza.setLayout(new GridLayout(7,7));



        for (i=0;i<7;i++)
            for (j=0;j<7;j++){

                if ((i == 0) || (j == 0) || (i == 6) || (j == 6)) {
                    tab[i][j]= new Pzyciski(i,j);                    //dodaje klase z przyciskami do wskazanych przeze mnie pól
                    tab[i][j].addActionListener(new Graj());   //dodaje do kazdego przycisku sluchacza z dzwiekiem
                    (tab[i][j]).setBackground(Color.gray);

                    if ((i==0)&&(j==0)||(i==0)&&(j==6)||(i==6)&&(j==0)||(i==6)&&(j==6)) {
                        (tab[i][j]).setBackground(Color.darkGray);
                        tab[i][j].setEnabled(false);
                    }
                }
                else{
                    tab[i][j]= new JButton();
                    (tab[i][j]).setBackground(Color.DARK_GRAY);
                    tab[i][j].setEnabled(false);
                }

                plansza.add(tab[i][j]);

            }


        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }



    public  int dajLiczbe(JButton tf) {

        return Integer.parseInt(tf.getText());}




    public class Pzyciski extends JButton implements ActionListener, Cloneable {

        ImageIcon L,P,G,D,UGP,UDP,UGL,UDL;
        int i,j;
        byte wartosc=0;

        public Pzyciski(int i, int j){
            this.i=i;this.j=j;
            L = new ImageIcon("lewo.png");
            P = new ImageIcon("prawo.png");
            G = new ImageIcon("gora.png");
            D = new ImageIcon("dol.png");
            UGP = new ImageIcon("ukosprawygora.png");
            UDP = new ImageIcon("ukosprawydol.png");
            UGL = new ImageIcon("ukoslewygora.png");
            UDL = new ImageIcon("ukoslewydol.png");
            this.addActionListener(this);
        }


        @Override
        public void actionPerformed(ActionEvent e) {
            wartosc++;
            wartosc%=9;

            switch(wartosc){

                case 0:                               // w zaleznosci od ilosci wcisnietych przyciskow ustawiam obrazek strzaleczki
                    setIcon(null);
                    break;


                case 1:
                    setIcon(L);
                    break;

                case 2:

                    setIcon(P);
                    break;

                case 3:
                    setIcon(G);
                    break;

                case 4:
                    setIcon(D);
                    break;

                case 5:
                    setIcon(UDL);
                    break;

                case 6:
                    setIcon(UDP);
                    break;

                case 7:
                    setIcon(UGL);

                    break;
                case 8:
                    setIcon(UGP);
                    break;

                default:
            }
            Metody.wyzeruj();
            Metody.dodaj(tab);


        }
    }




    class Graj implements ActionListener {                   //klasa która dodaje dŸwiêk do przycisku

        public void playSound(String nazwamuzyki) {
            try {
                AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(new File(nazwamuzyki).getAbsoluteFile());
                Clip clip = AudioSystem.getClip();
                clip.open(audioInputStream);
                clip.start();
            } catch (Exception ex) {

            }
        }


        public void actionPerformed(ActionEvent e) {
            playSound("beznazwy.wav");

        }
    }



    class Instr implements ActionListener {

        public void playSound2(String nazwamuzyki) {
            Metody.grajMuzyke(nazwamuzyki);
        }

        public void actionPerformed(ActionEvent e) {
            playSound2("instrukcja.wav");
            JFrame f = new Instrukcja();
            f.setSize(1020,150);
            f.setLocation(500,330);

        }
    }
    class Wczytaj implements ActionListener {
        private X plik = new X();
        int i,j;
        public void actionPerformed(ActionEvent e) {             //sluchacz ktory wczytuje wybrany plik ze wczesniejszego okienka wyboru
            try {
                t2.setText("Wybierz z pliku ³amig³ówê, któr¹ chcesz rozwi¹zaæ:");
                if (e.getSource() == wczytaj) {
                    plik.lamm(model.st);  //Wczytywanie
                }
                for (j = 1; j < 6; j++) {
                    for (i = 1; i < 6; i++) {
                        tab[i][j].setText(Integer.toString(model.st.get((j - 1) * 5 + (i - 1))));          //id¹c po tablicy, odczytuje ze wskazanej wczesniej listy odpowiednie wartosci
                        tab[i][j].setFont(t.getFont().deriveFont(30.0f));

                    }
                } t2.setText("Œwietnie! Mo¿esz zaczynaæ!");
                model.st.clear();
            }catch (Exception x){}


        }
    }




    class Ponow implements ActionListener {

        Ponow(){}
        public void actionPerformed(ActionEvent e) {
            int i, j;
            JButton[][] kon = Metody.ponow();                   //po wcisnieciu przyciska ponow wykonuje metode ponow

            for (i=0;i<7;i++)
                for (j=0;j<7;j++){

                    tab[i][j].setIcon(kon[i][j].getIcon());              //ustawiam obrazki we skazanym miejscu

                }


        }

    }

    class Rozwiazanie implements ActionListener {


        public void actionPerformed(ActionEvent e) {
            try {
                if (dajLiczbe(tab[1][1]) == 4) {
                    JFrame fi = new £am2();
                    fi.setSize(500, 600);
                    fi.setLocation(400, 130);

                } else {
                    JFrame fj = new Lam1();
                    fj.setSize(500, 600);
                    fj.setLocation(400, 130);
                }
            }catch(Exception x){}
        }
    }
    class Cofnij implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {

            try {
                int i, j;
                JButton[][] kon = Metody.cofnij();

                for (i = 0; i < 7; i++)
                    for (j = 0; j < 7; j++) {

                        tab[i][j].setIcon(kon[i][j].getIcon());

                    }
            }catch(Exception x){}

            }

    }




    class Wczyt implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            try{
                FileOutputStream pl= new FileOutputStream("plansza");
                ObjectOutputStream pl2= new ObjectOutputStream(pl);
                pl2.writeObject(Metody.copy(tab));
                pl2.writeObject(Metody.lista);
                pl2.writeObject(Metody.licz);
                pl.close();
            } catch (Exception x) {

            }

        }                                                                                          //serializacja
    }

    class Wczyt2 implements ActionListener{
  int i, j;
        @Override
        public void actionPerformed(ActionEvent e) {
            try{
                ObjectInputStream is=new ObjectInputStream(new FileInputStream("plansza"));
                JButton[][] stan= (JButton[][]) is.readObject();
                ArrayList<JButton[][]> lista2= (ArrayList<JButton[][]>) is.readObject();
                int licz2=(int) is.readObject();
                Metody.lista=lista2;         //przypiuje nowa liste starej liscie
                Metody.licz=licz2;            // przypisuje stary licznik nowemu licznikowi

                try{
                    for (i=0;i<7;i++)
                        for (j=0;j<7;j++){

                            tab[i][j].setIcon(stan[i][j].getIcon());

                        }

                }catch (Exception xx){}
            } catch (Exception x) {

            }

        }
    }


            public static void main(String[] args) {

        JFrame f = new Plansza();
        f.setSize(1200,700);
        f.setLocation(400,100);
        f.setVisible(true);

    }
}

