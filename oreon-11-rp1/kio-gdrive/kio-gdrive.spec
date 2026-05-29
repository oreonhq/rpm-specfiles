%global source0_hash none

Name:           kio-gdrive
Version:        26.04.1
Release:        1%{?dist}
Summary:        An Google Drive KIO slave for KDE

License:        GPL-2.0-or-later
URL:            https://community.kde.org/KIO_GDrive
# use releaseme
Source0:        https://download.kde.org/%{stable_kf6}/release-service/26.04.1/src/kio-gdrive-26.04.1.tar.xz


# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# arch's where libkgapi is available (due to inderect dependencies on qtwebengine)
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(KAccounts6)
BuildRequires:  libkgapi-devel
BuildRequires:  libaccounts-glib-devel
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  libappstream-glib
BuildRequires:  intltool
BuildRequires:  cmake(KF6Purpose)
Requires:       kaccounts-providers

# QML SSO.OnlineAccounts
Requires:       accounts-qml-module-qt6

%description
Provides KIO Access to Google Drive using the gdrive:/// protocol.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kio6_gdrive --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_datadir}/remoteview/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml ||:

%files -f kio6_gdrive.lang
%license COPYING
%doc HACKING README.md
%{_qt6_plugindir}/kaccounts/daemonplugins/gdrive.so
%{_kf6_plugindir}/kfileitemaction/gdrivecontextmenuaction.so
%{_kf6_plugindir}/propertiesdialog/gdrivepropertiesplugin.so
%{_kf6_plugindir}/purpose/purpose_gdrive.so
%{_kf6_datadir}/accounts/services/kde/google-drive.service
%{_kf6_datadir}/knotifications6/gdrive.notifyrc
%{_kf6_datadir}/remoteview/gdrive-network.desktop
%{_kf6_datadir}/metainfo/org.kde.kio_gdrive.metainfo.xml
%{_kf6_qtplugindir}/kf6/kio/gdrive.so
%{_datadir}/purpose/purpose_gdrive_config.qml

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
