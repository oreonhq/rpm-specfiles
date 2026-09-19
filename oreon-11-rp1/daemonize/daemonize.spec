%global source0_hash 20c4fc9925371d1ddf1b57947f8fb93e2036eb9ccc3b43a1e3678ea8471c4c60

Name: daemonize
Version: 1.7.8
Release: 15%{?dist}
Summary: Run a command as a Unix daemon
License: BSD-3-Clause AND MIT AND FSFUL
URL: http://www.clapper.org/software/daemonize/
Source: https://github.com/bmc/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz

# Fix for getopt.c too many args errors in gcc-15
# https://github.com/bmc/daemonize/commit/eaf4746d47e171e7b8655690eb1e91fc216f2866
Patch0: 0001-fix-getopt.c-too-many-arguments-to-function-write-er.patch

BuildRequires:  gcc
BuildRequires: make
%description
daemonize runs a command as a Unix daemon. As defined in W. Richard Stevens' 
1990 book, Unix Network Programming (Addison-Wesley, 1990), a daemon is "a 
process that executes 'in the background' (i.e., without an associated 
terminal or login shell) either waiting for some event to occur, or waiting 
to perform some specified task on a periodic basis." Upon startup, a typical 
daemon program will:

- Close all open file descriptors (especially standard input, standard output 
  and standard error)
- Change its working directory to the root filesystem, to ensure that it 
  doesn’t tie up another filesystem and prevent it from being unmounted
- Reset its umask value
- Run in the background (i.e., fork)
- Disassociate from its process group (usually a shell), to insulate itself 
  from signals (such as HUP) sent to the process group
- Ignore all terminal I/O signals
- Disassociate from the control terminal (and take steps not to reacquire one)
- Handle any SIGCLD signals

Most programs that are designed to be run as daemons do that work for 
themselves. However, you’ll occasionally run across one that does not. 
When you must run a daemon program that does not properly make itself into a 
true Unix daemon, you can use daemonize to force it to run as a true daemon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-release-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" INSTALL_SBIN=%{_sbindir} install

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_sbindir}/daemonize
%{_mandir}/man1/daemonize.1.gz

%changelog
%autochangelog
