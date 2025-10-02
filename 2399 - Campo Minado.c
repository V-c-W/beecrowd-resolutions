#include <stdio.h>
 
int main()
{
    int i;
    int numCel;
    char tabuleiro[] = {0, 0, 0};
    scanf("%d", &numCel);
    for(i = 0; i < numCel + 1; i++){
        if(i < numCel){
            scanf("%hhd", &tabuleiro[i % 3]);
        }
        else{
            tabuleiro[i % 3] = 0;
        }
        if(i > 0){
            printf("%d\n", tabuleiro[0] + tabuleiro[1] + tabuleiro[2]);
        }
    }
    return 0;
}