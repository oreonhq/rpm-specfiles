%global source0_hash d927b8c8e0d65c1ae2bb49217a3beaaed5ec9c4b3b576d6aa5c486a07f83a3c1
Name:           dtklog
Version:        6.7.50
Release:        1%{?dist}
Summary:        Simple, convenient and thread safe logger for Qt-based C++ apps
License:        LGPL-2.1-or-later
URL:            https://github.com/linuxdeepin/dtklog
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(spdlog)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  qt5-qtbase-private-devel
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
%oreon_prep
%build

%cmake \
    -DBUILD_WITH_SYSTEMD=ON \
    -DBUILD_WITH_QT6=OFF \
    -DDLOG_VERSION=%{version} \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dtklog-devel -f %{oreon_filedir}/dtklog-devel.list

%changelog

%autochangelog
