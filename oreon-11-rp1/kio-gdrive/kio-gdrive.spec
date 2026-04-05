Name:           kio-gdrive
Version:        25.12.3
Release:	2%{?dist}
Summary:        An Google Drive KIO slave for KDE

License:        GPL-2.0-or-later
URL:            https://community.kde.org/KIO_GDrive
# use releaseme
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


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
%autosetup -p1

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
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
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
