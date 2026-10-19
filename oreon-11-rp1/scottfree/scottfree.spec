%global source0_hash a033a7e11c7f20e392df8aac1122c06cc10a4cad85df8c644c9bdbbdbf22d8b6
Name:    scottfree
Version: 1.14
Release:        1%{?dist}
Summary:        Interpreter for Scott Adams format text adventure games
License: GPL-2.0-or-later
URL:     http://ifarchive.org/if-archive/scott-adams/interpreters/scottfree/
Source0:        http://ifarchive.org/if-archive/scott-adams/interpreters/scottfree/ScottFree.tar.gz
Source1: %{name}.6
Patch0:  %{name}-1.14-Makefile.patch
Patch1:  %{name}-1.14-includes.patch
Patch2: %{name}-1.14-format_strings.patch
Patch3: %{name}-1.14-fscanf.patch
Patch4: scottfree-c99.patch
Patch5: %{name}-1.14-gcc15.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
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
install -d %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man6/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
