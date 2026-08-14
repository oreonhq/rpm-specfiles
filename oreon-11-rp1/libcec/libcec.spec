%global source0_hash 7f7da95a4c1e7160d42ca37a3ac80cf6f389b317e14816949e0fa5e2edf4cc64

Summary:        Library for controlling CEC-enabled devices over HDMI
Name:           libcec
Version:        7.1.1
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://libcec.pulse-eight.com/
Source0:        https://github.com/Pulse-Eight/libcec/archive/refs/tags/libcec-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  p8-platform-devel
BuildRequires:  libudev-devel
BuildRequires:  lockdev-devel
BuildRequires:  swig
BuildRequires:  python3-devel

%description
libCEC is a library that allows communication with Pulse-Eight and other
CEC USB adapters, as well as with CEC-capable hardware over HDMI, allowing
control of TVs, receivers and similar devices via the HDMI-CEC bus.

Provides the HDMI-CEC remote control backend used by plasma-bigscreen.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and pkgconfig file for building against libcec.

%package utils
Summary:        Command line client for libcec
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
The cec-client command line tool for testing and controlling CEC devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-libcec-%{version}

%build
%cmake -DHAVE_LOCKDEV=1
%cmake_build

%install
%cmake_install

%files
%license LICENSE.md
%doc README.md ChangeLog
%{_libdir}/libcec.so.*

%files devel
%{_includedir}/libcec/
%{_libdir}/libcec.so
%{_libdir}/pkgconfig/libcec.pc

%files utils
%{_bindir}/cec-client
%{_bindir}/cecc-client

%changelog
%autochangelog
