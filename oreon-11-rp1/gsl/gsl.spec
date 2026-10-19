%global source2_hash 754dbbaf2640bb8bc4fc3166918b9ba0f99ae438f5a6888e0ac8a082020eb9d6
%global source1_hash 4e48a4bb62ae9ec40185d52b3691a963c9dac6a317290eb80985cdbadcdf4476
%global source0_hash 6a99eeed15632c6354895b1dd542ed5a855c0f15d9ad1326c6fe2b2c9e423190
Summary:        The GNU Scientific Library for numerical analysis
Name: gsl
Version: 2.8
Release:        1%{?dist}
URL: https://www.gnu.org/software/gsl/
VCS: git://git.savannah.gnu.org/gsl.git
License: GPL-3.0-or-later
Source0:        https://mirrors.kernel.org/gnu/gsl/%{name}-%{version}.tar.gz
Source1:        https://mirrors.kernel.org/gnu/gsl/%{name}-%{version}.tar.gz.sig
Source2: https://www.gnu.org/software/gsl/key/gsl_key.txt
Patch0: gsl-1.10-lib64.patch
Patch1: gsl-tol.patch
Patch2: gsl-test.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%patch -P0 -p1 -b .lib64
%patch -P1 -p1 -b .tol
%patch -P2 -p1 -b .test

%build

%ifarch aarch64 ppc64 ppc64le s390 s390x x86_64 riscv64
export CFLAGS="%{optflags} -ffp-contract=off"
%endif
%configure --disable-silent-rules --disable-static
%make_build
%check

make check || ( cat */test-suite.log && exit 1 )
%install
%make_install
rm -rf %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gsl-devel -f %{oreon_filedir}/gsl-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8-3
- Prepare for Oreon 11 (RP1)
