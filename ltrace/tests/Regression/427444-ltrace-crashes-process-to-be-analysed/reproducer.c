#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>


#ifndef   NI_MAXHOST
#define   NI_MAXHOST 1025
#endif // NI_MAX_HOST

// On a DARWIN system EAI_OVERFLOW is define as EAI_MAX
#ifndef   EAI_OVERFLOW
#define   EAI_OVERFLOW EAI_MAX
#endif // EAI_OVERFLOW

int main(int argc, char *argv[])
{
// sleep before we can catch you via ltrace
        sleep(5);
        struct addrinfo * result;

        size_t hostname_len = NI_MAXHOST;
        char * hostname     = NULL;

        int error;

        if ( 0 != ( error = getaddrinfo( "www.example.com", NULL, NULL, &result ) ) )
        {
                fprintf( stderr, "error using getaddrinfo: %s\n", gai_strerror( error ) );
        }

        if ( result )
        {
                for( ; ; hostname_len *= 2 )
                {
                        hostname = ( char * ) realloc( hostname, hostname_len );

                        if ( NULL == hostname )
                        {
                                perror( "" );
                                break;  
                        }

                        error = getnameinfo( result->ai_addr, result->ai_addrlen, hostname, hostname_len, NULL, 0, 0 );

                        if ( 0 == error )
                        {
                                break;
                        }

                        if ( EAI_OVERFLOW != error )
                        {
                                fprintf( stderr, "error using getaddrinfo: %s\n", gai_strerror( error ) );
                                break;
                        }
                }

                if ( NULL != hostname )
                {
                        free( hostname );
                }

                freeaddrinfo( result );
        }

        return 0;
}

