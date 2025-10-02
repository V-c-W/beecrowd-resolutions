#include <stdio.h>

int digitos_dif(int N, int M){
    int cont = 0;
    int v[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    for(N; N <= M; N++){
        int i = N;
        do{
            v[i%10]++;
            if(v[i%10] > 1){
                break;
            }
            i /= 10;
        }while(i > 0);
        if(i == 0){
            cont++;
        }
        for(int c = 0; c < 10; c++){
            v[c] = 0;
        }
    }
    return cont;
}

int main()
{
    int N;
    int M;
    while(scanf("%d %d", &N, &M) != EOF){
        printf("%d\n", digitos_dif(N, M));
    }
    return 0;
}