%global source0_hash a5b4eb11d9065f2fcd55a8f5109b4ca3b64ce363f9b5927077a6c90a068dd5d4

%global forgeurl https://github.com/libretro/%{corename}-libretro
%global commit 04486b4846ec45e8a3971f7e52a03d9be7ac5552
%global corename gambatte

Name:           libretro-%{corename}
Version:        0
%forgemeta
Release:        0.9.%autorelease
Summary:        Libretro implementation of libgambatte

License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
BuildRequires:  make

Supplements:    gnome-games
Supplements:    retroarch

%description
Gambatte is an accuracy-focused, open-source, cross-platform Game Boy Color
emulator written in C++. It is based on hundreds of corner case hardware tests,
as well as previous documentation and reverse engineering efforts.

The core emulation code is contained in a separate library back-end
(libgambatte) written in platform-independent C++. There is currently a GUI
front-end (gambatte_qt) using Trolltech's Qt4 toolkit, and a simple command-line
SDL front-end (gambatte_sdl).

The GUI front-end contains platform-specific extensions for video, sound and
timers. It should work on MS Windows, Linux/BSD/UNIX-like OSes, and Mac OS X.

The SDL front-end should be usable on all platforms with a working SDL port. It
should also be quite trivial to create new (simple) front-ends (note that the
library API should in no way be considered stable).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%set_build_flags
%make_build

%install
%make_install core_installdir=%{_libdir}/libretro
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro

%files
%license COPYING
%doc README.md
%{_libdir}/libretro/

%changelog
%autochangelog
