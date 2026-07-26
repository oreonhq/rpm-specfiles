%global source0_hash b5fe7c71c2da1ed9bcdc5784a12c5fa9fb417577513fe8a38de5de0007f7aaa1

Name:		xblas
Version:	1.0.248
Release:	34%{?dist}
Summary:	Extra Precise Basic Linear Algebra Subroutines
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.netlib.org/xblas
Source0:	http://www.netlib.org/%{name}/%{name}-%{version}.tar.gz
Patch0:		xblas-1.0.247-shared.patch
BuildRequires: make
BuildRequires:	gcc-gfortran, autoconf, m4, indent

%description
The XBLAS library of routines is part of a reference implementation for 
the Dense and Banded Basic Linear Algebra Subroutines, along with their 
Extended and Mixed Precision versions, as documented in Chapters 2 and 4 
of the new BLAS Standard.

%package devel
Summary:	Development files for xblas
Requires:	%{name} = %{version}-%{release}

%description devel
Headers and libraries for developing code that uses xblas.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .shared
autoconf

%build
%configure
make makefiles
# smp_mflags doesn't work
make lib

%install
mkdir -p %{buildroot}%{_libdir}
install -m0755 libxblas.so.1.0.0 %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -s libxblas.so.1.0.0 libxblas.so.1
ln -s libxblas.so.1.0.0 libxblas.so
popd
mkdir -p %{buildroot}%{_includedir}
install -m0644 src/*.h %{buildroot}%{_includedir}

%check
make tests

%ldconfig_scriptlets

%files
%doc LICENSE doc/report.ps
%{_libdir}/*.so.*

%files devel
%doc README
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
%autochangelog
