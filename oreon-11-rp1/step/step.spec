
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    step
Summary: Interactive Physics Simulator 
Version: 25.12.3
Release: 1%{?dist}

License: GPL-2.0-or-later
URL:     https://invent.kde.org/edu/%{name}
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Plotting)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)

BuildRequires: cmake(Qt6Xml) 
BuildRequires: cmake(Qt6Svg) 
BuildRequires: cmake(Qt6OpenGL) 


BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(libqalculate)

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-qt

## unpackaged files
# omit bundled copies of python-(mwclient,simplejson)
rm -frv %{buildroot}%{_kf6_datadir}/parley/plugins/mwclient/
rm -fv %{buildroot}%{_kf6_datadir}/locale/*/LC_SCRIPTS/step/*.js


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/knsrcfiles/%{name}*.knsrc
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/actions/*
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/mime/packages/org.kde.%{name}.xml


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
