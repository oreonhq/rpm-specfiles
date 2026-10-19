%global source0_hash 3b19a148b1e7ad84df41cad7d74fcc198326e1e27140e5127ddfe6b6475b1643
Name:          maui-mauikit-archiver
Version:       4.0.0
Release:        1%{?dist}
License:       LGPL-2.1-or-later AND BSD-2-Clause AND GPL-3.0-or-later
Summary:        Maui plugin for online archived/compressed files management
URL:           https://invent.kde.org/maui/mauikit-archiver/
Source0:        https://download.kde.org/stable/maui/mauikit-archiver/%{version}/mauikit-archiver-%{version}.tar.xz
Patch0:        licenses.patch
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
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
%global oreon_srcdir mauikit-archiver-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
sed -e '/prefer/d' -i %{buildroot}%{_kf6_qmldir}/org/mauikit/archiver/qmldir
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n maui-mauikit-archiver-devel -f %{oreon_filedir}/maui-mauikit-archiver-devel.list

%changelog

%autochangelog
