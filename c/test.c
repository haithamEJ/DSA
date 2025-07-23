#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* crypter(char* input){

  char* key = "keyhash";
  int passL = strlen(input);
  int keyL = strlen(key);
  char* result = (char*)malloc(passL + 1);
  char* origin = (char*)malloc(passL + 1);
 

  for(int i = 0 ; i < passL ; i++){
  
    result[i] = input[i] ^ key[i % keyL];  

  }
  result[passL] = '\0';

  return result;

}

char * decrypter(char* hashed){

  char* key = "keyhash";
  int passL = strlen(hashed);
  int keyL = strlen(key);
  char* origin = (char*)malloc(passL + 1);
  for(int i = 0 ; i < passL ; i++){
    origin[i] = hashed[i] ^ key[i % keyL];  
  }

  origin[passL] = '\0';
  return origin;


}
int main(){
    char inputt[100];

    printf("Enter input : \n");
    scanf("%s",inputt);
    
    char* test = crypter(inputt);

    printf("%s \n",test);

    char* fixed = decrypter(test);

    printf("%s",fixed);

    free(test);
    free(fixed);

    return 0 ;
}