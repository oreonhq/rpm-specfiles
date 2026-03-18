#include <sys/stat.h>
#include <fcntl.h>
#include <pthread.h>
#include <sys/mman.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/sem.h>
#include <unistd.h>
//#include "trigger_error.h"
#define THREAD_NUM 100
#define MALLOC_LEN 1024*1024*10
#define DEFAULT_NUM 0
#define MAXSEM 5

int fd[10000];
int fullid;
int emptyid;
int mutxid;

union semun
{
	int              val;    /* Value for SETVAL */
	struct semid_ds *buf;    /* Buffer for IPC_STAT, IPC_SET */
	unsigned short  *array;  /* Array for GETALL, SETALL */
	struct seminfo  *__buf;  /* Buffer for IPC_INFO (Linux-specific) */
};

void *thread_handle_a(void *temp);

int main(int argc, char *argv[])
{
	pthread_t tid_a;
	int i;
	int ai[THREAD_NUM];
	int ret_a = -1;
	int file_num;
	char filename[10];
	char str[20];
	struct sembuf P, V;;
	union semun arg;
	pid_t pid;

	int *array;
	int *sum;
	int *set;
	int *get;

	if (DEFAULT_NUM == 0) {
		file_num = 10;
	}

#ifdef STS_SLEEP
	sleep(10);
#endif

	for (i = 0; i < file_num; i++) {
		sprintf(filename, "%d", i);
		printf("open fd%d\n", i);
		fd[i] = open(filename, O_RDONLY);
		if (fd[i] < 0)
			continue;

		if (read(fd[i], str, sizeof(str)) < 0) {
			close(fd[i]);
			fd[i] = -1;
			continue;
		}
		printf("%s", str);
	}

	for (i = 0; i < file_num; i++) {
		if (fd[i] >= 0) {
			close(fd[i]);
		}
	}

	for (i = 0; i < file_num; i++) {
		fd[0] = open("/dev/null", O_RDONLY);
		if (fd[0] < 0) {
			perror("open /dev/null");
			continue;
		}
		close(fd[0]);
	}

	for (i = 0; i < file_num; i++) {
		fd[0] = open("/proc/meminfo", O_RDONLY);
		if (fd[0] < 0) {
			perror("open /proc/meminfo");
			continue;
		}
		if (read(fd[0], str, sizeof(str)) < 0) {
			close(fd[0]);
			continue;
		}
		printf("%s\n", str);
		close(fd[0]);
	}
	for (i = 0; i < file_num; i++) {
		fd[0] = open("/proc/self/maps", O_RDONLY);
		if (fd[0] < 0) {
			perror("open /proc/meminfo");
			continue;
		}
		if (read(fd[0], str, sizeof(str)) < 0) {
			close(fd[0]);
			continue;
		}
		printf("%s\n", str);
		close(fd[0]);
	}

	array =
	    (int *)mmap(NULL, sizeof(int) * 5, PROT_READ | PROT_WRITE,
			MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	sum =
	    (int *)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE,
			MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	get =
	    (int *)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE,
			MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	set =
	    (int *)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE,
			MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	*sum = 0;
	*get = 0;
	*set = 0;

	fullid = semget(IPC_PRIVATE, 1, IPC_CREAT | 00666);
	emptyid = semget(IPC_PRIVATE, 1, IPC_CREAT | 00666);
	mutxid = semget(IPC_PRIVATE, 1, IPC_CREAT | 00666);

	arg.val = 0;
	if (semctl(fullid, 0, SETVAL, arg) == -1)
		perror("semctl setval error");

	arg.val = MAXSEM;
	if (semctl(emptyid, 0, SETVAL, arg) == -1)
		perror("semctl setval error");

	arg.val = 1;
	if (semctl(mutxid, 0, SETVAL, arg) == -1)
		perror("setctl setval error");

	V.sem_num = 0;
	V.sem_op = 1;
	V.sem_flg = SEM_UNDO;
	P.sem_num = 0;
	P.sem_op = -1;
	P.sem_flg = SEM_UNDO;

	i = 0;
	while (i < 5) {

		semop(emptyid, &P, 1);
		semop(mutxid, &P, 1);

		array[*(set) % MAXSEM] = i + 1;
		printf("Producer %d\n", array[(*set) % MAXSEM]);
		(*set)++;
		fflush(NULL);
		semop(mutxid, &V, 1);
		semop(fullid, &V, 1);
		i++;
	}
	semctl(fullid, 0, IPC_RMID);
	semctl(emptyid, 0, IPC_RMID);
	semctl(mutxid, 0, IPC_RMID);

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
	} else {
		printf("fork error\n");
	}

	fflush(NULL);
	write(1, "BEFORE_ERROR\n", 13);
	//trigger_error();
	raise(SIGFPE);
	write(1, "EXIT_FLAG\n", 10);
	return 10;
}

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

