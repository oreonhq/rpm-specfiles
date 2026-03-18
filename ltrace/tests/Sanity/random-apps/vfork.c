#define _GNU_SOURCE
#include <unistd.h>
#include <stdio.h>

int main (void)
{
	pid_t child = vfork ();

	/* PRINTF/SLEEP violate the VFORK operations restriction.  */
	printf ("%d pid=%d\n", (int) child, (int) getpid ());
	sleep (1);
	if (!child)
	  execlp ("/bin/true", "/bin/true", NULL);
	return 0;
}
