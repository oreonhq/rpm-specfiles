#ifndef TINYCTHREAD_THREAD_H
#define TINYCTHREAD_THREAD_H

#include <threads.h>

/* Threads */
#define tct_thrd_t thrd_t
#define tct_thrd_create thrd_create
#define tct_thrd_equal thrd_equal
#define tct_thrd_current thrd_current
#define tct_thrd_sleep thrd_sleep
#define tct_thrd_yield thrd_yield
#define tct_thrd_exit thrd_exit
#define tct_thrd_detach thrd_detach
#define tct_thrd_join thrd_join
#define tct_thrd_success thrd_success
#define tct_thrd_timedout thrd_timedout
#define tct_thrd_busy thrd_busy
#define tct_thrd_nomem thrd_nomem
#define tct_thrd_error thrd_error
#define tct_thrd_start_t thrd_start_t

/* Mutual exclusion */
#define tct_mtx_t mtx_t
#define tct_mtx_init mtx_init
#define tct_mtx_lock mtx_lock
#define tct_mtx_timedlock mtx_timedlock
#define tct_mtx_trylock mtx_trylock
#define tct_mtx_unlock mtx_unlock
#define tct_mtx_destroy mtx_destroy
#define tct_mtx_plain mtx_plain
#define tct_mtx_recursive mtx_recursive
#define tct_mtx_timed mtx_timed

/* Call once */
#define tct_call_once call_once

/* Condition variables */
#define tct_cnd_t cnd_t
#define tct_cnd_init cnd_init
#define tct_cnd_signal cnd_signal
#define tct_cnd_broadcast cnd_broadcast
#define tct_cnd_wait cnd_wait
#define tct_cnd_timedwait cnd_timedwait
#define tct_cnd_destroy cnd_destroy

/* Thread-local storage */
#define tct_thread_local thread_local
#define tct_tss_t tss_t
#define TCT_TSS_DTOR_ITERATIONS TSS_DTOR_ITERATIONS
#define tct_tss_dtor_t tss_dtor_t
#define tct_tss_create tss_create
#define tct_tss_get tss_get
#define tct_tss_set tss_set
#define tct_tss_delete tss_delete

#endif /* TINYCTHREAD_THREAD_H */
