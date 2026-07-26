/* This file is here to prevent a file conflict on multiarch systems.  A
 * conflict will occur because <HEADER>.h has arch-specific definitions.
 *
 * DO NOT INCLUDE THE NEW FILE DIRECTLY -- ALWAYS INCLUDE THIS ONE INSTEAD.
 */

#if defined(__aarch64__)
#include "<HEADER>-aarch64.h"

#elif defined(__arm__)
#include "<HEADER>-armv7hl.h"

#elif defined(__i386__)
#include "<HEADER>-i386.h"

#elif defined(__ia64__)
#include "<HEADER>-ia64.h"

#elif defined(__powerpc64__) && defined(__LITTLE_ENDIAN__)
#include "<HEADER>-ppc64le.h"

#elif defined(__powerpc64__)
#include "<HEADER>-ppc64.h"

#elif defined(__powerpc__)
#include "<HEADER>-ppc.h"

#elif defined(__s390x__)
#include "<HEADER>-s390x.h"

#elif defined(__s390__)
#include "<HEADER>-s390.h"

#elif defined(__x86_64__)
#include "<HEADER>-x86_64.h"

#else
#error "This libast-devel package does not work your architecture?"
#endif
