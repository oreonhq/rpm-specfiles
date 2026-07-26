%global source0_hash 515eb95d5d2a51b495df01adf56ef0af703c5d344bb49bc2a6390ef57bba027b

%undefine __cmake_in_source_build
Name:           kdesvn
Version:        2.1.0
Release:        16%{?dist}
Summary:        Subversion client for KDE

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/KDE/kdesvn
Source0:        http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}-1.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  subversion-devel
BuildRequires:  neon-devel
BuildRequires:  cmake3 >= 3.1.0
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  libappstream-glib

%description
KDESvn is a frontend to the subversion vcs. In difference to most other
tools it uses the subversion C-Api direct via a c++ wrapper made by Rapid
SVN and doesn't parse the output of the subversion client. So it is a real
client itself instead of a frontend to the command line tool.

It is designed for the K-Desktop environment and uses all of the goodies
it has. It is planned for future that based on the native client some plugins
for konqueror and/or kate will made.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# TODO: Please submit an issue to upstream (rhbz#2380672)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# erase invalid tag order (2.0 before 2.1)
sed -i -e '/release version="2.0" date="2016-12-10"/d' src/org.kde.kdesvn.appdata.xml

%cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-html

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING GPL.txt
%{_bindir}/%{name}
%{_bindir}/kdesvnaskpass
%{_qt5_plugindir}/kdesvnpart.so
%{_qt5_plugindir}/kio_ksvn.so
%{_kf5_plugindir}/kded/kdesvnd.so
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/*.protocol
%{_datadir}/kservices5/ServiceMenus/%{name}*.desktop
%{_datadir}/config.kcfg/kdesvn_part.kcfg
%{_datadir}/dbus-1/interfaces/kf5_org.kde.kdesvnd.xml
%{_datadir}/dbus-1/services/org.kde.kdesvnd.service
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svgz
%{_datadir}/kconf_update/kdesvn-use-external-update.sh
%{_datadir}/kconf_update/kdesvnpartrc-use-external.upd
%{_datadir}/%{name}
%{_datadir}/kxmlgui5/%{name}
%{_datadir}/metainfo/org.kde.kdesvn.appdata.xml
%{_mandir}/man1/kdesvn.1.gz
%{_mandir}/man1/kdesvnaskpass.1.gz
%{_mandir}/*/man1/*.gz

%changelog
%autochangelog
