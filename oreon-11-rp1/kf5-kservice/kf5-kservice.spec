%global source0_hash 52b7c2c317d0a662ca33200f9b4f93e0b7efb1843abd120a3b49c9a092f4a869
%undefine __cmake_in_source_build
%global framework kservice
Name:    kf5-%{framework}
Summary:        KDE Frameworks 5 Tier 3 solution for advanced plugin and service introspection
Version: 5.116.0
Release:        1%{?dist}
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Patch100:  kservice-5.15.0-xdg-menu.patch
Patch101:  kservice-5.17.0-vfolder_spam.patch
Recommends:       redhat-menus
# oreon:deps
BuildRequires:  bison
BuildRequires:  extra-cmake-modules
BuildRequires:  flex
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
KDE Frameworks 5 Tier 3 solution for advanced plugin and service
introspection.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfig-devel >= %{majmin}
Requires:       kf5-kcoreaddons-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%{cmake_kf5}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-man
mv %{buildroot}%{_kf5_sysconfdir}/xdg/menus/applications.menu \
   %{buildroot}%{_kf5_sysconfdir}/xdg/menus/kf5-applications.menu
mkdir -p %{buildroot}%{_kf5_datadir}/kservices5
mkdir -p %{buildroot}%{_kf5_datadir}/kservicetypes5
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kservice-devel -f %{oreon_filedir}/kf5-kservice-devel.list

%changelog

%autochangelog
