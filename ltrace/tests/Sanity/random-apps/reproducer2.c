#include <stddef.h>
#include <signal.h>

static void h(int sig) {}

int main()
{
        struct sigaction sa;
        sigemptyset(&sa.sa_mask);
        sa.sa_handler = h;
        sa.sa_flags = SA_RESETHAND | SA_NODEFER;
        sigaction (SIGUSR1, &sa, NULL);
        return 0;
}

