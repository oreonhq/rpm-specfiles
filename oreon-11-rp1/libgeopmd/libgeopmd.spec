%global source0_hash 83079122c51f781a3be03dc6814be5da4715a02f7acadb1f27f85ad22b72e603
%define abi_ver 2.2.0
%global desc %{expand: \
The Global Extensible Open Power Manager (GEOPM) provides a framework to
explore power and energy optimizations on platforms with heterogeneous mixes
of computing hardware.
Users can monitor their system's energy and power consumption, and safely
optimize system hardware settings to achieve energy efficiency and/or
performance objectives.}
Name:		libgeopmd
Version:	3.2.1
Release:        1%{?dist}
Summary:        C/C++ implementation of the GEOPM access service
License:	BSD-3-Clause
URL:		https://geopm.github.io
Source0:        https://github.com/geopm/geopm/archive/v%{version}/geopm-%{version}.tar.gz
Patch0:		libgeopmd-fedora.patch
ExclusiveArch:	x86_64
Requires:	abseil-cpp
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  gmock-devel
BuildRequires:  grpc-devel
BuildRequires:  gtest-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  liburing-devel
BuildRequires:  protobuf-devel
BuildRequires:  systemd-devel
BuildRequires:  zlib-ng-compat-devel
# /oreon:deps
%description
%{desc}

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%package -n geopmd-cli
Summary:	libgeopmd command-line tools
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	geopmd
%description -n geopmd-cli
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n geopm-%{version}

pushd %{name}
echo %{version} > VERSION
autoreconf -vif
popd

%build

pushd %{name}
%configure \
	--disable-build-gtest \
	--enable-grpc
%make_build
popd
%install
pushd %{name}
%make_install
rm -v %{buildroot}/%{_libdir}/libgeopmd.a
rm -v %{buildroot}/%{_libdir}/libgeopmd.la
popd
%oreon_autofiles geopmd-cli usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd %{name}
make check
popd
%files -f %{oreon_filedir}/main.list
%files -n libgeopmd-devel -f %{oreon_filedir}/libgeopmd-devel.list
%files -n geopmd-cli -f %{oreon_filedir}/geopmd-cli.list

%changelog

%autochangelog
