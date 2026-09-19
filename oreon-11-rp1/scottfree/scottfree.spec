%global source0_hash a033a7e11c7f20e392df8aac1122c06cc10a4cad85df8c644c9bdbbdbf22d8b6

Name:    scottfree
Version: 1.14
Release: 35%{?dist}
Summary: Interpreter for Scott Adams format text adventure games

License: GPL-2.0-or-later
URL:     http://ifarchive.org/if-archive/scott-adams/interpreters/scottfree/
Source0: http://ifarchive.org/if-archive/scott-adams/interpreters/scottfree/ScottFree.tar.gz
# Man page taken from Debian
Source1: %{name}.6
# Fix Makefile
Patch0:  %{name}-1.14-Makefile.patch
# Add missing headers
# https://salsa.debian.org/games-team/scottfree/blob/master/debian/patches/02_scottcurses_includes.diff
Patch1:  %{name}-1.14-includes.patch
# Fix format strings
# https://salsa.debian.org/games-team/scottfree/blob/master/debian/patches/format-strings.patch
Patch2: %{name}-1.14-format_strings.patch
# Include time.h, fix two warnings in fscanf calls
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=968375
# https://salsa.debian.org/games-team/scottfree/blob/master/debian/patches/04_968375.patch
Patch3: %{name}-1.14-fscanf.patch
Patch4: scottfree-c99.patch
# Fix building with gcc 15
Patch5: %{name}-1.14-gcc15.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel

%description
ScottFree is an interpreter for Scott-Adams-format text adventure games
(remember those?). It reads and executes TRS-80 format data files.

Most Adventure International Games are distributed as shareware and are 
available from http://ifarchive.org/if-archive/scott-adams/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1

# Fix file permissions
chmod 644 *

%build
%set_build_flags
%make_build

%install
%make_install

# Install man page
install -d %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man6/

%files
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%doc README Definition

%changelog
%autochangelog
