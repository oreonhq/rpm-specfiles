%global source0_hash b4514749b30b5aa3c61c36925b2e603a5d25da6865e7b3eb84709654ba0fb090
Name:           dtk6log
Version:        6.7.32
Release:        1%{?dist}
Summary:        Simple, convenient and thread safe logger for Qt-based C++ apps
License:        LGPL-2.1-or-later
URL:            https://github.com/linuxdeepin/dtklog
Source0:        https://github.com/linuxdeepin/dtklog/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(spdlog)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsystemd)
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir dtklog-%{version}
%oreon_prep
%build

%cmake -DDTK5=OFF -DBUILD_WITH_SYSTEMD=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dtk6log-devel -f %{oreon_filedir}/dtk6log-devel.list

%changelog

%autochangelog
