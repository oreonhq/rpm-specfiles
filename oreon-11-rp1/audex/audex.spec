%global stable_kf6 stable
%global source0_hash cf558c7421bccc611628ba2e333a1ca3efb80922aeb99d407026ebbe0c384162

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           audex
Version:        26.08.1
Release:        1%{?dist}
Summary:        Audio ripper
License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later
URL:            https://apps.kde.org/audex/
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Qml)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KCddb6)

BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcdio_paranoia)

# encoder backends
Recommends:     flac
Recommends:     lame
Recommends:     vorbis-tools

%description
Audex is an audio grabber tool for CD-ROM drives built with KDE Frameworks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.audex.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.audex.appdata.xml

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/audex
%{_kf6_datadir}/solid/actions/audex-rip-audiocd.desktop
%{_kf6_datadir}/applications/org.kde.audex.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.audex.svg
%{_kf6_datadir}/audex/
%{_kf6_metainfodir}/org.kde.audex.appdata.xml

%changelog
%autochangelog
