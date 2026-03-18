#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/types.h>
#include <signal.h>

#define NTHD 60

int thd_no;


long sub_func(void)
{
	uid_t uid;

	printf("sub-thread created: %d\n", ++thd_no);

	for (;;) {
		uid = getuid();
		sleep(1);
	}

	return (long)uid;
}

void *sub_thd(void *c)
{
	sub_func();
}

int main(int argc, char *argv[])
{
	int i;
	pthread_t thd[NTHD];

	printf("test start...\n");

	for (i = 0; i < NTHD; i++) {
		pthread_create(&thd[i], NULL, sub_thd, NULL);
	}
//	pause();
        return 0;
}

