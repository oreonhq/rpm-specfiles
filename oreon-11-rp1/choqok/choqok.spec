%global source0_hash 3a9bd870b9de5a4a3d1421287dc9f73a462c7c4fa045ceca65e32598bddeb98c
%bcond konqplugin %[!(0%{?fedora} >= 40 || 0%{?rhel} >= 10)]
%global forgeurl https://github.com/KDE/choqok/
%global commit de3801bb52f4d4ee3ad3cbaa7f8704d0013881f3
Name:    choqok
Version: 1.7.0
Summary:        KDE Micro-Blogging Client
License: GPL-3.0-only
%{forgemeta}
Release:        1%{?dist}
URL:     %{forgeurl}
Source0:        %{forgeurl}archive/%{commit}/%{name}-%{commit}.tar.gz
Source1: %{name}.rpmlintrc
%if %{with konqplugin}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF5Attica)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5Emoticons)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-purpose-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qt5-qtnetworkauth-devel
# /oreon:deps
%description
A Free/Open Source micro-blogging client for K Desktop Environment.
The name comes from an ancient Persian word, which means Sparrow!
Choqok currently supports:
Twitter, Friendica, Mastodon social, Pump.io network, GNU social
and Open Collaboration Services.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}

%package devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{forgesetup}
%autosetup -p1 -n %{archivename}

%build

%{cmake_kf5}
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.choqok.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.choqok.desktop
%files -f %{oreon_filedir}/main.list
%files -n choqok-libs -f %{oreon_filedir}/choqok-libs.list
%files -n choqok-devel -f %{oreon_filedir}/choqok-devel.list

%changelog

%autochangelog
