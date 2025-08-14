#include <stdio.h>

int bs(int tab[100],int target){
    int d = 0;
    int f = 16;

    while (d <= f){
        int mid = (d+f)/2;

        if (tab[mid] == target){
            return mid;
        }
        if (tab[mid] > target){
            f = mid - 1;
            
        }else{
            d = mid+1;
        }
        
    }
  return -1;
    
}
int main() {
    
int table[17] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
    
    printf("%d",bs(table,90));
    return 0;
}