%global source0_hash bfabdc12234f9ae73ba652d881d66e9220fba3f8bbf6074fcde6a0e90cc7fc1a

%global app_id  org.kde.hashomatic

Name:           hash-o-matic
Version:        1.0.1
Release:        4%{?dist}
Summary:        KDE file checksum utility
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND CC0-1.0 AND BSD-2-Clause
URL:            https://apps.kde.org/hashomatic/
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(QGpgmeQt6)

Requires:       hicolor-icon-theme
Requires:       qt6qml(org.kde.coreaddons)
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)

%description
Hash-o-matic is an application allowing to generate, compare, and verify
sha256, sha1 and md5 checksums for files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang hashomatic

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}.metainfo.xml

%files -f hashomatic.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/hashomatic
%{_kf6_datadir}/applications/%{app_id}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_kf6_datadir}/kio/servicemenus/hashFile.desktop
%{_kf6_metainfodir}/%{app_id}.metainfo.xml

%changelog
%autochangelog
