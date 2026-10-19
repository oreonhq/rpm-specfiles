%global source0_hash 43ddfe10724a8b85e2468f6403b6000737186f01e60e0bd62fde69d842234cc5
Summary:        Revision Control System (RCS) file version management tools
Name: rcs
Version: 5.10.1
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: http://www.gnu.org/software/rcs/
Source0:        http://ftp.gnu.org/gnu/rcs/%{name}-%{version}.tar.lz
Patch0: rcs-configure-c99.patch
Patch1: rcs-fix_locks.patch
Provides: bundled(gnulib)
Requires: diffutils
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ed
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  groff-base
BuildRequires:  lzip
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
%description
The Revision Control System (RCS) is a system for managing multiple
versions of files.  RCS automates the storage, retrieval, logging,
identification and merging of file revisions.  RCS is useful for text
files that are revised frequently (for example, programs,
documentation, graphics, papers and form letters).

The rcs package should be installed if you need a system for managing
different versions of files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

autoreconf

%build

%configure --with-diffutils
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
install -m 755 src/rcsfreeze $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
%oreon_autofiles main

%check

make check XFAIL_TESTS="`tests/known-failures %{version}`"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
