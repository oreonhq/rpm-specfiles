Name:    akregator
Summary: Feed Reader
Version: 25.12.3
Release:	2%{?dist}

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://www.kde.org/applications/internet/akregator/

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: perl-generators

BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(QGpgmeQt6)

# kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Syndication)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6DocTools)

BuildRequires: cmake(KPim6GrantleeTheme)
BuildRequires: cmake(KPim6KontactInterface)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6MessageViewer)
BuildRequires: cmake(KF6TextEditTextToSpeech)
BuildRequires: cmake(KF6TextUtils)
BuildRequires: cmake(KPim6WebEngineViewer)
BuildRequires: cmake(KPim6PimCommon)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake
BuildRequires: cmake(KF6IconThemes)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Akregator is a news feed reader. It enables you to follow news sites,
blogs and other RSS/Atom-enabled websites without the need to manually
check for updates using a web browser.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml


%files -f %{name}.lang
%license LICENSES/*
%{_datadir}/dbus-1/interfaces/org.kde.akregator.part.xml
%{_kf6_bindir}/akregator
%{_kf6_bindir}/akregatorstorageexporter
%{_kf6_datadir}/applications/org.kde.akregator.desktop
%{_kf6_datadir}/config.kcfg/akregator.kcfg
%{_kf6_datadir}/icons/hicolor/*/apps/akregator.*
%{_kf6_datadir}/icons/hicolor/*/apps/akregator_empty.png
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_metainfodir}/org.kde.akregator.appdata.xml
%{_kf6_datadir}/knotifications6/akregator.notifyrc

%files libs
%{_kf6_libdir}/libakregatorinterfaces.so.*
%{_kf6_libdir}/libakregatorprivate.so.*
%{_kf6_qtplugindir}/akregatorpart.so
%dir %{_kf6_qtplugindir}/pim6/kontact/
%{_kf6_qtplugindir}/pim6/kontact/kontact_akregatorplugin.so
%{_kf6_qtplugindir}/pim6/kcms/akregator/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
