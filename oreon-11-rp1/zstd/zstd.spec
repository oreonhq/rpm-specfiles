%global source0_hash eb33e51f49a15e023950cd7825ca74a4a2b43db8354825ac24fc1b7ee09e6fa3
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: zstd
Version: 1.5.7
Release: 8%{?dist}
Summary: Zstandard compression
License: BSD-3-Clause OR GPL-2.0-only
URL: https://facebook.github.io/zstd/
Source0: https://github.com/facebook/zstd/releases/download/v%{version}/zstd-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make

Requires: libzstd%{?_isa} = %{version}-%{release}

%description
Zstandard is a real time compression algorithm, providing high compression ratios.

%package -n libzstd
Summary: Zstandard compression library

%description -n libzstd
Shared library for the Zstandard compression format.

%package -n libzstd-devel
Summary: Development files for the Zstandard library
Requires: libzstd%{?_isa} = %{version}-%{release}
Obsoletes: zstd-devel < 1.5.7-8

%description -n libzstd-devel
Header files and pkg-config file for the Zstandard library.

%prep
%oreon_sha256
%autosetup -p1

%build
make -s -C lib %{?_smp_mflags} PREFIX=%{_prefix} LIBDIR=%{_libdir} PKGCONFIGDIR=%{_libdir}/pkgconfig CFLAGS="%{_oreon_cflags} -fPIC"
make -s -C programs %{?_smp_mflags} prefix=%{_prefix} bindir=%{_bindir} mandir=%{_mandir} CFLAGS="%{_oreon_cflags} -fPIE"

%install
make -s -C lib install-shared install-includes install-pc DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} PKGCONFIGDIR=%{_libdir}/pkgconfig
make -s -C programs install DESTDIR=%{buildroot} prefix=%{_prefix} bindir=%{_bindir} mandir=%{_mandir}

%files
%license LICENSE
%{_bindir}/zstd
%{_bindir}/zstdmt
%{_bindir}/unzstd
%{_bindir}/zstdcat
%{_bindir}/zstdgrep
%{_bindir}/zstdless
%{_mandir}/man1/zstd.1*
%{_mandir}/man1/unzstd.1*
%{_mandir}/man1/zstdcat.1*
%{_mandir}/man1/zstdgrep.1*
%{_mandir}/man1/zstdless.1*

%ldconfig_scriptlets -n libzstd

%files -n libzstd
%license LICENSE
%{_libdir}/libzstd.so.1
%{_libdir}/libzstd.so.1.*

%files -n libzstd-devel
%{_includedir}/zstd.h
%{_includedir}/zstd_errors.h
%{_includedir}/zdict.h
%{_libdir}/libzstd.so
%{_libdir}/pkgconfig/libzstd.pc
