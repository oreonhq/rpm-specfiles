%global source0_hash 537512904744b35e232912055ccf8ec66d768639ff3abe5788d90d792ec5f48b
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: lz4
Version: 1.10.0
Release: 1%{?dist}
Summary: LZ4 compression
License: BSD-2-Clause OR GPL-2.0-only
URL: https://lz4.org/
Source0: https://github.com/lz4/lz4/releases/download/v%{version}/lz4-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
LZ4 is a lossless compression algorithm, providing compression speed at 400 MB/s per core.

%package devel
Summary: LZ4 compression
Requires: lz4%{?_isa} = %{version}-%{release}
Provides: pkgconfig(liblz4)

%description devel
LZ4 is a lossless compression algorithm, providing compression speed at 400 MB/s per core.

%prep
%oreon_sha256
%autosetup -p1

%build
make -s %{?_smp_mflags} BUILD_STATIC=no PREFIX=%{_prefix} CFLAGS="%{_oreon_cflags} -fPIE"

%install
make -s install BUILD_STATIC=no DESTDIR=%{buildroot} PREFIX=%{_prefix} libdir=%{_libdir}

%files
%license LICENSE
%{_bindir}/lz4
%{_bindir}/lz4c
%{_bindir}/lz4cat
%{_bindir}/unlz4
%{_libdir}/liblz4.so.1
%{_libdir}/liblz4.so.1.*
%{_mandir}/man1/lz4.1*
%{_mandir}/man1/lz4c.1*
%{_mandir}/man1/lz4cat.1*
%{_mandir}/man1/unlz4.1*

%files devel
%{_includedir}/lz4.h
%{_includedir}/lz4frame.h
%{_includedir}/lz4hc.h
%{_libdir}/liblz4.so
%{_libdir}/pkgconfig/liblz4.pc
