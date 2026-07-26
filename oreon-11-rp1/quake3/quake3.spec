%global source0_hash f8093d14ad063904b7a2e24b95c347ed79212e29438158dbeebb14de9fe79fdf

Name:           quake3
Version:        1.36
Release:        50.svn2102%{?dist}
Summary:        Quake 3 Arena engine (ioquake3 version)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://ioquake3.org/
# to regenerate (note included systemlib copies are removed for size, lcc
# is removed as it is not Free software):
# svn co svn://svn.icculus.org/quake3/tags/%%{version} %%{name}-%%{version}
# pushd %%{name}-%%{version}
# rm -fr `find -name .svn` code/AL code/SDL12 code/libcurl code/libs
# rm -fr code/jpeg-8c code/zlib code/libspeex code/tools/lcc
# popd
# tar cvfj %%{name}-%%{version}.tar.bz2 %%{name}-%%{version}
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
# Note this is for wop 1.5, 1.6 is available but that needs a custom engine
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
# patches from Debian for openarena compatibility (increase some buffer sizes)
Patch2:         0011-Double-the-maximum-number-of-cvars.patch
Patch3:         0012-Increase-the-command-buffer-from-16K-to-128K-followi.patch
# big-endian build fix
Patch4:         quake3-1.36-build.patch
Patch5:         quake3-fastcall.patch
Patch6:         quake3-aarch64.patch
# For urban-terror 4.2
Patch7:         quake3-1.36-unaligned-qvm.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL-devel libXt-devel openal-soft-devel libjpeg-devel
BuildRequires:  speex-devel speexdsp-devel libvorbis-devel curl-devel
BuildRequires:  zlib-devel desktop-file-utils libappstream-glib
%ifarch %{ix86} x86_64
BuildRequires:  nasm
%endif
# for quake3-update
Requires:       autodownloader tar

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
# quake3-demo used to be part of the quake3 package, make sure that people
# who have the old version with the demo included don't all of a sudden have
# the demo menu entry disappear.
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
# the CROSS_COMPILING=1 is a hack to not build q3cc and qvm files
# since we've stripped out q3cc as this is not Free Software.
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

# below is the desktop file and icon stuff.
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

%files
%doc BUGS ChangeLog id-readme.txt md4-readme.txt NOTTODO README TODO
%license COPYING.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-smp
%{_bindir}/%{name}-update
%{_bindir}/q3ded
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}-update.autodlrc

%files demo
%{_bindir}/%{name}-demo
%{_datadir}/%{name}/%{name}.autodlrc
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%files -n urbanterror
%{_bindir}/urbanterror
%{_datadir}/%{name}/urbanterror.autodlrc
%{_datadir}/appdata/urbanterror.appdata.xml
%{_datadir}/applications/urbanterror.desktop
%{_datadir}/icons/hicolor/128x128/apps/urbanterror.png

%files -n worldofpadman
%{_bindir}/worldofpadman
%{_datadir}/%{name}/worldofpadman.autodlrc
%{_datadir}/appdata/worldofpadman.appdata.xml
%{_datadir}/applications/worldofpadman.desktop
%{_datadir}/icons/hicolor/32x32/apps/wop.png
%{_datadir}/icons/hicolor/scalable/apps/wop.svg

%changelog
%autochangelog
