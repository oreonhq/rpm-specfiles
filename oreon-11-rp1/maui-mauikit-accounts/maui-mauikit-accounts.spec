%global source0_hash 28461b6155c770eaf10ec01e6c0fd07103ef2be23036f2d43a8e5f3321b432ef
Name:          maui-mauikit-accounts
Version:       4.0.0
Release:        1%{?dist}
License:       BSD-2-Clause AND LGPL-2.1-or-later AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later
Summary:        MauiKit utilities to handle User Accounts
URL:           https://invent.kde.org/maui/mauikit-accounts
Source0:        https://download.kde.org/stable/maui/mauikit-accounts/%{version}/mauikit-accounts-4.0.0.tar.xz
# oreon:deps
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(MauiKit4)
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
%global oreon_srcdir mauikit-accounts-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang mauikitaccounts
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n maui-mauikit-accounts-devel -f %{oreon_filedir}/maui-mauikit-accounts-devel.list

%changelog

%autochangelog
