%global source0_hash e7dcb24a3fab78b4c056b89a204a216b8ad741ea41af9ff7ccbc00561fff448c

#
# $Id$
#
%define debug_package %{nil}

Summary:        This program speeds up writing tapes on remote tape drives
Summary(fr):    Ce programme accélère l'écriture des bandes sur des périphériques distants

Name:           buffer
Version:        1.19
Release:        30%{?dist}
License:        GPL-1.0-or-later
Url:            http://hello-penguin.com/software/buffer
Source:         http://hello-penguin.com/software/buffer/%{name}-%{version}.tar.gz
 
Patch0:         01-debian-patches.all.gz
Patch1:         02-fedora-patch.all.gz
Patch2:         03-GPL.patch.all.gz

BuildRequires:  gcc
BuildRequires: make
%description
This is a program designed to speed up writing tapes on remote tape drives.
When this program is put "in the pipe", two processes are started.
One process reads from standard-in and the other writes to standard-out.
Both processes communicate via shared memory.

%description -l fr
Le programme buffer est conçu pour accélérer l'écriture des bandes sur des
périphériques bande distants.
Quand ce programme est utilisé dans un tuyau (pipe), deux processus sont 
démarrés.
Un processus lit depuis l'entrée standard et l'autre écrit vers la sortie 
standard.
Les deux processus communiquent au travers de mémoire partagée.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%make_build CFLAGS="%{optflags} -Dultrix"

%install
install -p -m 755 -D buffer --strip %{buildroot}/%{_bindir}/buffer
install -p -m 644 -D buffer.man %{buildroot}/%{_mandir}/man1/buffer.1

%files
%doc README 
%license COPYING
%{_bindir}/buffer
%{_mandir}/man1/buffer.1*

%changelog
%autochangelog
