

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    khangman
Summary: Hangman game 
Version: 25.12.3
Release:	2%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/edu/%{name}
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Svg)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6DocTools)

BuildRequires: cmake(LibKEduVocDocument)
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkeduvocdocument-devel >= %{majmin_ver}

Requires: dustin-dustismo-roman-fonts
Requires: dustin-domestic-manners-fonts
Requires: kdeedu-data
# qml deps
Requires: kf6-knewstuff%{?_isa}
Requires: qt6-qt5compat%{?_isa}
Requires: qt6-qtmultimedia%{?_isa}

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-man --with-qt

## unpackaged files
# omit bundled dustismo roman font
rm -fv %{buildroot}%{_kf6_datadir}/khangman/fonts/Dustismo_Roman.ttf
# omit bundled domestic manners font
rm -fv %{buildroot}%{_kf6_datadir}/khangman/fonts/Domestic_Manners.ttf
# bug, harmattan icon should not be installed (when harmattan build is off)
rm -vf %{buildroot}%{_kf6_datadir}/icons/hicolor/*/apps/khangman-harmattan.*


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop ||:


%files -f %{name}.lang
%license COPYING*
%doc README
%{_kf6_bindir}/%{name}*
%{_kf6_datadir}/knsrcfiles/%{name}.knsrc
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_mandir}/man6/%{name}.6*


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
