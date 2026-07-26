// The original realpath.c included in grafx2 has no license and the copyright
// holder was impossible to accurately determine. This replacement file uses
// only the wrapper function (which was written by the GrafX2 upstream) and
// is under the GPLv2 license (like the rest of GrafX2).
//
// Since Fedora always is Linux, we don't worry about the conditionals.

#include <stdlib.h>

// Use the stdlib function.
    char *Realpath(const char *_path, char *resolved_path)
    {
      /// POSIX 2004 states :
      /// If resolved_name is a null pointer, the behavior of realpath()
      /// is implementation-defined.
      ///
      /// but POSIX 2008 :
      /// If resolved_name is a null pointer, the generated pathname shall
      /// be stored as a null-terminated string in a buffer allocated as if
      /// by a call to malloc().
      ///
      /// So we assume all platforms now support passing NULL.
      /// If you find a platform where this is not the case,
      /// please add a new implementation with ifdef's.
      return realpath(_path, resolved_path);
    }
