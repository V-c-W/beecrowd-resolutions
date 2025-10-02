#include <stdio.h>

int crescimento(int PA, int PB, float GA, float GB) {
	int anos;
	while(PA <= PB) {
		PA = ((float)GA / 100) * PA + PA;
		PB = ((float)GB / 100) * PB + PB;
		anos++;
		if(anos > 100) {
			break;
		}
	}
	return anos;
}

int main() {
	int T;
	int PA;
	int PB;
	float GA;
	float GB;
	scanf("%d", &T);
	for(int i; i < T; i++) {
		scanf("%d%d%f%f", &PA, &PB, &GA, &GB);
		int R = crescimento(PA, PB, GA, GB);
		if(R <= 100) {
			printf("%d anos.\n", R);
		}
		else {
			printf("Mais de 1 seculo.\n");
		}
	}
	return 0;
}