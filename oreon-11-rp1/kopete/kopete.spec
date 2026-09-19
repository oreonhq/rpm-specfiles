%global source0_hash 0af87805f0c256ec3e5615e3ec70720ee09d0dbdc0a36b53813f3078a91b8e31

Name:    kopete
Summary: Instant messenger
Version: 23.08.5
Release: 4%{?dist}

License: GPL-2.0-or-later AND LGPL-2.1-only
URL:     https://www.kde.org/applications/internet/kopete/

Source0: http://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches
Patch100: kopete-17.08.3-openssl-1.1.patch

BuildRequires: gcc-c++ gcc
BuildRequires: desktop-file-utils

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
# Introduced here: https://src.fedoraproject.org/rpms/kde-filesystem/c/3cc17949d085bef5476638f2fbade0f19dbcea32?branch=rawhide
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
BuildRequires: kde4-filesystem
%endif

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Emoticons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5TextEditor)
BuildRequires: cmake(KF5TextEditTextToSpeech)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5KDELibs4Support)

BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)

BuildRequires: cmake(Phonon4Qt5)

BuildRequires: cmake(KF5Contacts)
BuildRequires: cmake(KF5IdentityManagement)
BuildRequires: cmake(KF5Libkleo)

BuildRequires: cmake(KF5DNSSD)

BuildRequires: cmake(Qca-qt5)

BuildRequires: giflib-devel
BuildRequires: perl-generators

BuildRequires: pkgconfig(alsa)
BuildRequires: openslp-devel
BuildRequires: pkgconfig(libgadu) >= 1.8.0

BuildRequires: openssl-devel
BuildRequires: pkgconfig(jasper)
BuildRequires: pkgconfig(libidn)
BuildRequires: pkgconfig(libotr)
BuildRequires: pkgconfig(libv4l2)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: libvncserver-devel
BuildRequires: openldap-devel

Obsoletes: kopete-cryptography < %{version}-%{release}

Provides: bundled(iris) = 2.0.0

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: qca-qt5-ossl%{?_isa}

Conflicts: kde-l10n < 17.08.3-5

%description
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# disable oscar support due to FTBFS,
# https://bugs.kde.org/show_bug.cgi?id=393372
%{cmake_kf5} \
  -DWITH_wlm:BOOL=OFF
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/org.kde.kopete.desktop

%files -f %{name}.lang
%license COPYING*
%{_kf5_sysconfdir}/xdg/kopete*
%{_kf5_bindir}/kopete
%{_kf5_bindir}/winpopup-*
%{_kf5_datadir}/applications/org.kde.kopete.desktop
%{_kf5_metainfodir}/org.kde.kopete.appdata.xml
%{_kf5_datadir}/config.kcfg/*.kcfg
%{_kf5_datadir}/kopete/
%{_kf5_datadir}/kopete_history/
%{_kf5_datadir}/sounds/Kopete_*
%{_kf5_datadir}/kconf_update/kopete*
%{_kf5_datadir}/knotifications5/kopete.*
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/*.protocol
%{_kf5_datadir}/kservices5/kconfiguredialog/kopete_*
%{_kf5_datadir}/kservicetypes5/kopete*.desktop
%{_kf5_datadir}/kxmlgui5/kopete*/
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/icons/oxygen/*/*/*
%{_kf5_datadir}/qlogging-categories5/kopete.categories

%files libs
%{_kf5_libdir}/libkopete*.so.*
%{_kf5_libdir}/liboscar.so.*
%{_kf5_libdir}/libqgroupwise.so
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/accessible/chatwindowaccessiblewidgetfactory.so

%files devel
%{_includedir}/kopete/
%{_kf5_libdir}/libkopete*.so
%{_kf5_libdir}/liboscar.so
%{_kf5_datadir}/dbus-1/interfaces/org.kde.*.xml

%changelog
%autochangelog
