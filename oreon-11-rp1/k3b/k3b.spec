# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    k3b
Summary: CD/DVD/Blu-ray burning application
Epoch:   1
Version: 25.12.3
Release:	2%{?dist}

License: GPL-2.0-or-later
URL:     https://invent.kde.org/multimedia/k3b

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches
# https://bugzilla.redhat.com/show_bug.cgi?id=2212471
Patch10: prefer-wodim.patch

## downstream patches

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Core5Compat)

%ifarch %{qt6_qtwebengine_arches}
BuildRequires: cmake(Qt6WebEngineWidgets)
%endif

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KCddb6)

BuildRequires: ffmpeg-free-devel
BuildRequires: lame-devel
BuildRequires: libmpcdec-devel
BuildRequires: pkgconfig(dvdread)
BuildRequires: pkgconfig(flac++)

BuildRequires: pkgconfig(mad)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(vorbisenc) pkgconfig(vorbisfile)
BuildRequires: pkgconfig(taglib)

Conflicts: k3b-extras-freeworld < 1:17.03

Obsoletes: k3b-common < 1:17.03
Provides:  k3b-common = %{epoch}:%{version}-%{release}

Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

Requires: cdrdao
# cdrecord compatibility layer from libburn, I know it's newer, but k3b
# hangs when trying to use it, and installs as same priority as wodim (50)
# do definitely confusing in the least, dropping for now -- rex
#Requires: cdrskin
Requires: dvd+rw-tools
## BR these runtime dependencies for sanitiy (for now) -- rex
## use real packages, not virtual provides since they have
## been recently removed, https://bugzilla.redhat.com/1599009
# mkisofs
BuildRequires: genisoimage
Requires: genisoimage
# cdrecord
BuildRequires: wodim
Requires: wodim

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
%autosetup -p1


%build
%cmake_kf6 \
  -DQT_MAJOR_VERSION=6 \
  -DK3B_BUILD_FFMPEG_DECODER_PLUGIN:BOOL=ON \
  -DK3B_BUILD_LAME_ENCODER_PLUGIN:BOOL=ON \
  -DK3B_BUILD_MAD_DECODER_PLUGIN:BOOL=ON

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.k3b.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.k3b.desktop


%files -f %{name}.lang
%doc README*
%license LICENSES/*
%{_kf6_bindir}/k3b
%{_kf6_metainfodir}/org.kde.k3b.appdata.xml
%{_kf6_datadir}/applications/org.kde.k3b.desktop
%{_kf6_datadir}/knotifications6/k3b.*
%{_datadir}/knsrcfiles/k3btheme.knsrc
%{_kf6_datadir}/konqsidebartng/virtual_folders/services/*.desktop
%{_kf6_datadir}/solid/actions/k3b*.desktop
%{_kf6_datadir}/mime/packages/x-k3b.xml
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/k3b/
%{_kf6_datadir}/kio/servicemenus/*
%{_kf6_datadir}/qlogging-categories6/k3b.categories
%{_libexecdir}/kf6/kauth/k3bhelper
%{_datadir}/dbus-1/system-services/org.kde.k3b.service
%{_datadir}/dbus-1/system.d/org.kde.k3b.conf
%{_datadir}/polkit-1/actions/org.kde.k3b.policy

%files libs
%{_kf6_libdir}/libk3bdevice.so.*
%{_kf6_libdir}/libk3blib.so.*
%{_kf6_qtplugindir}/k3b_plugins
%{_kf6_plugindir}/kio/videodvd.so

%files devel
%{_includedir}/k3b*.h
%{_kf6_libdir}/libk3bdevice.so
%{_kf6_libdir}/libk3blib.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
