#include <stdio.h>

long long threebonacci(int N){
    long long prim = 1;
    long long seg = 2;
    long long v[60];
    int i = 0;
    while(i < N){
        seg = seg + prim;
        prim = seg - prim;
        long long d = seg;
        if(seg % 3 == 0){
            v[i] = seg;
            i++;
            continue;
        }
        while(d > 0){
            if(d % 10 == 3){
                v[i] = seg;
                i++;
                d = 0;
                continue;
            }
            d /= 10;
        }
    }
    i -= 1;
    return v[i];
}

int main(){
    int N;
    long long R;
    while(scanf("%d", &N) != EOF){
        R = threebonacci(N);
        printf("%lld\n", R);
    }
    return 0;
}