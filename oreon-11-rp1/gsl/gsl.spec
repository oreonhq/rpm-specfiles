%global source0_hash none

Summary: The GNU Scientific Library for numerical analysis
Name: gsl
Version: 2.8
Release: 3%{?dist}
URL: https://www.gnu.org/software/gsl/
VCS: git://git.savannah.gnu.org/gsl.git
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
Source0: https://ftp.gnu.org/gnu/gsl/%{name}-%{version}.tar.gz
Source1: https://ftp.gnu.org/gnu/gsl/%{name}-%{version}.tar.gz.sig
Source2: https://www.gnu.org/software/gsl/key/gsl_key.txt
Patch0: gsl-1.10-lib64.patch
# http://lists.gnu.org/archive/html/bug-gsl/2015-12/msg00012.html
Patch1: gsl-tol.patch
Patch2: gsl-test.patch

BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: pkgconfig
BuildRequires: make

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package devel
Summary: Libraries and the header files for GSL development
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The gsl-devel package contains the header files necessary for 
developing programs using the GSL (GNU Scientific Library).

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%patch -P0 -p1 -b .lib64
%patch -P1 -p1 -b .tol
%patch -P2 -p1 -b .test

%build
# disable FMA
%ifarch aarch64 ppc64 ppc64le s390 s390x x86_64 riscv64
export CFLAGS="%{optflags} -ffp-contract=off"
%endif
%configure --disable-silent-rules --disable-static
%make_build

%check
make check || ( cat */test-suite.log && exit 1 )

%install
%make_install
# remove unpackaged files from the buildroot
rm -rf %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/*.la

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/gsl-histogram
%{_bindir}/gsl-randist
%{_libdir}/libgsl.so.28*
%{_libdir}/libgslcblas.so.0*
%{_mandir}/man1/gsl-histogram.1*
%{_mandir}/man1/gsl-randist.1*

%files devel
%{_bindir}/gsl-config
%{_libdir}/libgsl.so
%{_libdir}/libgslcblas.so
%{_libdir}/pkgconfig/gsl.pc
%{_mandir}/man1/gsl-config.1*
%{_mandir}/man3/gsl.3*
%{_infodir}/gsl-ref.info*
%{_datadir}/aclocal/gsl.m4
%{_includedir}/gsl/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8-3
- Prepare for Oreon 11 (RP1)
