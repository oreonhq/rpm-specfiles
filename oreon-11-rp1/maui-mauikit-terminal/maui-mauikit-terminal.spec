%global source0_hash b471c95b04bad6719f2b1e93a593b6e0bb1fb2f5ef273f11816abac946c66dbb
Name:          maui-mauikit-terminal
Version:       4.0.0
Release:        1%{?dist}
License:       LGPL-2.0-or-later AND GPL-3.0-or-later AND CC0-1.0 AND GPL-2.0-or-later
Summary:        Terminal support components for Maui applications
URL:           https://invent.kde.org/maui/mauikit-terminal
Source0:        https://download.kde.org/stable/maui/mauikit-terminal/%{version}/mauikit-terminal-4.0.0.tar.xz
Patch0:        licenses.patch
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Pty)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
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
%global oreon_srcdir mauikit-terminal-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang mauikitterminal
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n maui-mauikit-terminal-devel -f %{oreon_filedir}/maui-mauikit-terminal-devel.list

%changelog

%autochangelog
