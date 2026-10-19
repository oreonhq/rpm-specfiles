%global source0_hash f8093d14ad063904b7a2e24b95c347ed79212e29438158dbeebb14de9fe79fdf
Name:           quake3
Version:        1.36
Release:        1%{?dist}
Summary:        Quake 3 Arena engine (ioquake3 version)
License:        GPL-2.0-or-later
URL:            http://ioquake3.org/
Source0:        %{name}-%{version}-svn2102.tar.bz2
Source1:        %{name}-demo.sh
Source2:        %{name}.autodlrc
Source3:        %{name}.desktop
Source4:        %{name}.png
Source5:        %{name}-update.sh
Source6:        %{name}-update.autodlrc
Source7:        urbanterror.sh
Source8:        urbanterror.autodlrc
Source9:        urbanterror.desktop
Source10:       urbanterror.png
Source11:       worldofpadman.sh
Source12:       worldofpadman.autodlrc
Source13:       worldofpadman.desktop
Source14:       wop.png
Source15:       jpeg_memsrc.h
Source16:       jpeg_memsrc.c
Source17:       %{name}.appdata.xml
Source18:       urbanterror.appdata.xml
Source19:       worldofpadman.appdata.xml
Source20:       wop.svg
Patch0:         quake3-1.36-syslibs.patch
Patch1:         quake3-1.34-rc4-demo-pak.patch
Patch2:         0011-Double-the-maximum-number-of-cvars.patch
Patch3:         0012-Increase-the-command-buffer-from-16K-to-128K-followi.patch
Patch4:         quake3-1.36-build.patch
Patch5:         quake3-fastcall.patch
Patch6:         quake3-aarch64.patch
Patch7:         quake3-1.36-unaligned-qvm.patch
%ifarch %{ix86} x86_64
%endif
Requires:       autodownloader tar
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libXt-devel
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  openal-soft-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
This package contains the enhanced opensource ioquake3 version of the Quake 3
Arena engine. This engine can be used to play a number of games based on this
engine, below is an (incomplete list):

* OpenArena, Free, Open Source Quake3 like game, recommended!
  (packagename: openarena)

* Urban Terror, gratis, but not Open Source FPS best be described as a
  Hollywood tactical shooter, a downloader and installer including an
  application menu entry is available in the urbanterror package.

* World of Padman, gratis, but not Open Source Comic FPS, a downloader and
  installer including an application menu entry is available in the
  worldofpadman package.

* Quake3 Arena, the original! A downloader and installer for the gratis, but
  not Open Source demo, including an application menu entry is available in
  the quake3-demo package.
  
  If you own a copy of quake 3, you will need to copy pak0.pk3 from the
  original CD-ROM and your q3key to /usr/share/quake3/baseq3 or ~/.q3a/baseq3.
  Also copy the pak?.pk3 files from the original 1.32 Quake 3 Arena point
  release there if you have them available or run quake3-update to download
  them for you.

%package demo
Summary:        Quake 3 Arena tournament 3D shooter game demo installer
Requires:       quake3 = %{version}-%{release}
Requires:       hicolor-icon-theme opengl-games-utils unzip
Obsoletes:      quake3 <= 1.34-0.4.rc4.fc9
%description demo
Quake 3 Arena tournament 3D shooter game demo installer. The Quake3 engine is
Open Source and as such is available as part of Fedora. The original Quake3
datafiles however are not Open Source and thus are not available as part of
Fedora. There is a gratis, but not Open Source demo available on the internet.

This package installs an applications menu entry for playing the Quake3 Arena
demo. The first time you click this menu entry, it will offer to download and
install the Quake 3 demo datafiles for you.

%package -n urbanterror
Summary:        FPS best be described as a Hollywood tactical shooter
URL:            http://www.urbanterror.net/
Requires:       quake3 = %{version}-%{release}
Requires:       hicolor-icon-theme opengl-games-utils unzip
%description -n urbanterror
Urban Terror could best be described as a Hollywood tactical shooter; it is
realism based to a certain extent (environments/weapons/player models), but
also goes by the motto "fun over realism" (fast gameplay and lots of action).
This combination of reality and action results in a very unique, enjoyable
and addictive game.

Urban Terror uses the GPL licensed ioquake3 engine, however the Urban Terror
datafiles are not freely redistributable. This package will install an Urban
Terror menu entry, which will automatically download the necessary datafiles
(2GB!) the first time you start Urban Terror.

%package -n worldofpadman
Summary:        World Of Padman - Comic 3D-Shooter
URL:            http://padworld.myexp.de/
Requires:       quake3 = %{version}-%{release}
Requires:       hicolor-icon-theme opengl-games-utils tar gzip
%description -n worldofpadman
World of Padman (WoP) is a first-person shooter computer game available in
both English and German. The idea is based on the Padman comic strip for the
magazine PlayStation Games created by the professional cartoon artist Andreas
'ENTE' Endres, who is also the man who made many of the maps included with the
game in 1998. Most of the maps in the game are lilliput style.

World of Padman uses the GPL licensed ioquake3 engine, however the Wop data-
files are not freely redistributable. This package will install a World of
Padman menu entry, which will automatically download the necessary datafiles
(1GB!) the first time you start World of Padman.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
# Add jpeg_memsrc
cp -p %{SOURCE15} %{SOURCE16} ./code/renderer/

%build

make %{?_smp_mflags} \
    OPTIMIZE="$RPM_OPT_FLAGS -fno-strict-aliasing" \
    DEFAULT_BASEDIR=%{_datadir}/%{name} USE_CODEC_VORBIS=1 \
    USE_LOCAL_HEADERS=0 BUILD_GAME_SO=0 GENERATE_DEPENDENCIES=0 \
    USE_INTERNAL_SPEEX=0 USE_INTERNAL_ZLIB=0 USE_INTERNAL_JPEG=0 \
    BUILD_CLIENT_SMP=1 CROSS_COMPILING=1
appstream-util validate-relax --nonet %{SOURCE17} %{SOURCE18} %{SOURCE19}
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 build/release-linux-*/ioquake3.* \
  $RPM_BUILD_ROOT%{_bindir}/quake3
install -m 755 build/release-linux-*/ioquake3-smp.* \
  $RPM_BUILD_ROOT%{_bindir}/quake3-smp
install -m 755 build/release-linux-*/ioq3ded.* \
  $RPM_BUILD_ROOT%{_bindir}/q3ded
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/quake3-demo
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/quake3-update
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/urbanterror
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755 %{SOURCE11} $RPM_BUILD_ROOT%{_bindir}/worldofpadman
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE9}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE13}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE17} $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE18} $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE19} $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE10} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE14} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE20} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
%oreon_autofiles urbanterror usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles worldofpadman usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n quake3-demo -f %{oreon_filedir}/quake3-demo.list
%files -n urbanterror -f %{oreon_filedir}/urbanterror.list
%files -n worldofpadman -f %{oreon_filedir}/worldofpadman.list

%changelog

%autochangelog
