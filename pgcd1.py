#include <stdio.h>
int pgcd(int a, int b) {
    int r;
    while (b != 0) {
        r = a % b;
        printf("%d = %d *%d + %d\n",a,b,a/b,r);
        a = b;
        b = r;
    }
    return a;
}

int main() {
    int a, b, c, resultat;

    printf("Entrez les trois nombres: ");
    scanf("%d %d %d", &a,&b,&c);

    resultat = pgcd(pgcd(a, b), c);

    printf("\nLe PGCD de %d, %d et %d est : %d\n", a, b, c, resultat);

    if (resultat == 1)
        printf("Les trois nombres sont premiers entre eux.\n");
    else
        printf("Les trois nombres ne sont pas premiers entre eux.\n");

    return 0;
}

