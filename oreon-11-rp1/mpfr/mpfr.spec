%global source0_hash b67ba0383ef7e8a8563734e2e889ef5ec3c3b898a01d00fa0a6869ad81c6ce01
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: mpfr
Version: 4.2.2
Release: 1%{?dist}
Summary: GNU MPFR, the Multiple Precision Floating-Point Reliable Library
License: LGPL-3.0-or-later
URL: https://www.mpfr.org/
Source0: https://ftp.gnu.org/gnu/mpfr/mpfr-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gmp-devel
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
This manual documents how to install and use the Multiple Precision Floating-Point Reliable Library, version 4.2.2.

%package devel
Summary: GNU MPFR, the Multiple Precision Floating-Point Reliable Library
Requires: mpfr%{?_isa} = %{version}-%{release}
Provides: pkgconfig(mpfr)

%description devel
This manual documents how to install and use the Multiple Precision Floating-Point Reliable Library, version 4.2.2.

%prep
%oreon_sha256
%autosetup -p1

%build
# stock configure fails on this compiler
export CFLAGS="-O2 -g -std=gnu17"
export CXXFLAGS="-O2 -g -std=gnu17"
export LDFLAGS="-Wl,-z,relro -Wl,-z,now -Wl,--as-needed"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-shared
make -j%{?_smp_build_ncpus}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.a
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
