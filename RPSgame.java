// package RPSgame;

import java.util.Scanner;

public class RPSgame {
    int playerWins = 0;
    int computerWins = 0;
    int computerTurn;
    String choiceMade;
    choices choiceM;
    choices choiceC;
    Scanner playerTurn = new Scanner(System.in);

    enum choices{
        ROCK,
        PAPER,
        SCISSORS
        }


    public void turn(){
        computerTurn=(int)((Math.random()*3)+1);
        System.out.println("Please type 1 for rock, 2 for paper, or 3 for scissors.");
        choiceMade =playerTurn.nextLine();
        if (choiceMade.equals("1")){
            choiceM=choices.ROCK;
            System.out.println("You played " + choiceM);
        }
        if (choiceMade.equals("2")){
            choiceM=choices.PAPER;
            System.out.println("You played " + choiceM);

        }
        if (choiceMade.equals("3")){
            choiceM=choices.SCISSORS;
            System.out.println("You played " + choiceM);
        }
        if (computerTurn==1){
            choiceC=choices.ROCK;
            System.out.println("Computer plays " + choiceC);
        }
        if (computerTurn==2){
            choiceC=choices.PAPER;
            System.out.println("Computer plays " + choiceC);
        }
        if (computerTurn==3){
            choiceC=choices.SCISSORS;
            System.out.println("Computer plays " + choiceC);
        }

    }

    public void checkWin(){
        choices myVar= choiceM;
        choices compVar=choiceC;


        switch(myVar) {
            case ROCK:
                switch(compVar){
                    case ROCK:
                    System.out.println("Tie");
                    break;

                    case SCISSORS:
                    System.out.println("Win");
                    playerWins +=1;
                    break;

                    case PAPER:
                    System.out.println("Lose");
                    computerWins +=1;
                    break;
                }
            break;

            case SCISSORS:
                switch(compVar){
                        case ROCK:
                        System.out.println("Lose");
                        computerWins +=1;
                        break;

                        case SCISSORS:
                        System.out.println("Tie");
                        break;

                        case PAPER:
                        System.out.println("Win");
                        playerWins +=1;
                        break;
                    }
            break;


            case PAPER:
                switch(compVar){
                        case ROCK:
                        System.out.println("Win");
                        playerWins +=1;
                        break;

                        case SCISSORS:
                        System.out.println("Lose");
                        computerWins +=1;
                        break;

                        case PAPER:
                        System.out.println("Tie");
                        break;
                    }
            break;

        }
    }

    public void run(){
        while (playerWins<10 && computerWins<10){
            turn();
            checkWin();
            System.out.println("The current score is " + playerWins + " -- " + computerWins);

            if (playerWins>=10) {
                System.out.println("The game is over. You have won!");

            }
             if (computerWins>=10) {
                System.out.println("The game is over. You have lost");

            }
        }


    }

    public static void main(String[] args) {
        RPSgame game = new RPSgame();
        game.run();

    }


}
