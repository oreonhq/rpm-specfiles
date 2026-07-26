%global source0_hash 6b2e7ac2c40f6d4eb0e68e847ef62497fdb9c510492a202dce366f3f033a1fad

Name:    cervisia
Summary: CVS frontend
Version: 25.04.2
Release: 4%{?dist}

License: GPL-2.0-or-later AND LGPL-2.0-or-later AND GFDL-1.2-or-later
URL:     https://invent.kde.org/sdk/%{name}.git

Source0: https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5Su)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Widgets)

%{?kf5_kinit_requires}

# translations moved here
Conflicts: kde-l10n < 17.03

Conflicts:      kdesdk-common < 4.10.80
Provides:       kdesdk-cervisia = %{version}-%{release}
Obsoletes:      kdesdk-cervisia < 4.10.80

%description
Cervisia is a CVS frontend for KDE

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.cervisia.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.cervisia.desktop

%files -f %{name}.lang
%license COPYING*
%doc ChangeLog README
%{_kf5_bindir}/cervisia
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_qtplugindir}/kf5/parts/cervisiapart.so
%{_kf5_datadir}/applications/org.kde.cervisia.desktop
%{_kf5_metainfodir}/org.kde.cervisia.appdata.xml
%{_kf5_datadir}/config.kcfg/cervisiapart.kcfg
%{_kf5_datadir}/dbus-1/interfaces/org.kde.cervisia5.*.xml
%{_mandir}/man1/cervisia*
%{_kf5_bindir}/cvsaskpass
%{_kf5_bindir}/cvsservice5
%{_kf5_datadir}/knotifications5/cervisia.notifyrc
%{_kf5_datadir}/kservices5/org.kde.cvsservice5.desktop
%{_kf5_datadir}/kxmlgui5/cervisia/
%{_kf5_datadir}/kxmlgui5/cervisiapart/

%changelog
%autochangelog
