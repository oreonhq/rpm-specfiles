#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <signal.h>

#define THREAD_NUM 32

void *thread_function (void *);

int main (int argc, char *argv[])
{
        int i =0, x = 0;
        int res = 0;
        pthread_t a_thread[THREAD_NUM];
        void *thread_result;

        for (i = 0; i < THREAD_NUM; i++) {
                res = pthread_create (&a_thread[i], NULL, thread_function, (void *)0);
                if (res != 0) {
                        printf("Thread create failed\n");
                        return (10);
                }
        }
	raise(SIGABRT);
        return (0);
}

void *thread_function (void *arg)
{
	sleep(1);
	printf("Thread TEST\n");
}
