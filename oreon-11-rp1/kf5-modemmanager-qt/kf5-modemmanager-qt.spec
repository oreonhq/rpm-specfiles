%global source0_hash 06055351f3a6f8755df60f48b3fdaabb4a406939b9c777f474e8a22bdd116f80
%undefine __cmake_in_source_build
%global framework modemmanager-qt
ExcludeArch: %{ix86}
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        A Tier 1 KDE Frameworks module wrapping ModemManager DBus API
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/modemmanager-qt-%{version}.tar.xz
Requires:       kf5-filesystem >= %{majmin}
# oreon:deps
BuildRequires:  ModemManager-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
A Qt 5 library for ModemManager.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ModemManager-devel
Requires:       qt5-qtbase-devel
%description    devel
Qt 5 libraries and header files for developing applications
that use ModemManager.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-modemmanager-qt-devel -f %{oreon_filedir}/kf5-modemmanager-qt-devel.list

%changelog

%autochangelog
