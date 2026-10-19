%global source0_hash 5f5b1cc3cc2a0f204089d55ff8dae5236da147878fb0925080399090d05f4d2e
%global framework pimcommon
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        PIM common libraries
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://api.kde.org/kdepim/pimcommon/html/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}
%global kf5_ver 5.28
%global majmin_ver %{version}
Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-libs < 7:16.04.0
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KPim5Ldap)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-akonadi-contacts-devel
BuildRequires:  kf5-akonadi-mime-devel
BuildRequires:  kf5-akonadi-search-devel
BuildRequires:  kf5-akonadi-server-devel
BuildRequires:  kf5-grantleetheme-devel
BuildRequires:  kf5-kcalendarcore-devel
BuildRequires:  kf5-kcontacts-devel
BuildRequires:  kf5-kimap-devel
BuildRequires:  kf5-kmime-devel
BuildRequires:  kf5-kpimtextedit-devel
BuildRequires:  kf5-libkdepim-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(libxslt)
# /oreon:deps
%description
%{summary}.

%package        akonadi
Summary:        The PimCommonAkondi runtime library
Obsoletes:      kf5-libkdepim-akonadi < 20.08.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description akonadi
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5Config)
Requires:       cmake(KF5TextAutoCorrectionWidgets)
Requires:       %{name}-akonadi%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KPim5AkonadiContact)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5IMAP)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libpimcommon5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libpimcommon/libpimcommon5/" src/CMakeLists.txt
sed -i "s/libpimcommon/libpimcommon5/" src/Messages.sh

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
