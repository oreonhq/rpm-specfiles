#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <pthread.h>
#include <sys/wait.h>

#define DEFAULT_NUM 0
#define THREAD_NUM 3
#define MALLOC_LEN 1024*1024*10

void *thread_handle_a(void *t)
{
	long page_size = MALLOC_LEN;
	int j = *(int *)t;
	char *ptr;
	char *addr;

	struct stat buf;
	addr = (char *)malloc(page_size);
	if (addr != NULL) {
		sprintf(addr, "hello");
		printf("(a) malloc %d success: %s\n", j, addr);
	} else {
		printf("(a)malloc %d failed\n", j);
	}


	printf("thread (a) will exit\n");
	fflush(NULL);
	if(addr != NULL)
		free(addr);
	return NULL;
}

int main()
{
	int i = 0;
	pid_t pid;
	pthread_t tid_a;
	int ai[THREAD_NUM];
	int ret_a = -1;

#ifdef STS_SLEEP
	sleep(10);
#endif

	if ((pid = fork()) == 0) {
		for (i = 0; i < THREAD_NUM; i++) {
			ai[i] = i;
			ret_a = pthread_create(&tid_a, NULL, thread_handle_a, &ai[i]);
			printf("thread a : \n");

			if (ret_a == 0) {
				pthread_detach(tid_a);
			}
		}
	} else if (pid > 0) {
		for (i = 0; i < THREAD_NUM; i++) {
			ai[i] = i;
			ret_a = pthread_create(&tid_a, NULL, thread_handle_a, &ai[i]);
			printf("thread a : \n");

			if (ret_a == 0) {
				pthread_detach(tid_a);
			}
		}

		waitpid(pid, NULL, 0);
		fflush(NULL);
		write(1, "EXIT_FLAG\n", 10);
	} else {
		printf("fork error\n");
	}
	return 0;
}
