%global source0_hash 7f1f02924691cc764af5f79c0c227735d75cdc3c68457160bd302ccee1699f02

Name:          maui-mauikit-imagetools
Version:       4.0.0
Release:       8%{?dist}
License:       GPL-3.0-or-later AND BSD-2-Clause AND GPL-2.0-only AND LGPL-2.1-or-later AND LGPL-2.1-only AND LGPL-2.0-or-later AND CC0-1.0 AND LGPL-3.0-or-later AND GPL-3.0-only AND LGPL-3.0-only
Summary:       MauiKit Image Tools Components
URL:           https://invent.kde.org/maui/mauikit-imagetools/

Source0:       https://download.kde.org/stable/maui/mauikit-imagetools/%{version}/mauikit-imagetools-%{version}.tar.xz

# Apps depending on imagetools fail to start because of a path issue with some qml files
# https://invent.kde.org/maui/mauikit-imagetools/-/merge_requests/7
Patch0:        7.patch

# Doesn't build on i686.
ExcludeArch:   %{ix86}

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(exiv2)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)

BuildRequires: cmake(MauiKit4)
BuildRequires: cmake(KQuickImageEditor)
BuildRequires: cmake(Tesseract)
BuildRequires: cmake(OpenCV)

Requires:      %{name}-cities

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

%autosetup -p1 -n mauikit-imagetools-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang mauikitimagetools

%files -f mauikitimagetools.lang
%license LICENSES/*
%{_kf6_libdir}/libMauiKitImageTools4.so.4
%{_kf6_libdir}/libMauiKitImageTools4.so.%{version}
%{_kf6_qmldir}/org/mauikit/imagetools/

%files devel
%{_kf6_libdir}/cmake/MauiKitImageTools4/
%{_kf6_libdir}/libMauiKitImageTools4.so
%{_includedir}/MauiKit4/FileBrowsing/imagetools_version.h
%{_includedir}/MauiKit4/ImageTools/

%files cities
%{_kf6_datadir}/org/mauikit/imagetools/cities.db

%changelog
%autochangelog
