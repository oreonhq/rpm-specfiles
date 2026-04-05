
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kdenetwork-filesharing
Summary: Network filesharing
Version: 25.12.3
Release:	2%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/network/%{name}
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


# upstream patches

BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickWidgets)

BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WidgetsAddons)

BuildRequires: cmake(packagekitqt6)
BuildRequires: cmake(QCoro6Core)

# or gets pulled in via PK at runtime
Recommends: samba
Recommends: samba-usershares

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kdenetwork-filesharing.metainfo.xml


%files -f %{name}.lang
%license LICENSES/*
%dir %{_kf6_plugindir}/propertiesdialog/
%{_kf6_plugindir}/propertiesdialog/sambausershareplugin.so
%{_kf6_plugindir}/propertiesdialog/SambaAcl.so
%{_kf6_metainfodir}/org.kde.kdenetwork-filesharing.metainfo.xml
%{_kf6_libexecdir}/kauth/authhelper
%{_kf6_datadir}/dbus-1/system-services/org.kde.filesharing.samba.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.filesharing.samba.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.filesharing.samba.policy


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
