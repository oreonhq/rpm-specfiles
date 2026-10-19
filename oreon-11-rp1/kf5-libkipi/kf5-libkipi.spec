%global source0_hash 4c06da914ab3bd952976cc135d24c307e972ef0007c754738f3644e567db88ba
%global base_name libkipi
Name:    kf5-libkipi
Summary:        Common plugin infrastructure for KDE image applications
Version: 24.05.2
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/%{base_name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(Qt5Gui)
# /oreon:deps
%description
Kipi (KDE Image Plugin Interface) is an effort to develop a common plugin
structure (for Digikam, Gwenview, etc.). Its aim is to share
image plugins among graphic applications.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Gui)
Requires: cmake(KF5Config)
Requires: cmake(KF5Service)
Requires: cmake(KF5XmlGui)
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup  -n %{base_name}-%{version} -p1

%build

%{cmake_kf5}
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-libkipi-devel -f %{oreon_filedir}/kf5-libkipi-devel.list

%changelog

%autochangelog
