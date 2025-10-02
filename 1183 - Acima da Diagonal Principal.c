#include <stdio.h>
#include <math.h>

int main()
{
	double M[12][12], resultado = 0;
	int linha, coluna, cont = 0;
	char oper;
	scanf("%c", &oper);
	for(linha = 0; linha < 12; linha++){
		for(coluna = 0; coluna < 12; coluna++){
			scanf("%lf", &M[linha][coluna]);
			if (coluna > linha)
			{
				resultado = resultado + M[linha][coluna];
				cont++;
			}
		}
	}
	if(oper == 'M'){
    	resultado = resultado / cont;
    	printf("%.1lf\n", resultado);
	}else if(oper == 'S'){
    	printf("%.1lf\n", resultado);
    }
	return 0;
}