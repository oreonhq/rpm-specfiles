#include <stdio.h>
#include <math.h>
#define nx	192
#define ny	94
#define dx	3
#define dy	3
/* v1.2 wesley ebisuzaki */
#define INT int
/* if the default integer is 16 bit then */
/* #define INT long int */

void main() {
	FILE *in;
	float land[nx];
	INT header;
	int i, j;
	char c;

	printf("Test creation of a binary file\n");
	printf("before running this program, enter wgrib land.grb -d 1\n");

	if ((in = fopen("dump","rb")) == NULL) {
		printf("could not find file: dump\n");
		printf("did you run wgrib land.grb -d 1?\n");
		exit(8);
	}

	if (fread((void *) &header, sizeof(INT), 1, in) != 1) {
		printf("no data?\n");
		exit(8);
	}

	if (header != nx*ny*sizeof(float)) {
		printf("wrong header size: %d\n", (int) header);
		exit(8);
	}

	for (j = 0; j < ny; j++) {
		if (fread((void *) land, sizeof(float), nx, in) != nx) {
			printf("not enough data\n");
			exit(8);
		}
		for (i = 0; i < nx; i++) {
			c = '?';
			if (floor(land[i]*10000.0+0.5) == 0) c = ' ';
			if (floor(land[i]*10000.0+0.5) == 10000.0) c = 'x';
			if (c == '?') {
				printf("bad value: %g\n",land[i]);
				exit(8);
			}
			if (i % dx == 0 && j % dy == 0) {
				putchar(c);
			}
		}
		if (j % dy == 0) putchar('\n');
	}
	printf("should see continents -- if you do, it works\n");
}
