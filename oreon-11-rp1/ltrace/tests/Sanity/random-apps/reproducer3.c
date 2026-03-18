#include <pthread.h>
#include <unistd.h>

void *start (void *arg) {
  return arg;
}

pthread_t thread1;

int main () {
  pthread_create (&thread1, NULL, start, NULL);
  sleep (1);
  return 0;
}

