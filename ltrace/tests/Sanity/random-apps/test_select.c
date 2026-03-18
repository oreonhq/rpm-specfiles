#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/types.h>

#define MAXBUF 1024
#define THREAD_NUM 100
#define MALLOC_LEN 1024*1024*10

void *thread_handle_a(void *t)
{
	long page_size = MALLOC_LEN;
	int j = *(int *)t;
	char *addr;
	addr = (char *)malloc(page_size);
	if (addr != NULL) {
		sprintf(addr, "hello");
		printf("(a) malloc %d success: %s\n", j, addr);
	} else {
		printf("(a)malloc %d failed\n", j);
	}

	printf("thread (a) will exit\n");
	fflush(NULL);
	return NULL;
}

int main(int argc, char **argv)
{
	fd_set wfds;
	struct timeval tv;
	int retval, maxfd = -1;
	pthread_t tid_a;
	int i;
	int ai[THREAD_NUM];
	int ret_a = -1;

	sleep(5);

	for (i = 0; i < THREAD_NUM; i++) {
		ai[i] = i;
		ret_a = pthread_create(&tid_a, NULL, thread_handle_a, &ai[i]);
		printf("thread a : \n");

		if (ret_a == 0) {
			pthread_detach(tid_a);
		}
	}

	FD_ZERO(&wfds);
	FD_SET(STDOUT_FILENO, &wfds);
	maxfd = STDOUT_FILENO;
	tv.tv_sec = 1;
	tv.tv_usec = 0;
	
	retval = select(maxfd+1, NULL, &wfds, NULL, &tv);
	if (retval == -1) {
		fprintf(stderr, "select failed\n");
	} else if (retval == 0){
		printf("Time out\n");
	} else {
		printf("stdout can be write\n");
	}
	
	printf("EXIT_FLAG\n");
	return 0;
}
