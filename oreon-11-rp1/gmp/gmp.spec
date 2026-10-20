%global source0_hash a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gmp
Version: 6.3.0
Release: 1%{?dist}
Summary: GNU MP, arbitrary precision arithmetic
License: GPL-3.0-or-later OR LGPL-3.0-or-later
URL: https://gmplib.org/
Source0: https://ftp.gnu.org/gnu/gmp/gmp-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
GNU MP is a library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating point numbers. It has a rich set of functions, and the functions have a regular interface.

%package devel
Summary: GNU MP, arbitrary precision arithmetic
Requires: gmp%{?_isa} = %{version}-%{release}
Provides: pkgconfig(gmp)

%description devel
GNU MP is a library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating point numbers. It has a rich set of functions, and the functions have a regular interface.

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
