
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    dolphin-plugins
Summary: Dolphin plugins
Version: 25.12.3
Release:	2%{?dist}

License: GPL-2.0-or-later
URL:     https://invent.kde.org/sdk/%{name}
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  dolphin-devel >= %{maj_ver_kf6}.%{min_ver_kf6}
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6DBus)

Requires:       dolphin >= %{maj_ver_kf6}.%{min_ver_kf6}


%description
Dolphin integration for revision control systems, Dropbox, and disk images.


%prep
%autosetup


%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_metainfodir}/org.kde.dolphin-plugins.metainfo.xml
%{_kf6_datadir}/qlogging-categories6/dolphingit.categories
%dir %{_kf6_qtplugindir}/dolphin/
%dir %{_kf6_qtplugindir}/dolphin/vcs/
%{_kf6_qtplugindir}/dolphin/vcs/fileviewbazaarplugin.so
%{_kf6_qtplugindir}/dolphin/vcs/fileviewdropboxplugin.so
%{_kf6_qtplugindir}/dolphin/vcs/fileviewgitplugin.so
%{_kf6_qtplugindir}/dolphin/vcs/fileviewsvnplugin.so
%{_kf6_qtplugindir}/dolphin/vcs/fileviewhgplugin.so
%{_kf6_plugindir}/kfileitemaction/mountisoaction.so
%{_kf6_plugindir}/kfileitemaction/makefileactions.so
%{_kf6_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_kf6_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg
%{_kf6_datadir}/config.kcfg/fileviewhgpluginsettings.kcfg


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
