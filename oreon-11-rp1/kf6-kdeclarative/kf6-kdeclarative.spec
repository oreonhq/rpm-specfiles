%global source1_hash 585b7d3e651d88c79438390910480d1272ee1da10958bc9d1260b630eea70bba
%global source0_hash 7ec3583a2cf2cd7143e39936ffb39e22d20563f4c87a8462e0e9d12c59ea89a6
%global framework kdeclarative
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 3 addon for Qt declarative
License: CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:  kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libepoxy-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
# /oreon:deps
%description
KDE Frameworks 6 Tier 3 addon for Qt declarative

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Config)
Requires:       cmake(KF6Package)
Requires:       qt6-qtdeclarative-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{name} --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kdeclarative-devel -f %{oreon_filedir}/kf6-kdeclarative-devel.list

%changelog

%autochangelog
