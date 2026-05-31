%global source0_hash f04f04bc6dca946f6be9b72b235cbe884197327f61609e349ed8b39ea5ce73db

Summary: A utility which lists open files on a Linux/UNIX system
Name: lsof
Version: 4.98.0
Release: 9%{?dist}
License: lsof
URL: https://github.com/lsof-org/lsof

# lsof contains licensed code that we cannot ship.  Therefore we use
# upstream2downstream.sh script to remove the code before shipping it.
#
# The script can be found in SCM or downloaded from:
# http://pkgs.fedoraproject.org/cgit/lsof.git/tree/upstream2downstream.sh

%global lsofrh lsof-%{version}-rh
Source0: %{lsofrh}.tar.xz
Source1: upstream2downstream.sh

# BZ#1260300 - move lsof man page to section 1
Patch0: lsof-man-page-section.patch
Patch1: f42-ftbfs.patch

BuildRequires: gcc
BuildRequires: libselinux-devel
BuildRequires: libtirpc-devel
BuildRequires: groff-base
BuildRequires: make
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: git

%description
Lsof stands for LiSt Open Files, and it does just that: it lists information
about files that are open by the processes running on a UNIX system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{lsofrh} -S git

%build
%configure
%make_build DEBUG="%{build_cflags} -I/usr/include/tirpc" CFGL="%{build_ldflags} -L./lib -llsof -lselinux -ltirpc"
# rebase to 4.93 introduced change in Lsof.8 with unhandled .so inclusion
soelim -r Lsof.8 > lsof.1

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -p -m 0755 lsof ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m 0644 lsof.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/lsof.1

%files
%doc 00README 00CREDITS 00FAQ 00LSOF-L 00QUICKSTART
%{_bindir}/lsof
%{_mandir}/man*/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.98.0-9
- Import
