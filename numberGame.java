// package numberGame;

import java.util.Scanner;

public class numberGame {
    private int computerChoice;
    private Scanner playerChoice = new Scanner(System.in);
    private int playersMove;

    public void number() {
        System.out.println("Guess a number from 1 to 100");
        playersMove =playerChoice.nextInt();
    }
    public void highLow() {
        if (computerChoice>playersMove) {
            System.out.println("The number is higher");
        }
        if (computerChoice<playersMove) {
            System.out.println("The number is lower");
        }
    }
    public boolean checkWin(){
        if (playersMove==computerChoice) {
            return true;

        }
        else {
            return false;
        }

    }

    public void run(){
        playersMove=0;
        computerChoice=(int)((Math.random()*100)+1);
        while (playersMove != computerChoice) {
            number();
            highLow();
            checkWin();
            if (checkWin()) {
                System.out.println("You are correct!");
            }

         }
    }


    public static void main(String[] args) {
        numberGame game = new numberGame();
        game.run();

    }


}
