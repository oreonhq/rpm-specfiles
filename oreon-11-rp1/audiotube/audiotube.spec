%global kf6_min_version 5.240.0


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           audiotube
Version:        25.12.3
Release:	2%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        AudioTube can search YouTube Music, list albums and artists, play automatically generated playlists, albums and allows to put your own playlist together.
Url:            https://apps.kde.org/audiotube/
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# Upstream
# Fails to build on F41 (Lower Qt version)
Patch0:         e56b2b4cf82f5770da307b7ad1c345df94c4fc1f.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules >= %{kf6_min_version}
BuildRequires:  kf6-rpm-macros      >= %{kf6_min_version}

BuildRequires: pybind11-devel
BuildRequires: python3-devel
BuildRequires: python3-ytmusicapi
BuildRequires: yt-dlp

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6DBus)

BuildRequires: cmake(KF6Kirigami)     >= %{kf6_min_version}
BuildRequires: cmake(KF6I18n)         >= %{kf6_min_version}
BuildRequires: cmake(KF6CoreAddons)   >= %{kf6_min_version}
BuildRequires: cmake(KF6Crash)        >= %{kf6_min_version}
BuildRequires: cmake(KF6WindowSystem) >= %{kf6_min_version}
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(FutureSQL6)
BuildRequires: cmake(QCoro6Core)

Requires:   hicolor-icon-theme
Requires:   kf6-kirigami%{?_isa}
Requires:   kf6-kirigami-addons%{?_isa}
Requires:   kf6-purpose%{?_isa}
Requires:   qt6-qt5compat%{?_isa}
Requires:   qt6-qtmultimedia%{?_isa}
%if %{undefined flatpak}
# these are provided by a flatpak extension
Requires:   python3-ytmusicapi
Requires:   yt-dlp
%endif

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
