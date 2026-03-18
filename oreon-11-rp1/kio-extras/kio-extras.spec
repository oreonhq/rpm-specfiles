Name:    kio-extras
Version: 25.12.3
Release: 1%{?dist}
Summary: Additional components to increase the functionality of KIO Framework

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/network/kio-extras

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstramable patches

## upstream patches

BuildRequires:  bzip2-devel
BuildRequires:  gperf

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DNSSD)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Notifications)

BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaActivitiesStats)

BuildRequires:  cmake(KDSoap) >= 1.9
BuildRequires:  cmake(KDSoapWSDiscoveryClient)
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  pkgconfig(libproxy-1.0)

BuildRequires:  libjpeg-devel
BuildRequires:  libmtp-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel
BuildRequires:  cmake(OpenEXR)
BuildRequires:  perl-generators
BuildRequires:  phonon-qt6-devel
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  taglib-devel > 1.11

# This package provides plugins for KIO
Supplements:    kf6-kio-core

%description
%{summary}.

%package info
Summary: Info kioslave
%description info
Kioslave for reading info pages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 -DLIBSSH_LIBRARIES="$(pkg-config --libs libssh)"
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%license LICENSES/*

%{_kf6_plugindir}/kded/
%exclude %{_kf6_plugindir}/kio/info.so
%{_kf6_plugindir}/kio/
%{_kf6_plugindir}/kiod/
%{_kf6_plugindir}/thumbcreator/
%{_kf6_plugindir}/kfileitemaction/
%{_datadir}/config.kcfg/jpegcreatorsettings5.kcfg
%{_datadir}/dbus-1/services/org.kde.kmtpd5.service
%{_datadir}/applications/kcm_*
%{_datadir}/mime/packages/org.kde.kio.smb.xml
%{_datadir}/remoteview/
%{_datadir}/konqueror/
%dir %{_kf6_datadir}/kio_filenamesearch/
%{_kf6_datadir}/kio_filenamesearch/kio-filenamesearch-grep
%{_kf6_datadir}/qlogging-categories6/kio-extras*
%{_kf6_datadir}/solid/actions/solid_afc.desktop
%{_kf6_datadir}/solid/actions/solid_mtp.desktop
%{_kf6_libdir}/libkioarchive6.so.6{,.*}
%{_kf6_libexecdir}/smbnotifier
%{_libexecdir}/wpad-detector-helper
%{_kf6_qtplugindir}/kcm_trash.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_*.so

%files info
%{_kf6_plugindir}/kio/info.so
# perl deps, but required at runtime for the info kioslave to actually work:
%dir %{_datadir}/kio_info/
%{_datadir}/kio_info/kde-info2html*

%files devel
%{_includedir}/KioArchive6/*.h
%{_kf6_libdir}/cmake/KioArchive6/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
