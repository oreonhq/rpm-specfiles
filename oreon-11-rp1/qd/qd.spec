%global source0_hash a47b6c73f86e6421e86a883568dd08e299b20e36c11a99bdfbe50e01bde60e38
%{!?_fmoddir: %global _fmoddir %{_libdir}/gfortran/modules}
Name:		qd
Version:	2.3.24
Release:        1%{?dist}
Summary:        Double-Double and Quad-Double Arithmetic
License:	BSD-3-Clause-LBNL
URL:		https://www.davidhbailey.com/dhbsoftware/
VCS:		git:%{url}.git
Source0:        https://www.davidhbailey.com/dhbsoftware//%{name}-%{version}.tar.gz
Patch:		%{name}-lto.patch
Patch:		%{name}-intrinsic.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  make
BuildRequires:  tex(latex)
# /oreon:deps
%description
This package provides numeric types of twice the precision of IEEE double (106
mantissa bits, or approximately 32 decimal digits) and four times the
precision of IEEE double (212 mantissa bits, or approximately 64 decimal
digits).  Due to features such as operator and function overloading, these
facilities can be utilized with only minor modifications to conventional C++
and Fortran-90 programs.

In addition to the basic arithmetic operations (add, subtract, multiply,
divide, square root), common transcendental functions such as the exponential,
logarithm, trigonometric and hyperbolic functions are also included.

%package devel
Summary:	Double-Double and Quad-Double Arithmetic
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides numeric types of twice the precision of IEEE double (106
mantissa bits, or approximately 32 decimal digits) and four times the
precision of IEEE double (212 mantissa bits, or approximately 64 decimal
digits).  Due to features such as operator and function overloading, these
facilities can be utilized with only minor modifications to conventional C++
and Fortran-90 programs.

In addition to the basic arithmetic operations (add, subtract, multiply,
divide, square root), common transcendental functions such as the exponential,
logarithm, trigonometric and hyperbolic functions are also included.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Force documentation rebuild
rm -f docs/qd.pdf

%build

%ifarch s390x %{arm64} %{power64}
export CFLAGS='%{build_cflags} -ffp-contract=off'
export CXXFLAGS='%{build_cxxflags} -ffp-contract=off'
%endif
export FC=gfortran
%configure \
%ifnarch %{ix86} s390x %{arm64} %{power64}
  --enable-fma \
%endif
  --enable-shared \
  --disable-static
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="gfortran"|CC="gfortran -Wl,--as-needed"|' \
    -e 's|CC=.g[c+][c+]|& -Wl,--as-needed|' \
    -i libtool
sed -i '/F77/s/\$(AM_V_lt)/& --tag=FC/' fortran/Makefile
%make_build
%install
%make_install
mv %{buildroot}%{_docdir}/qd/* .
rm -rf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_fmoddir}/%{name}
mv %{buildroot}%{_includedir}/qd/*.mod %{buildroot}%{_fmoddir}/%{name}
if [ "%{_lib}" = "lib64" ]; then
  sed -i 's/^libdir=.*/&64/' %{buildroot}%{_libdir}/pkgconfig/qd.pc
fi
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_LIBRARY_PATH=$PWD/src/.libs:$PWD/fortran/.libs make check
%files -f %{oreon_filedir}/main.list
%files -n qd-devel -f %{oreon_filedir}/qd-devel.list

%changelog

%autochangelog
