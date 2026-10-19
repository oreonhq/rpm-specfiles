%global source0_hash 7f1f02924691cc764af5f79c0c227735d75cdc3c68457160bd302ccee1699f02
Name:          maui-mauikit-imagetools
Version:       4.0.0
Release:        1%{?dist}
License:       GPL-3.0-or-later AND BSD-2-Clause AND GPL-2.0-only AND LGPL-2.1-or-later AND LGPL-2.1-only AND LGPL-2.0-or-later AND CC0-1.0 AND LGPL-3.0-or-later AND GPL-3.0-only AND LGPL-3.0-only
Summary:        MauiKit Image Tools Components
URL:           https://invent.kde.org/maui/mauikit-imagetools/
Source0:        https://download.kde.org/stable/maui/mauikit-imagetools/%{version}/mauikit-imagetools-%{version}.tar.xz
Patch0:        7.patch
ExcludeArch:   %{ix86}
Requires:      %{name}-cities
# oreon:deps
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(OpenCV)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Tesseract)
BuildRequires:  cmake(exiv2)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Required headers to build components based
on %{name}.

%package cities
Summary:        %{name} cities database
BuildArch: noarch
%description cities
Cities database required for geolocation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mauikit-imagetools-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang mauikitimagetools
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n maui-mauikit-imagetools-devel -f %{oreon_filedir}/maui-mauikit-imagetools-devel.list
%files -n maui-mauikit-imagetools-cities -f %{oreon_filedir}/maui-mauikit-imagetools-cities.list

%changelog

%autochangelog
