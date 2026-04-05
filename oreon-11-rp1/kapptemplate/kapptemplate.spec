
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kapptemplate
Summary: KDE Template generator
Version: 25.12.3
Release:	2%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://apps.kde.org/kapptemplate/
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6IconThemes)

%description
Factory for the easy creation of KDE/Qt components and programs


%prep
%autosetup -p1


%build
%cmake_kf6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop ||:


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/kdevappwizard/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_kf6_datadir}/qlogging-categories6/%{name}.*


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
