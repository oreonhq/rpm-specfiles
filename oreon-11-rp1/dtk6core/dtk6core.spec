%global source0_hash 7a5628c4182b61be3b228f6b88ecbd4e0f46f34daa525ce572c3df142fd493de
Name:           dtk6core
Version:        6.7.32
Release:        1%{?dist}
Summary:        Deepin tool kit core modules
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        https://github.com/linuxdeepin/dtkcore/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       deepin-desktop-base
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Log)
BuildRequires:  cmake(DtkBuildHelper)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(spdlog)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(uchardet)
# /oreon:deps
%description
Deepin tool kit core modules.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcommon-devel%{_isa}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# comply with dtkcore in Fedora and dtk6core in Arch Linux
sed -i 's|/etc/os-version|/etc/dde-version|' src/dsysinfo.cpp

%build

%cmake -GNinja -DDTK5=OFF -DBUILD_WITH_SYSTEMD=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dtk6core-devel -f %{oreon_filedir}/dtk6core-devel.list

%changelog

%autochangelog
