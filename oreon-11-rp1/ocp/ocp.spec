%global source0_hash 3695aab527df75ff41c397c91b21e84a878dbf683947f3c9fbcfee0e9c50d808

#global snapshot 0
%global commit d9d81d02d47499d0a7c96abb6a92fb152a118a58
%global commitdate 20260208
%global gittag v3.1.3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		ocp
Version:	3.1.3%{?snapshot:^%{commitdate}git%{shortcommit}}
Release:	1%{?dist}
Summary:	Open Cubic Player for MOD/S3M/XM/IT/MIDI music files

# Main ocp source is GPL-2.0-or-later.
# Graphics and animations are CC-BY-3.0.
License:	GPL-2.0-or-later AND CC-BY-3.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GFDL-1.1-or-later AND X11 AND BSD-2-Clause AND BSD-3-Clause AND Zlib
URL:		https://stian.cubic.org/project-ocp.php
%if 0%{?snapshot}
# Since this project uses git submodules and Github's auto-archive
# feature doesn't archive the submodules, you need to create a git
# snapshot tarball manually with ocp-git-snapshot.sh.
Source0:	ocp-%{commit}.tar.bz2
%else
Source0:	https://stian.cubic.org/ocp/ocp-%{version}.tar.bz2
%endif
Source1:	ftp://ftp.cubic.org/pub/player/gfx/opencp25image1.zip
Source2:	ftp://ftp.cubic.org/pub/player/gfx/opencp25ani1.zip
Source3:	ocp-git-snapshot.sh
Source4:	ocp-bundled-versions.sh
Patch0:		ocp-0.2.106-ini-optimize.patch
Patch1:		ocp-0.2.106-ini-rompaths.patch
Patch2:		ocp-3.1.1-timidity-config-file.patch

BuildRequires:	alsa-lib-devel
BuildRequires:	bzip2-devel
BuildRequires:	cjson-devel
BuildRequires:	desktop-file-utils
BuildRequires:	flac-devel
BuildRequires:	freetype-devel
BuildRequires:	game-music-emu-devel
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	ancient-devel
BuildRequires:	libdiscid-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXxf86vm-devel
BuildRequires:	make
BuildRequires:	ncurses-devel
BuildRequires:	perl-interpreter
BuildRequires:	SDL2-devel
BuildRequires:	texinfo
BuildRequires:	unifont-fonts
BuildRequires:	unzip
BuildRequires:	xa
BuildRequires:	zlib-devel

# For the hicolor icon directories
Requires:	hicolor-icon-theme
Requires:	unifont-fonts

# Recommend a soundfont for MIDI files
Recommends:	soundfont2-default

# Bundled code
# AC_INIT([TiMidity++],[2.15.0],[timidity-talk@lists.sourceforge.net],[TiMidity++])
Provides:	bundled(timidity++) = 2.15.0
# m4_define([lib_major], [3]) m4_define([lib_minor], [0]) m4_define([lib_level], [0a]) m4_define([lib_version], [lib_major.lib_minor.lib_level]) AC_INIT([libsidplayfp],[lib_version],[],[],[https://github.com/libsidplayfp/libsidplayfp/])
Provides:	bundled(libsidplayfp) = 3.0.0a
# AC_INIT([adplug], [2.4.1-beta])
Provides:	bundled(adplug) = 2.4.1-beta
# AC_INIT([binio],[1.5],[dn.tlp@gmx.net],[libbinio])
# const char* residfpII_version_string = "3.1.0";
Provides:	bundled(libbinio) = 1.5
Provides:	bundled(reSIDfp) = 3.1.0
# AC_INIT([libexsid], [2.1], [], [], [https://github.com/libsidplayfp/exsid-driver])
Provides:	bundled(libexsid) = 2.1

%description
Open Cubic Player is a music file player ported from DOS that supports
Amiga MOD module formats and many variants, such as MTM, STM, 669,
S3M, XM, and IT.  It is also able to render MIDI files using sound
patches and play SID, OGG Vorbis, FLAC, and WAV files.  OCP provides a
nice text-based interface with several text-based and graphical
visualizations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?snapshot}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif
unzip %{SOURCE1}
mv license.txt license-images.txt
unzip %{SOURCE2}
mv license.txt license-videos.txt

%build
%configure --with-x11 \
	   --with-alsa \
	   --without-coreaudio \
	   --without-oss \
	   --with-lzw \
	   --with-lzh \
	   --with-libgme \
	   --with-flac \
	   --without-sdl \
	   --with-sdl2 \
	   --with-mad \
	   --with-libiconv=auto \
	   --with-timidity-default-path=/etc \
%if 0%{?fedora} < 38
	   --with-unifontdir-ttf=/usr/share/fonts/unifont \
	   --without-unifont-csur-ttf \
%else
	   --with-unifont-otf=/usr/share/fonts/unifont/unifont.otf \
	   --with-unifont-csur-otf=/usr/share/fonts/unifont/unifont_csur.otf \
	   --with-unifont-upper-otf=/usr/share/fonts/unifont/unifont_upper.otf \
%endif
	   --with-dumptools \
	   --without-update-mime-database \
	   --without-update-desktop-database \
	   --docdir=%{_pkgdocdir} \
#	   --with-debug
# Makefiles are not SMP-clean
%global _smp_mflags -j1
%make_build

%install
mkdir -p %{buildroot}/etc
%make_install

# mv config to /etc (ocp will search here if it isn't found in the original location)
mv %{buildroot}%{_datadir}/%{name}/etc/ocp.ini %{buildroot}/etc/ocp.ini
rmdir %{buildroot}%{_datadir}/%{name}/etc

# remove info/dir
rm -f %{buildroot}/%{_infodir}/dir

# rename desktop file to name.desktop to match packaging guidelines
mv %{buildroot}%{_datadir}/applications/*opencubicplayer.desktop \
   %{buildroot}%{_datadir}/applications/ocp.desktop
desktop-file-install --add-category="Midi" \
		     --dir=%{buildroot}%{_datadir}/applications \
		     --delete-original \
		     %{buildroot}%{_datadir}/applications/ocp.desktop

# install images and animations
cp -p CPPIC*.TGA CPANI*.DAT %{buildroot}%{_datadir}/%{name}/data

# remove COPYING from buildroot/docdir as it will be installed as a license file below
rm -f %{buildroot}%{_pkgdocdir}/COPYING

%files
%license COPYING license-images.txt license-videos.txt
# install already installs the docs here for us
%doc %{_pkgdocdir}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_bindir}/ocp
%{_bindir}/ocp-curses
%{_bindir}/ocp-sdl2
%{_bindir}/ocp-vcsa
%{_bindir}/ocp-x11
%{_bindir}/dump*
%{_infodir}/ocp.info*
%{_mandir}/man1/ocp.1*
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/64x64/apps/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/*ocp.desktop
%{_datadir}/mime/packages/opencubicplayer.xml
%config(noreplace) /etc/ocp.ini

%changelog
%autochangelog
