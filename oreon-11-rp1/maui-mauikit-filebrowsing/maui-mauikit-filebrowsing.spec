%global source0_hash b93edb5b07fd1fd74f4b46d5bb1402c57370728038e7e407dba1be3730f1da2e

Name:          maui-mauikit-filebrowsing
Version:       4.0.0
Release:       7%{?dist}
License:       CC0-1.0 AND BSD-2-Clause AND LGPL-2.1-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later
Summary:       MauiKit File Browsing utilities and controls
URL:           https://invent.kde.org/maui/mauikit-filebrowsing/

Source0:       https://download.kde.org/stable/maui/mauikit-filebrowsing/%{version}/mauikit-filebrowsing-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Network)

BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)

BuildRequires: cmake(MauiKit4)

%description
FileBrowsing is a MauiKit Framework to work with local and remote files.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mauikit-filebrowsing-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang mauikitfilebrowsing

%files -f mauikitfilebrowsing.lang
%license LICENSES/*
%{_kf6_libdir}/libMauiKitFileBrowsing4.so.4
%{_kf6_libdir}/libMauiKitFileBrowsing4.so.%{version}
%{_kf6_qmldir}/org/mauikit/filebrowsing/

%files devel
%{_includedir}/MauiKit4/FileBrowsing/
%{_kf6_libdir}/cmake/MauiKitFileBrowsing4/
%{_kf6_libdir}/libMauiKitFileBrowsing4.so

%changelog
%autochangelog
