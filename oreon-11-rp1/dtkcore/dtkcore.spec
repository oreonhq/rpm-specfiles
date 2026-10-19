%global source0_hash bf627dee1ce15d10a87d5b974c0272dd0aa8f5c65816d2365f9a7f11be18290f
Name:           dtkcore
Version:        6.7.50
Release:        1%{?dist}
Summary:        Deepin tool kit core modules
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       deepin-desktop-base
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(DtkLog)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  doxygen
BuildRequires:  dtkcommon-devel
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  qt5-qtbase-private-devel
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
sed -i 's|/etc/os-version|/etc/dde-version|' src/dsysinfo.cpp

%build

%cmake -GNinja \
    -DDTK_VERSION=%{version} \
    -DQCH_INSTALL_DESTINATION=%{_qt5_docdir}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dtkcore-devel -f %{oreon_filedir}/dtkcore-devel.list

%changelog

%autochangelog
