%global source0_hash 67a8fc1c9bef2b3704381bfb3fb3ce99e3952bc4fea2817729a7180fddf4a71e
Name:		libsoundio
Version:	2.0.0
Release:        1%{?dist}
Summary:        C library for cross-platform real-time audio input and output
License:	MIT
URL:		http://libsound.io/
Source0:        http://github.com/andrewrk/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:		libsoundio-2.0.0-cmake-4.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
C library providing cross-platform audio input and output. The API is suitable
for real-time software such as digital audio workstations as well as consumer
software such as music players.

%package devel
Summary:	Development files for libsoundio
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for libsoundio.

%package doc
Summary:	Documentation for libsoundio
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for libsoundio.

%package utils
Summary:	Utilities for libsoundio
%description utils
Utilities files for libsoundio.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_STATIC_LIBS=FALSE
%cmake_build
%cmake_build -t doc
%install
%cmake_install
cd %{__cmake_builddir}
install -m 0644 -pDt %{buildroot}%{_docdir}/%{name}-doc/html html/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

cd %{__cmake_builddir}
./unit_tests
./overflow
./underflow
%files -f %{oreon_filedir}/main.list
%files -n libsoundio-devel -f %{oreon_filedir}/libsoundio-devel.list
%files -n libsoundio-doc -f %{oreon_filedir}/libsoundio-doc.list
%files -n libsoundio-utils -f %{oreon_filedir}/libsoundio-utils.list

%changelog

%autochangelog
