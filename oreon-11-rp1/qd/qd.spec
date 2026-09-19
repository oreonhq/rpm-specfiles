%global source0_hash ad6738e8330928308e10346ff7fd357ed17386408f8fb7a23704cd6f5d52a6c8

# Fortran module directory
%{!?_fmoddir: %global _fmoddir %{_libdir}/gfortran/modules}

Name:		qd
Version:	2.3.24
Release:	7%{?dist}
Summary:	Double-Double and Quad-Double Arithmetic
License:	BSD-3-Clause-LBNL
URL:		https://www.davidhbailey.com/dhbsoftware/
VCS:		git:%{url}.git
Source:		%{url}/%{name}-%{version}.tar.gz
# Fix LTO warnings about type mismatches
Patch:		%{name}-lto.patch
# Fix warnings about unused type specifications for intrinsic functions
Patch:		%{name}-intrinsic.patch

BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	ghostscript-tools-dvipdf
BuildRequires:	make
BuildRequires:	tex(latex)

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

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="gfortran"|CC="gfortran -Wl,--as-needed"|' \
    -e 's|CC=.g[c+][c+]|& -Wl,--as-needed|' \
    -i libtool

# Supply missing fortran tags
sed -i '/F77/s/\$(AM_V_lt)/& --tag=FC/' fortran/Makefile

%make_build

%install
%make_install

# Fix location of documentation
mv %{buildroot}%{_docdir}/qd/* .
rm -rf %{buildroot}%{_datadir}

# Move Fortran modules to %{_fmoddir}
mkdir -p %{buildroot}%{_fmoddir}/%{name}
mv %{buildroot}%{_includedir}/qd/*.mod %{buildroot}%{_fmoddir}/%{name}

# Fix pkgconfig file on 64-bit systems
if [ "%{_lib}" = "lib64" ]; then
  sed -i 's/^libdir=.*/&64/' %{buildroot}%{_libdir}/pkgconfig/qd.pc
fi

%check
LD_LIBRARY_PATH=$PWD/src/.libs:$PWD/fortran/.libs make check

%files
%doc AUTHORS NEWS README TODO
%license COPYING
%{_libdir}/libqd*.so.0{,.*}

%files devel
%doc qd.pdf
%{_bindir}/qd-config
%{_fmoddir}/qd/
%{_includedir}/qd/
%{_libdir}/libqd*.so
%{_libdir}/pkgconfig/qd.pc

%changelog
%autochangelog
