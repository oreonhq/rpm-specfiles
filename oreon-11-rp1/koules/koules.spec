%global source0_hash c36f93feafeebd59983bf44100240e67a84a8bacabd7ee528c93046defe4a21b

Name:           koules
Version:        1.4
Release:        49%{?dist}
Summary:        Action game with multiplayer, network and sound support

License:        GPL-2.0-or-later AND BSD-4-Clause-UC AND HPND-Netrek
URL:            http://www.ucw.cz/~hubicka/koules/
Source0:        http://www.ucw.cz/~hubicka/koules/packages/%{name}%{version}-src.tar.gz
Source1:        koules.desktop
Source2:        koules.sndsrv.linux

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  SDL2_gfx-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  imake
BuildRequires:  desktop-file-utils

Requires:       %{name}-sound%{?_isa} = %{version}-%{release}
Requires:       %{name}-x11%{?_isa}   = %{version}-%{release}

Obsoletes:      koules-svgalib < 1.4-34

# https://github.com/lkundrak/koules/tree/SDL2
Patch1:         0001-gitignore.patch
Patch2:         0002-Fix-warnings.patch
Patch3:         0003-Remove-relics.patch
Patch4:         0004-Fix-a-buffer-overflow.patch
Patch5:         0005-From-Debian-100_spelling.diff.patch
Patch6:         0006-From-Debian-050_defines.diff.patch
Patch7:         0007-We-do-not-install-manual-pages.patch
Patch8:         0008-Fix-build.patch
Patch9:         0009-Install-to-relative-location-and-look-for-the-sound-.patch
Patch10:        0010-From-Debian-106_shm_check.diff.patch
Patch11:        0011-From-Debian-107_fix_xsynchronize.diff.patch
Patch12:        0012-From-Debian-108_use_right_visual.diff.patch
Patch13:        0013-From-Debian-109_fpe_fix.diff.patch
Patch14:        0014-Set-TABSIZE-globally.patch
Patch15:        0015-io.h-no-longer-needed.patch
Patch16:        0016-DEFAULTINITPORT-is-not-defined-if-building-without-N.patch
Patch17:        0017-Fix-undefined-reference-if-building-with-net-and-wit.patch
Patch18:        0018-Fix-pointer-target-signedness.patch
Patch19:        0019-Fix-banner-placement-with-OS-2.patch
Patch20:        0020-Fix-rocketcolor-signedness.patch
Patch21:        0021-Fix-background-color-calculation.patch
Patch22:        0022-Fix-string-quoting.patch
Patch23:        0023-Fix-socket-types.patch
Patch24:        0024-Silence-warning-about-potentially-uninitialized-stru.patch
Patch25:        0025-Fix-warning-about-ambigious-if-else-s.patch
Patch26:        0026-Avoid-warnings-about-unused-labels.patch
Patch27:        0027-Get-rid-of-unused-variables-if-building-with-both-MO.patch
Patch28:        0028-Dynamically-decide-about-window-size-based-on-inform.patch
Patch29:        0029-Fix-rocketcolor-signedness.patch
Patch30:        0030-Add-SDL-support.patch
Patch31:        0031-Add-koules.sdl.6-manual.patch
Patch32:        0032-Fix-an-off-by-one-error.patch
Patch33:        0033-Drop-an-unused-variable.patch
Patch34:        0034-Make-compiler-bounds-checking-happy.patch
Patch35:        0035-Don-t-do-extern-inline.patch
Patch36:        0036-Remove-redundant-normalize-function.patch
Patch37:        0037-Allow-setting-DESTDIR-for-sdl-and-svga-installs.patch
Patch38:        0038-SDL2-build.patch
Patch39:        0039-SDL2-GFX.patch
Patch40:        0040-SDL2-input.patch
Patch41:        0041-Correct-path-to-the-sound-server.patch
Patch43:        0043-Fix-accel-type-mismatch.patch
Patch44:        0044-Fix-lastlevel-joystick-format-overflows.patch
Patch45:        0045-Fix-unused-results.patch
Patch46:        0046-Makefiles-use-cc-variable.patch
Patch48:        0048-From-Debian-110_manpage_hyphens.diff.patch
Patch49:        0049-From-Debian-111_font_unsigned_char.diff.patch
Patch50:        0050-From-Debian-112_unsigned_control.diff.patch
Patch51:        0051-From-Debian-113_spelling_fixes.diff.patch
Patch52:        0052-From-Debian-double-declaration.patch
Patch100:       0100-c23.patch
Patch101:       0101-ansi-c.patch

%description
Koules is a fast action arcade-style game.  It works in fine resolution
with cool 256 color graphics, multiplayer mode up to 5 players, full sound
and, of course, network support.  Koules is an original idea. First version
of Koules was developed from scratch by Jan Hubicka in July 1995.

%package x11
Summary:        X Window system variant of a multiplayer action game
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       xorg-x11-fonts-misc

%description x11
This package contains variant of a classic Linux arcade game with X Window
System support and can act as a network server for multiplayer game.

%package sdl
Summary:        SDL2 variant of a multiplayer action game
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description sdl
This package contains variant of a classic Linux arcade game built with SDL
library that can also act as a network server for multiplayer game.

%package sound
Summary:        Sound files for a classic Linux multiplayer action game
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pulseaudio-utils

%description sound
This package contains sound files for a classic Linux arcade game.

%global bindir          BINDIR=%{_bindir}
%global sounddir        SOUNDDIR=%{_datadir}/%{name}/sound
%global mandir          MANDIR=%{_mandir}/man6
%global libexecdir      LIBEXECDIR=%{_libexecdir}/%{name}
%global makedirs        %{bindir} %{sounddir} %{mandir} %{libexecdir}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -N
pushd %{name}%{version}
%autopatch -p1
popd

%build
# Build SDL variant
cp -a  %{name}%{version} %{name}-%{version}-sdl
%make_build -C %{name}-%{version}-sdl -f Makefile.sdl %{makedirs} \
        OPTIMIZE="%{optflags}" OPTIMIZE1="%{optflags}"

# Build X11 variant
cp -a  %{name}%{version} %{name}-%{version}-x11
pushd %{name}-%{version}-x11
echo '#define HAVEUSLEEP' >>Iconfig
xmkmf -a
%make_build %{makedirs} CCOPTIONS="%{optflags} -DONLYANSI"
popd

%install
install -d %{buildroot}%{_mandir}/man6
install -d %{buildroot}%{_datadir}/%{name}/sound
install -d %{buildroot}%{_libexecdir}/%{name}

# Install SDL variant
%make_install -C %{name}-%{version}-sdl -f Makefile.sdl INSTALLSOUND=False \
        %{makedirs}

# Install X11 variant and sound
%make_install -C %{name}-%{version}-x11 %{makedirs}
install -d %{buildroot}%{_datadir}/pixmaps
install %{name}%{version}/Icon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
desktop-file-install \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
        %{SOURCE1}

# PulseAudio wrapper for the sound server
mv %{buildroot}%{_libexecdir}/%{name}/koules.sndsrv.linux{,.bin}
cp %{SOURCE2} %{buildroot}%{_libexecdir}/%{name}/koules.sndsrv.linux

%files
%license %{name}%{version}/COPYING
%doc %{name}%{version}/ANNOUNCE
%doc %{name}%{version}/BUGS
%doc %{name}%{version}/Card
%doc %{name}%{version}/ChangeLog
%doc %{name}%{version}/Koules.FAQ
%doc %{name}%{version}/README
%doc %{name}%{version}/TODO

%files sound
%{_datadir}/%{name}
%{_libexecdir}/%{name}

%files x11
%{_bindir}/xkoules
%attr(644,root,root) %{_mandir}/man6/xkoules.6*
%attr(644,root,root) %{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/koules.desktop

%files sdl
%attr(755,root,root) %{_bindir}/koules.sdl
%attr(644,root,root) %{_mandir}/man6/koules.sdl.6*

%changelog
%autochangelog
