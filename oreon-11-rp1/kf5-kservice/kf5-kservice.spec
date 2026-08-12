%global source0_hash 52b7c2c317d0a662ca33200f9b4f93e0b7efb1843abd120a3b49c9a092f4a869

%undefine __cmake_in_source_build
%global framework kservice

Name:    kf5-%{framework}
Summary: KDE Frameworks 5 Tier 3 solution for advanced plugin and service introspection
Version: 5.116.0
Release: 7%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

## upstream patches

## downstream patches
# Fedora customizations to the menu categories
# adds the Administration menu from redhat-menus which equals System + Settings
# This prevents the stuff getting listed twice, under both System and Settings.
Patch100:  kservice-5.15.0-xdg-menu.patch

# kbuildsycoca5 always gives:
# kf5.kservice.sycoca: Parse error in  "$HOME/.config/menus/applications-merged/xdg-desktop-menu-dummy.menu" , line  1 , col  1 :  "unexpected end of file"
# hide that by default, make it qCDebug instead (of qCWarning)
Patch101:  kservice-5.17.0-vfolder_spam.patch

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kcrash-devel >= %{majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{majmin}
BuildRequires:  kf5-kdoctools-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

BuildRequires:  flex
BuildRequires:  bison

# for the Administration category
Recommends:       redhat-menus

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

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
# this is not a config file, despite rpmlint complaining otherwise -- rex
%{_kf5_sysconfdir}/xdg/menus/kf5-applications.menu
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_bindir}/kbuildsycoca5
%{_kf5_libdir}/libKF5Service.so.5*
%{_kf5_datadir}/kservicetypes5/
%{_kf5_datadir}/kservices5/
%{_kf5_mandir}/man8/*.8*

%files devel

%{_kf5_includedir}/KService/
%{_kf5_libdir}/libKF5Service.so
%{_kf5_libdir}/cmake/KF5Service/
%{_kf5_archdatadir}/mkspecs/modules/qt_KService.pri

%changelog
%autochangelog
