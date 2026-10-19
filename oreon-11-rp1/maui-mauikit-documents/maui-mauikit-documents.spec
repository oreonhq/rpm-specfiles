%global source0_hash 13ebf295a5f62a86c8e85468d3a0641259b578da9c4ec2c9c258c25e2527e84b
Name:          maui-mauikit-documents
Version:       4.0.0
Release:        1%{?dist}
License:       MIT AND GPL-3.0-or-later AND LGPL-2.0-or-later AND CC0-1.0 AND BSD-2-Clause AND LGPL-2.1-or-later
Summary:        MauiKit QtQuick plugins for text editing
URL:           https://invent.kde.org/maui/mauikit-documents/
Source0:        https://download.kde.org/stable/maui/mauikit-documents/%{version}/mauikit-documents-%{version}.tar.xz
Patch0:        mauikit-documents-fix-build-against-qt-6-10.patch
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  poppler-qt6-devel
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Required headers to build components based
on %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mauikit-documents-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang mauikitdocuments
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n maui-mauikit-documents-devel -f %{oreon_filedir}/maui-mauikit-documents-devel.list

%changelog

%autochangelog
