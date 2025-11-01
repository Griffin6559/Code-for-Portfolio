// package readability;

import java.util.Scanner;

public class readability {
    private Scanner text = new Scanner(System.in);
    private String text_check;
    private int Lnum;
    private int Lavg;
    private int i=0;
    private int words=0;
    private int a=0;
    private int y=0;
    private int start;
    private int end;
    private int length;
    private int total_length;
    private int final_length;
    private int average;


    public void calculations() {
        System.out.println("Input your text here: ");
        text_check = text.nextLine();
        Lnum =text_check.length();
        while(i< Lnum) {
            char text = text_check.charAt(i);
            if(text==' '){
                words ++;
            }
            i++;
        }
        Lavg=(words%100);

        while (a<Lavg){
            while (y<100){
                start=a;
                end=a+100;
                length= (end-start);
                total_length+=length;
                y++;
            }
            final_length+=total_length;
            System.out.println(final_length);
        }
        average=final_length/Lavg;
        System.out.println(average + " is the average");


        System.out.println((words+1)+" Words");
        a++;

    }

    public static void main(String[] args) {
        readability passage = new readability();
        passage.calculations();
     }





    }

