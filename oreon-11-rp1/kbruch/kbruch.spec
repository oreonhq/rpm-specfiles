%global stable_kf6 stable

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kbruch
Summary: Practice Fractions 
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://apps.kde.org/kbruch/
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)


%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop ||:


%files -f %{name}.lang
%license LICENSES/*
#doc README
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_mandir}/man1/kbruch.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
