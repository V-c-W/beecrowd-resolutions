#include <stdio.h>
#include <math.h>

int digitos(int N, int M){
    if (N == 0) return 1;
    double resul = M * log10(N);
    return floor(resul) + 1;
}

int main(){
    int C;
    int N;
    int M;
    while(scanf("%d", &C) != EOF){
        for(int i = 0; i < C; i++){
            scanf("%d%d", &N, &M);
            printf("%d\n", digitos(N, M));
        }
    }
    return 0;
}