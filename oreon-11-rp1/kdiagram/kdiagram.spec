%global source0_hash 4659b0c2cd9db18143f5abd9c806091c3aab6abc1a956bbf82815ab3d3189c6d
Name:    kdiagram
Summary:        Powerful libraries (KChart, KGantt) for creating business diagrams
Version: 3.0.1
Release:        1%{?dist}
License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
Url:     https://invent.kde.org/graphics/kdiagram
Source0:        http://download.kde.org/stable/kdiagram/%{version}/kdiagram-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
Powerful libraries (KChart, KGantt) for creating business diagrams.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Svg)
Requires: cmake(Qt6Widgets)
Requires: cmake(Qt6PrintSupport)
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang_kf6 kchart6_qt
%find_lang_kf6 kgantt6_qt
cat kchart6_qt.lang kgantt6_qt.lang > %{name}.lang
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kdiagram-devel -f %{oreon_filedir}/kdiagram-devel.list

%changelog

* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 3.0.1-1
- Latest upstream release

%autochangelog
