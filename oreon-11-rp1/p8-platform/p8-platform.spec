%global source0_hash 064f8d2c358895c7e0bea9ae956f8d46f3f057772cb97f2743a11d478a0f68a0

Summary:        Platform support library used by libcec
Name:           p8-platform
Version:        2.1.0.1
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/Pulse-Eight/platform
Source0:        https://github.com/Pulse-Eight/platform/archive/refs/tags/p8-platform-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
p8-platform is a small, portable platform abstraction library (threads,
sockets, atomics) written by Pulse-Eight, used to build libcec.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers, pkgconfig and CMake config files for building against p8-platform.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n platform-p8-platform-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md debian/copyright
%{_libdir}/libp8-platform.so.2*

%files devel
%{_includedir}/p8-platform/
%{_libdir}/libp8-platform.so
%{_libdir}/pkgconfig/p8-platform.pc
%{_libdir}/p8-platform/

%changelog
%autochangelog
