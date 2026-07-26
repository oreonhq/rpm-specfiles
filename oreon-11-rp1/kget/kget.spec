%global source0_hash a82873a7dffc52825c12c043e93b3be1326176c276e98c735d5831ff8ea1b0bb

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kget
Summary: Download manager
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/network/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

%global majmin_ver %(echo %{version} | cut -d. -f1,2)

## upstream patches

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KTorrent6)

BuildRequires: cmake(Gpgmepp)
BuildRequires: cmake(QGpgmeQt6)
BuildRequires: pkgconfig(qca2-qt6)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libmms)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# when split occurred
Conflicts: kdenetwork-common < 7:4.10.80
Obsoletes: kdenetwork-kget < 7:4.10.80
Provides:  kdenetwork-kget = 7:%{version}-%{release}

Conflicts: kde-l10n < 17.08.3-2

%description
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: kdenetwork-kget-libs < 7:4.10.80
Provides:  kdenetwork-kget-libs = 7:%{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

## unpackaged files
rm -fv %{buildroot}%{_kf6_libdir}/libkgetcore.so

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS README TODO
%license COPYING*
%{_kf6_bindir}/kget
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/config.kcfg/kget*
%{_kf6_datadir}/dbus-1/services/org.kde.kget.service
%{_kf6_datadir}/icons/hicolor/*/apps/org.kde.kget.*
%{_kf6_datadir}/kget/
%{_kf6_datadir}/kio/servicemenus/kget_download.desktop
%{_kf6_datadir}/knotifications6/kget*
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files libs
%{_kf6_libdir}/libkgetcore.so.*
%{_kf6_qtplugindir}/kget/
%{_kf6_qtplugindir}/kget_kcms/

%changelog
%autochangelog
