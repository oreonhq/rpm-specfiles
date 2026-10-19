%global source0_hash 5a06482dd05b430ea745b72b7cb495444ab84223c27152375035d4fd3615825c
%global framework libksieve
ExcludeArch: %{ix86}
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        Sieve support library
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{framework}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}
%global kf5_ver 5.23.0
%global majmin_ver %{version}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-libs < 7:16.04.0
# oreon:deps
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-akonadi-contacts-devel
BuildRequires:  kf5-akonadi-server-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kidentitymanagement-devel
BuildRequires:  kf5-kmailtransport-devel
BuildRequires:  kf5-kmime-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kpimtextedit-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-libkdepim-devel
BuildRequires:  kf5-pimcommon-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-syntax-highlighting-devel
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
# /oreon:deps
%description
%{summary}.

%package        libs
Summary:        Only the linkable libraries for %{name}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5SyntaxHighlighting)
%description    devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libksieve5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libksieve/libksieve5/" src/CMakeLists.txt
sed -i "s/libksieve/libksieve5/" src/Messages.sh

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-libksieve-libs -f %{oreon_filedir}/kf5-libksieve-libs.list
%files -n kf5-libksieve-devel -f %{oreon_filedir}/kf5-libksieve-devel.list

%changelog

%autochangelog
