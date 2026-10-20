%global source0_hash 91204cd32f164bd3b7c992d4a6a8ce6519511aadab30f78b6982d0bf8d73e931
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: mpc
Version: 1.4.1
Release: 1%{?dist}
Summary: GNU MPC, a complex floating-point library
License: LGPL-3.0-or-later
URL: https://www.multiprecision.org/mpc/
Source0: https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gmp-devel
BuildRequires: mpfr-devel
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
GNU MPC is a complex floating-point library with exact rounding. It is based on the GNU MPFR floating-point library (http://www.mpfr.org/), which is itself based on the GNU MP library (http://gmplib.org/).

%package devel
Summary: GNU MPC, a complex floating-point library
Requires: mpc%{?_isa} = %{version}-%{release}
Provides: pkgconfig(mpc)

%description devel
GNU MPC is a complex floating-point library with exact rounding. It is based on the GNU MPFR floating-point library (http://www.mpfr.org/), which is itself based on the GNU MP library (http://gmplib.org/).

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
