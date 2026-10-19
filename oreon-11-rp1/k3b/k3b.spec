%global source0_hash 84ca4a064553587e7c6a93ff9b29a36bf05c07dd08269bea43f1ab5ff92374f3
%global stable_kf6 stable
%global _changelog_trimtime %(date +%s -d "1 year ago")
Name:    k3b
Summary:        CD/DVD/Blu-ray burning application
Epoch:   1
Version: 26.08.1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://invent.kde.org/multimedia/k3b
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch10: prefer-wodim.patch
%ifarch %{qt6_qtwebengine_arches}
%endif
Conflicts: k3b-extras-freeworld < 1:17.03
Obsoletes: k3b-common < 1:17.03
Provides:  k3b-common = %{epoch}:%{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: cdrdao
Requires: dvd+rw-tools
Requires: genisoimage
Requires: wodim
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KCddb6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  ffmpeg-free-devel
BuildRequires:  gcc-c++
BuildRequires:  genisoimage
BuildRequires:  kf6-rpm-macros
BuildRequires:  lame-devel
BuildRequires:  libappstream-glib
BuildRequires:  libmpcdec-devel
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  wodim
# /oreon:deps
%description
K3b provides a comfortable user interface to perform most CD/DVD
burning tasks. While the experienced user can take influence in all
steps of the burning process the beginner may find comfort in the
automatic settings and the reasonable k3b defaults which allow a quick
start.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Files for the development of applications which will use %{name} 
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
  -DQT_MAJOR_VERSION=6 \
  -DK3B_BUILD_FFMPEG_DECODER_PLUGIN:BOOL=ON \
  -DK3B_BUILD_LAME_ENCODER_PLUGIN:BOOL=ON \
  -DK3B_BUILD_MAD_DECODER_PLUGIN:BOOL=ON
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.k3b.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.k3b.desktop
%files -f %{oreon_filedir}/main.list
%files -n k3b-libs -f %{oreon_filedir}/k3b-libs.list
%files -n k3b-devel -f %{oreon_filedir}/k3b-devel.list

%changelog

%autochangelog
