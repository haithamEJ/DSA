#include<stdlib.h>
#include<stdio.h>
#include <string.h>

int main(){

    FILE *fp;

    char pass[100];
    char key[100] = "keyhash";
    char result[100];
    char origin[100];

    int passL = strlen(pass);
    int keyL = strlen(key);
    
    for(int i = 0 ; i < passL ; i++){
    result[i] = pass[i] ^ key[i % keyL];  
    }
    result[passL] = '\0';

    printf("%s \n",result);

    for(int i = 0 ; i < passL ; i++){
        origin[i] = result[i] ^ key[i % keyL];  
    }
    origin[passL] = '\0';

    printf("%s \n",origin);

    fp = fopen("D:\\zri3a.txt","r+");
    
    fseek(fp , 0 , SEEK_END);
    fprintf(fp, "%s" , result);
    
    fclose(fp);

}