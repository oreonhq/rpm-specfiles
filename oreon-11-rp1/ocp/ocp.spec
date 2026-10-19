%global source0_hash b20885d0f1b8bbc0f0dcb91b80c0aa447e811727fd7158b422751d0279b6ab04
%global commit d9d81d02d47499d0a7c96abb6a92fb152a118a58
%global commitdate 20260208
%global gittag v3.1.3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		ocp
Version:	3.1.3%{?snapshot:^%{commitdate}git%{shortcommit}}
Release:        1%{?dist}
Summary:        Open Cubic Player for MOD/S3M/XM/IT/MIDI music files
License:	GPL-2.0-or-later AND CC-BY-3.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GFDL-1.1-or-later AND X11 AND BSD-2-Clause AND BSD-3-Clause AND Zlib
URL:		https://stian.cubic.org/project-ocp.php
%if 0%{?snapshot}
Source0:        https://stian.cubic.org/%{name}/%{name}-%{version}.tar.bz2
%else
%endif
Source1:	ftp://ftp.cubic.org/pub/player/gfx/opencp25image1.zip
Source2:	ftp://ftp.cubic.org/pub/player/gfx/opencp25ani1.zip
Source3:	ocp-git-snapshot.sh
Source4:	ocp-bundled-versions.sh
Patch0:		ocp-0.2.106-ini-optimize.patch
Patch1:		ocp-0.2.106-ini-rompaths.patch
Patch2:		ocp-3.1.1-timidity-config-file.patch
Requires:	hicolor-icon-theme
Requires:	unifont-fonts
Recommends:	soundfont2-default
Provides:	bundled(timidity++) = 2.15.0
Provides:	bundled(libsidplayfp) = 3.0.0a
Provides:	bundled(adplug) = 2.4.1-beta
Provides:	bundled(libbinio) = 1.5
Provides:	bundled(reSIDfp) = 3.1.0
Provides:	bundled(libexsid) = 2.1
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  ancient-devel
BuildRequires:  bzip2-devel
BuildRequires:  cjson-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flac-devel
BuildRequires:  freetype-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libdiscid-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmad-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-interpreter
BuildRequires:  texinfo
BuildRequires:  unifont-fonts
BuildRequires:  unzip
BuildRequires:  xa
BuildRequires:  zlib-devel
# /oreon:deps
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
	   --with-unifont-otf=/usr/share/fonts/unifont/unifont.otf \
	   --with-unifont-csur-otf=/usr/share/fonts/unifont/unifont_csur.otf \
	   --with-unifont-upper-otf=/usr/share/fonts/unifont/unifont_upper.otf \
	   --with-dumptools \
	   --without-update-mime-database \
	   --without-update-desktop-database \
	   --docdir=%{_pkgdocdir} \
%global _smp_mflags -j1
%make_build
%install
mkdir -p %{buildroot}/etc
%make_install
mv %{buildroot}%{_datadir}/%{name}/etc/ocp.ini %{buildroot}/etc/ocp.ini
rmdir %{buildroot}%{_datadir}/%{name}/etc
rm -f %{buildroot}/%{_infodir}/dir
mv %{buildroot}%{_datadir}/applications/*opencubicplayer.desktop \
   %{buildroot}%{_datadir}/applications/ocp.desktop
desktop-file-install --add-category="Midi" \
		     --dir=%{buildroot}%{_datadir}/applications \
		     --delete-original \
		     %{buildroot}%{_datadir}/applications/ocp.desktop
cp -p CPPIC*.TGA CPANI*.DAT %{buildroot}%{_datadir}/%{name}/data
rm -f %{buildroot}%{_pkgdocdir}/COPYING
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
