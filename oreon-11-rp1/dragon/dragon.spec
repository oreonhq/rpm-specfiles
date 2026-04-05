
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    dragon
Summary: Media player
Version: 25.12.3
Release:	2%{?dist}

# code: KDE e.V. may determine that future GPL versions are accepted
# docs: GFDL
License: ( GPL-2.0-only OR GPL-3.0-only ) AND GFDL-1.2-or-later
URL:     https://apps.kde.org/dragonplayer/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

BuildRequires: desktop-file-utils
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6CorePrivate)

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Kirigami)

BuildRequires: cmake(Phonon4Qt6)
BuildRequires: pkgconfig(libavcodec)

BuildRequires: libappstream-glib

Provides:  dragonplayer = %{version}-%{release}

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-man


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.dragonplayer.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.dragonplayer.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/dragon
%{_kf6_datadir}/applications/org.kde.dragonplayer.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/dragonplayer.*
%{_kf6_qmldir}/org/kde/dragon/
%{_kf6_metainfodir}/org.kde.dragonplayer.appdata.xml


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
