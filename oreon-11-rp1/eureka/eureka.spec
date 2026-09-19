%global source0_hash 355658462cd5d08b1a657b231dc1e0cf09f623207a2744537f4236b14af44648

Name:       eureka
Version:    2.1.0
Release:    2%{?dist}
Summary:    A cross-platform map editor for the classic DOOM games

License:    GPL-2.0-or-later
URL:        http://eureka-editor.sourceforge.net
Source0:    https://github.com/ioan-chera/eureka-editor/archive/refs/tags/%{name}-%{version}/%{name}-%{version}.tar.gz

# This patch fixes two issues:
# 1. aarch64 is wrongfully classified as big-endian.
#    This seems to have already been fixed upsteam.
# 2. The program converts endianness when reading files, but not when writing
#    files, leading to malformed outputs on s390x.
Patch2:     0002-endianness.patch

BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  fltk-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libGL-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-fluid
BuildRequires:  make
BuildRequires:  ImageMagick
BuildRequires:  xdg-utils

%description
Eureka is a cross-platform map editor for the classic DOOM games.

It started when the ported the Yadex editor to a proper GUI toolkit, namely
FLTK, and implemented a system for multi-level Undo / Redo. These and other
features have required rewriting large potions of the existing code, and adding
lots of new code too. Eureka is now an independent program with its own
work-flow and its own quirks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n eureka-editor-%{name}-%{version}

%build
%cmake -DUSE_SYSTEM_FLTK=ON -DUSE_SYSTEM_GOOGLE_TEST=ON
%cmake_build

%install
%cmake_install

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
magick convert misc/eureka.ico %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/eureka.png

install -m 755 -d %{buildroot}/%{_mandir}/man6/
install -m 644 -p misc/eureka.6 %{buildroot}%{_mandir}/man6/%{name}.6

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p misc/eureka.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
%ctest

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license GPL.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/128x128/apps/eureka.png
%{_datadir}/applications/*.desktop
%{_mandir}/man6/%{name}.6*
%doc AUTHORS.md README.txt TODO.txt
%doc changelogs/

%changelog
%autochangelog
