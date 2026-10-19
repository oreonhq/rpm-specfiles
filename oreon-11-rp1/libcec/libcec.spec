%global source0_hash e4ac4d1dd3559cf83189d29ab40fc5537b5a2beceb82916ef173dac7e50dbfa0
Summary:        Library for controlling CEC-enabled devices over HDMI
Name:           libcec
Version:        8.1.7
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://libcec.pulse-eight.com/
Source0:        https://github.com/Pulse-Eight/libcec/archive/refs/tags/libcec-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libudev-devel
BuildRequires:  lockdev-devel
BuildRequires:  make
BuildRequires:  p8-platform-devel
BuildRequires:  python3-devel
BuildRequires:  swig
# /oreon:deps
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
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
%description utils
The cec-client command line tool for testing and controlling CEC devices.

%package -n python3-%{name}
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n python3-%{name}
Python 3 bindings for libCEC.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-libcec-%{version}

%build

%cmake -DHAVE_LOCKDEV=1
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libcec.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libcec-devel -f %{oreon_filedir}/libcec-devel.list
%files -n libcec-utils -f %{oreon_filedir}/libcec-utils.list
%files -n python3-libcec -f %{oreon_filedir}/python3-libcec.list

%changelog

%autochangelog
