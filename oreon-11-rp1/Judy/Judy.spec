Name:		Judy
Version:	1.0.5
Release:	42%{?dist}
Summary:	General purpose dynamic array
License:	LGPL-2.0-or-later
URL:		http://sourceforge.net/projects/judy/
Source0:	http://downloads.sf.net/judy/Judy-%{version}.tar.gz
Source1:	README.Fedora
Patch0:		Judy-1.0.4-test-shared.patch
Patch1:		Judy-1.0.4-fix-Judy1-mans.patch
Patch2:		04_fix_undefined_behavior_during_aggressive_loop_optimizations.patch
# oreon url source checksums begin
%global source0_sha256 d2704089f85fdb6f2cd7e77be21170ced4b4375c03ef1ad4cf1075bd414a63eb
%global source0_file Judy-1.0.5.tar.gz
# oreon url source checksums end
BuildRequires:	coreutils
BuildRequires:	gawk
BuildRequires:	gcc >= 4.1
BuildRequires:	hardlink
BuildRequires:	make
BuildRequires:	sed

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
# Provide also the lower-case name to be coherent with other RPM based distributions
Provides:	judy-devel = %{version}-%{release}

%description devel
This package contains the development libraries and header files
for developing applications that use the Judy library.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Judy-1.0.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d2704089f85fdb6f2cd7e77be21170ced4b4375c03ef1ad4cf1075bd414a63eb" || { echo "oreon: Source0 SHA256 mismatch for Judy-1.0.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
#%{?_smp_mflags}
# fails to compile properly with parallel make:
# https://sourceforge.net/p/judy/bugs/22/

%install
%make_install

# get rid of static libs and libtool archives
rm -f %{buildroot}%{_libdir}/*.{a,la}

# clean out zero length and generated files from doc tree
rm -rf doc/man
rm -f doc/Makefile* doc/ext/README_deliver
[ -s doc/ext/COPYRIGHT ] || rm -f doc/ext/COPYRIGHT
[ -s doc/ext/LICENSE ] || rm -f doc/ext/LICENSE

# hardlink identical manpages together
hardlink -cv %{buildroot}%{_mandir}/man3/J*.3*

%check
cd test
./Checkit
cd -

%files
%license COPYING README.Fedora
%doc AUTHORS ChangeLog README examples/
%{_libdir}/libJudy.so.1
%{_libdir}/libJudy.so.1.*

%files devel
%doc doc
%{_includedir}/Judy.h
%{_libdir}/libJudy.so
%{_mandir}/man3/J*.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.5-42
- Prepare for Oreon 11 (RP1)
