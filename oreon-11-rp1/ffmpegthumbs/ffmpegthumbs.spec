
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    ffmpegthumbs
Version: 25.12.3
Release:	2%{?dist}
Summary: KDE ffmpegthumbnailer service

License: GPL-2.0-or-later
URL:     https://apps.kde.org/%{name}/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Config)
BuildRequires: ffmpeg-free-devel

Provides: kffmpegthumbnailer = %{version}-%{release}

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml


%files
%license LICENSES/GPL-2.0-or-later.txt
%{_kf6_plugindir}/thumbcreator/ffmpegthumbs.so
%{_kf6_datadir}/config.kcfg/ffmpegthumbnailersettings5.kcfg
%{_kf6_datadir}/qlogging-categories6/ffmpegthumbs.categories
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
