/* Generate reasonable per-user default settings for kcmemail... *
 * Copyright (c) 2001 Red Hat, Inc.                              *
 * Programmed by Bernhard Rosenkraenzer <bero@redhat.com>        *
 * Copyright (c) 2021 Kevin Kofler <kevin.kofler@chello.at>      *
 * Released under the terms of the GNU GPL v2 or later.          *
 */
#include <pwd.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
	const char *name;
	const char *path;
	const char *param;
	bool text;
} mailer;
static mailer mailers[]={
	{ "kmail", "/usr/bin/kmail", NULL, false },
	{ "/usr/bin/balsa", "/usr/bin/balsa", NULL, false },
	{ "/usr/bin/mozilla", "/usr/bin/mozilla", "-mail", false },
	{ "/usr/bin/exmh", "/usr/bin/exmh", NULL, false },
	{ "/usr/bin/netscape", "/usr/bin/netscape", "-mail", false },
	{ "/usr/bin/pine", "/usr/bin/pine", NULL, true },
	{ "/usr/bin/mutt", "/usr/bin/mutt", NULL, true },
	{ "/bin/mail", "/bin/mail", NULL, true },
	{ NULL, NULL, NULL, false }
};

int main(int argc, char **argv)
{
	FILE *f=stdout;
	char *client;
	int mailer;
	struct passwd *p;
	char *emailAddress=0, *fullName=0, *mailSpool=0;
	p=getpwuid(getuid());
	for(mailer=0; mailers[mailer].path!=NULL; mailer++) {
		if(!access(mailers[mailer].path, X_OK))
			break;
	}
	if(mailers[mailer].param) {
		client=(char*)malloc(strlen(mailers[mailer].param)+strlen(mailers[mailer].name)+2);
		sprintf(client, "%s %s", mailers[mailer].name, mailers[mailer].param);
	} else
		client=strdup(mailers[mailer].name);
	if(p) {
		/* Look at the passwd file and take a good guess at the *
		 * email address...                                     *
		 * username@domainname.tld is usually a good choice.    */
		char hostname[1024];
		gethostname(hostname, 1024);
		if(strchr(hostname, '.') && strchr(hostname, '.') != strrchr(hostname, '.'))
			strcpy(hostname, strchr(hostname, '.')+1);
		emailAddress=(char*)malloc(strlen(p->pw_name)+strlen(hostname)+2);
		sprintf(emailAddress, "%s@%s", p->pw_name, hostname);
		fullName=p->pw_gecos;
		if(!fullName)
			fullName=p->pw_name;
		mailSpool=(char*)malloc(strlen(p->pw_name)+11);
		sprintf(mailSpool, "/var/mail/%s", p->pw_name);
	}
	fprintf(f,
		"[Defaults]\n"
		"Profile=Default\n"
		"[PROFILE_Default]\n"
		"EmailAddress=%s\n"
		"EmailClient=%s\n"
		"FullName=%s\n"
		"IncomingServer=%s\n"
		"IncomingServerType=localbox\n"
		"OutgoingCommand=/usr/sbin/sendmail\n"
		"OutgoingServerType=local\n"
		"TerminalClient=%s\n",
		emailAddress ? emailAddress : "",
		client ? client : "",
		fullName ? fullName : "",
		mailSpool ? mailSpool : "" ,
		mailers[mailer].text ? "true" : "false");
	fclose(f);
	free(client);
	if(emailAddress)
		free(emailAddress);
	if(mailSpool)
		free(mailSpool);
}
