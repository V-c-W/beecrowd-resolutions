#include <stdio.h>

int main() {
    int N, i, j, k;
    while (1) {
        scanf("%d", &N);
        if(N == 0) break;
        int M[N][N];
        for(i = 0; i < N; i++){
            for(j = 0; j < N; j++){
                M[i][j] = 1 + (i < j ? i : j);
                M[i][j] = 1 + ((N - 1 - i) < M[i][j] - 1 ? (N - 1 - i) : M[i][j] - 1);
                M[i][j] = 1 + ((N - 1 - j) < M[i][j] - 1 ? (N - 1 - j) : M[i][j] - 1);
            }
        }
        for(i = 0; i < N; i++){
            for(j = 0; j < N; j++){
                if(j != 0) printf(" ");
                printf("%3d", M[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}