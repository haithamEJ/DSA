#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

bool guess(){

    int i = 0;
    int input ;
    srand(time(NULL));
    int guessed = rand()%21;

    while (i != 5 )
    {
        printf("TRY TO GUESS THE NUMBER: \n");
        scanf("%d",&input);
       
        if(input == guessed){
            return true;

        }else{
            if(input > guessed){
                printf("TOO HIGH \n");
            }else if(input < guessed){
                printf("TOO LOW \n");
            }
            i ++;
        }

        if(i == 4){
            printf("ONE GUESS LEFT LOL");
        }

    }

    return false;
    
  
}

int main(){

    printf("WELCOME TO THE GAME");

    
    if(guess()){
        printf("gg");
    }else{
        printf("good luck next time");
    };

    return 0;
}