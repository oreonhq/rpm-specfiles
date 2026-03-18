Name:    kontact
Summary: Personal Information Manager
Version: 25.12.3
Release: 1%{?dist}

# code (generally) GPLv2, docs GFDL
# Automatically converted from old format: GPLv2 and GFDL - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/pim/%{name}

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebEngineWidgets)

# kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6TextTemplate)

BuildRequires: cmake(KPim6KontactInterface)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6GrantleeTheme)
BuildRequires: cmake(KPim6PimCommon)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# core/runtime deps
Requires: kaddressbook
Requires: kmail
Requires: korganizer

%description
Kontact is the integrated solution to your personal information management
(PIM) needs. It combines well-known KDE applications like KMail, KOrganizer
and KAddressBook into a single interface to provide easy access to mail,
scheduling, address book and other PIM functionality.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%check
for f in %{buildroot}%{_kf6_datadir}/applications/*.desktop ; do
  desktop-file-validate $f
done
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_bindir}/kontact
%{_kf6_metainfodir}/org.kde.kontact.appdata.xml
%{_kf6_datadir}/applications/org.kde.kontact.desktop
%{_kf6_datadir}/config.kcfg/kontact.kcfg
%{_kf6_datadir}/messageviewer/about/default/introduction_kontact.html
%{_kf6_datadir}/messageviewer/about/default/loading_kontact.html
%{_kf6_datadir}/icons/hicolor/*/apps/kontact.*
%{_kf6_datadir}/dbus-1/services/org.kde.kontact.service

%files libs
%{_kf6_libdir}/libkontactprivate.so.*
%{_qt6_plugindir}/pim6/kcms/kontact/kcm_kontact.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
