#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main( int argc, char ** argv, char ** envp )
{
              if( setgid(getegid()) ) perror( "setgid" );
              if( setuid(geteuid()) ) perror( "setuid" );
              execv( "/usr/share/BackupPC/sbin/BackupPC_Admin", argv );
              perror( argv[0] );
              return errno;
}
