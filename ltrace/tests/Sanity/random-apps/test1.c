#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	int pfd[2];
	pid_t pid = -1;
	int rc = 0;
	char buf[BUFSIZ];
        sigset_t sig_mask;

	/*
	 * Mask of SIGTRAP
	 * Initialize of the value of sig_mask
	 */
	sigemptyset(&sig_mask);

	/* Set of SIGTRAP in sig_mask */
	sigaddset(&sig_mask, SIGTRAP);

 	/* Set of SIGTRAP */
	sigprocmask(SIG_SETMASK, &sig_mask, NULL);

	rc = pipe(pfd);
	if(rc == -1){
		perror("pipe Error\n");
		exit (1);
	}
	pid = fork();
	if (pid == -1){
		perror("Fork Error\n");
		exit (1);
	} else if (pid == 0) {
		close(pfd[0]);
		close(1);
		dup(pfd[1]);
		close(pfd[1]);
		execl("./test2.sh", (char *)0);
		exit(0);
	} else {
		close(pfd[1]);
		while((read(pfd[0], buf, sizeof(buf))) > 0) {
			printf("%s", buf);
		}
		close(pfd[0]);
		wait(NULL);
		exit(0);
	}
}
