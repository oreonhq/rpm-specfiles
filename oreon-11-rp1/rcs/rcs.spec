%global source0_hash 43ddfe10724a8b85e2468f6403b6000737186f01e60e0bd62fde69d842234cc5

Summary: Revision Control System (RCS) file version management tools
Name: rcs
Version: 5.10.1
Release: 14%{?dist}
License: GPL-3.0-or-later
URL: http://www.gnu.org/software/rcs/
Source: http://ftp.gnu.org/gnu/rcs/%{name}-%{version}.tar.lz
Patch0: rcs-configure-c99.patch
Patch1: rcs-fix_locks.patch

# for bundled(gnulib) see https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib)
BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: groff-base
BuildRequires: ghostscript
BuildRequires: ed
BuildRequires: texinfo
BuildRequires: lzip
Requires: diffutils

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

%check
make check XFAIL_TESTS="`tests/known-failures %{version}`"

%files
%doc ChangeLog COPYING THANKS NEWS README
%{_bindir}/*
%{_mandir}/man[15]/*
%{_infodir}/*

%changelog
%autochangelog
