
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    filelight
Summary: Graphical disk usage statistics
Epoch:   1
Version: 25.12.3
Release: 1%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
License: GPL-2.0-only OR GPL-3.0-only
URL:     https://utils.kde.org/projects/filelight

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6Crash)

BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Widgets)

# Runtime Deps
Requires: kf6-qqc2-desktop-style
Requires: kf6-kcoreaddons
Requires: kf6-kirigami
Requires: kf6-kirigami-addons
Requires: kf6-kquickcharts


%description
Filelight allows you to quickly understand exactly where your diskspace
is being used by graphically representing your file system.


%prep
%autosetup


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license LICENSES/*
%doc AUTHORS README*
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_bindir}/filelight
%{_kf6_datadir}/applications/org.kde.filelight.desktop
%{_kf6_metainfodir}/org.kde.filelight.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/*/*filelight.*
%{_sysconfdir}/xdg/filelightrc
%{_kf6_datadir}/kio/servicemenus/filelight.desktop

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
