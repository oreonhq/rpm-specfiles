%global source0_hash 75a10c8707f83fd76e08c9608723b5181d9f828d7d50e21763d1fd25623fdd04

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    juk
Summary: Music player
Version: 25.12.3
Release: 1%{?dist}

# code: KDE e.V. may determine that future GPL versions are accepted
# handbook doc: GFDL-1.2-no-invariants-or-later
License: (GPL-2.0-only OR GPL-3.0-only) AND GFDL-1.2-no-invariants-or-later
URL:     https://invent.kde.org/multimedia/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6StatusNotifierItem)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Multimedia)

BuildRequires: cmake(Phonon4Qt6)
BuildRequires: pkgconfig(taglib)

# when split occurred
Obsoletes: kdemultimedia-juk < 6:4.8.80
Provides:  kdemultimedia-juk = 6:%{version}-%{release}

# docs/translations moved here
Conflicts: kde-l10n < 17.08.3-2

%description
Juk is a jukebox, tagger and music collection manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.juk.metainfo.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.juk.desktop

%files -f %{name}.lang
%license COPYING*
%{_datadir}/dbus-1/interfaces/org.kde.juk.*.xml
%{_kf6_bindir}/juk
%{_kf6_datadir}/applications/org.kde.juk.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/juk.*
%{_kf6_datadir}/juk/
%{_kf6_datadir}/kio/servicemenus/jukservicemenu.desktop
%{_kf6_datadir}/knotifications6/juk.*
%{_kf6_metainfodir}/org.kde.juk.metainfo.xml

%changelog
%autochangelog
