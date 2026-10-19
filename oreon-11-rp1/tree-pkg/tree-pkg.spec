%global source0_hash 22cf32e84e3eb508d97a9e991c2c3cc006b9dcf4afed201d96311c5c57d08fcf
Summary:        File system tree viewer
Name: tree-pkg
Version: 2.3.2
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://oldmanprogrammer.net/source.php?dir=projects/tree
Source0:        https://github.com/Old-Man-Programmer/tree/archive/refs/tags/%{version}.tar.gz#/tree-%{version}.tar.gz
Patch1: tree-license-fsf-addr.patch
Patch2: tree-size-field-len.patch
Patch3: tree-static-analysis.patch
Patch4: tree-static-analysis-2.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
# /oreon:deps
%description
The source RPM package of tree, which has to be named differently due to
limitations of Pagure and Gitlab.

%package -n tree
Summary: File system tree viewer
%description -n tree
The tree utility recursively displays the contents of directories in a
tree-like format.  Tree is basically a UNIX port of the DOS tree
utility.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n tree-%{version} -S git

# do not escape UTF-8 chars in file names by default in UTF-8 locale (#1480778)
sed -e 's/LINUX/__linux__/' -i tree.c

%build

%make_build CFLAGS="$CFLAGS $(getconf LFS_CFLAGS)" LDFLAGS="$LDFLAGS"
%install
%make_install DESTDIR=$RPM_BUILD_ROOT%{_bindir} \
	      MANDIR=$RPM_BUILD_ROOT%{_mandir}
%oreon_autofiles tree usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n tree -f %{oreon_filedir}/tree.list

%changelog

%autochangelog
