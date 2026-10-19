%global source0_hash 355658462cd5d08b1a657b231dc1e0cf09f623207a2744537f4236b14af44648
Name:       eureka
Version:    2.1.0
Release:        1%{?dist}
Summary:        A cross-platform map editor for the classic DOOM games
License:    GPL-2.0-or-later
URL:        http://eureka-editor.sourceforge.net
Source0:        https://github.com/ioan-chera/eureka-editor/archive/refs/tags/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch2:     0002-endianness.patch
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  fltk-fluid
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libGL-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  xdg-utils
BuildRequires:  zlib-devel
# /oreon:deps
%description
Eureka is a cross-platform map editor for the classic DOOM games.

It started when the ported the Yadex editor to a proper GUI toolkit, namely
FLTK, and implemented a system for multi-level Undo / Redo. These and other
features have required rewriting large potions of the existing code, and adding
lots of new code too. Eureka is now an independent program with its own
work-flow and its own quirks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir eureka-editor-%{name}-%{version}
%oreon_prep
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
%oreon_autofiles main

%check

%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
