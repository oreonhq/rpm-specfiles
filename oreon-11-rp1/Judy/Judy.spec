%global source0_hash d2704089f85fdb6f2cd7e77be21170ced4b4375c03ef1ad4cf1075bd414a63eb
Name:		Judy
Version:	1.0.5
Release:        1%{?dist}
Summary:        General purpose dynamic array
License:	LGPL-2.0-or-later
URL:		http://sourceforge.net/projects/judy/
Source0:        http://downloads.sf.net/judy/Judy-%{version}.tar.gz
Source1:	README.Fedora
Patch0:		Judy-1.0.4-test-shared.patch
Patch1:		Judy-1.0.4-fix-Judy1-mans.patch
Patch2:		04_fix_undefined_behavior_during_aggressive_loop_optimizations.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  hardlink
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
Judy is a C library that provides a state-of-the-art core technology that
implements a sparse dynamic array. Judy arrays are declared simply with a null
pointer. A Judy array consumes memory only when it is populated, yet can grow
to take advantage of all available memory if desired. Judy's key benefits are
scalability, high performance, and memory efficiency. A Judy array is
extensible and can scale up to a very large number of elements, bounded only by
machine memory. Since Judy is designed as an unbounded array, the size of a
Judy array is not pre-allocated but grows and shrinks dynamically with the
array population.

%package devel
Summary:	Development libraries and headers for Judy
Requires:	%{name} = %{version}-%{release}
Provides:	judy-devel = %{version}-%{release}
%description devel
This package contains the development libraries and header files
for developing applications that use the Judy library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n judy-%{version}

# Make tests use shared instead of static libJudy
%patch -P 0 -p1 -b .test-shared

# The J1* man pages were incorrectly being symlinked to Judy, rather than Judy1
# This patch corrects that; submitted upstream 2008/11/27
%patch -P 1 -p1 -b .fix-Judy1-mans

# Fix some code with undefined behavior, commented on and removed by gcc
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=782841
%patch -P 2 -p1 -b .behavior

# README.Fedora
cp -p %{SOURCE1} .

%build

export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure --disable-static
make
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.{a,la}
rm -rf doc/man
rm -f doc/Makefile* doc/ext/README_deliver
[ -s doc/ext/COPYRIGHT ] || rm -f doc/ext/COPYRIGHT
[ -s doc/ext/LICENSE ] || rm -f doc/ext/LICENSE
hardlink -cv %{buildroot}%{_mandir}/man3/J*.3*
%oreon_autofiles Judy-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd test
./Checkit
cd -
%files -f %{oreon_filedir}/main.list
%files -n Judy-devel -f %{oreon_filedir}/Judy-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.5-42
- Prepare for Oreon 11 (RP1)
