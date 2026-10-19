%global source0_hash de7eb94ab66212ae7758376524368a8ab208234b33796625ca630547dbc83832
%undefine _hardened_build
%global unstable 0
Name:           mednafen
Version:        1.32.1
%if %{unstable} == 1
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        A multi-system emulator utilizing OpenGL and SDL
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND ISC AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND Zlib 
URL:            https://mednafen.github.io/
%if %{?unstable} == 1
Source0:        https://mednafen.github.io/releases/files/%{name}-%{version}-UNSTABLE.tar.xz
%else
%endif
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libmpcdec-devel
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
A portable, utilizing OpenGL and SDL, argument(command-line)-driven multi-system
emulator. Mednafen has the ability to remap hotkey functions and virtual system
inputs to a keyboard, a joystick, or both simultaneously. Save states are
supported, as is real-time game rewinding. Screen snapshots may be taken, in the
PNG file format, at the press of a button. Mednafen can record audiovisual
movies in the QuickTime file format, with several different lossless codecs
supported.

The following systems are supported(refer to the emulation module documentation
for more details):

* Apple II/II+
* Atari Lynx
* Neo Geo Pocket (Color)
* WonderSwan
* GameBoy (Color)
* GameBoy Advance
* Nintendo Entertainment System
* Super Nintendo Entertainment System/Super Famicom
* Virtual Boy
* PC Engine/TurboGrafx 16 (CD)
* SuperGrafx
* PC-FX
* Sega Game Gear
* Sega Genesis/Megadrive
* Sega Master System
* Sega Saturn (experimental, x86_64 only)
* Sony PlayStation

Due to the threaded model of emulation used in Mednafen, and limitations of SDL,
a joystick is preferred over a keyboard to play games, as the joystick will have
slightly less latency, although the latency differences may not be perceptible
to most people. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

# Permission cleanup
find \( -name \*.c\* -or -name \*.h\* -or -name \*.inc \) -exec chmod -x {} \;

%build

%define _lto_cflags -flto=auto -ffat-lto-objects
CFLAGS="$RPM_OPT_FLAGS -Wl,-z,relro -Wl,-z,now"
CXXFLAGS="$RPM_OPT_FLAGS -Wl,-z,relro -Wl,-z,now"
export CFLAGS
export CXXFLAGS
%configure --disable-rpath \
    --with-external-lzo \
    --with-external-mpcdec
%make_build
%install
%make_install
rm -rf Documentation/*.def Documentation/*.php Documentation/generate.sh \
    Documentation/Makefile.* Documentation/docgen.inc
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
