%global source0_hash aafd8831ee2d187d7647ad671a03aabd2df3b7248b0bac0b3ac36ffeb441aedf
Name:          arx-libertatis
Version:       1.2.1
Release:        1%{?dist}
Summary:        Cross-platform, open source port of the Arx Fatalis RPG
License:       GPLv3+ and Bitstream Vera and OFL and BSL-1.0 and MIT and zlib
URL:           https://arx-libertatis.org/
Source0:        https://arx-libertatis.org/files/%{name}-%{version}.tar.xz
Requires: hicolor-icon-theme
Provides: bundled(dejavu-fonts) = 0
Provides: bundled(google-noto-fonts) = 0
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  libepoxy-devel
BuildRequires:  ninja-build
BuildRequires:  openal-soft-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Cross-platform port of Arx Fatalis, a first-person role-playing game

Arx Libertatis is based on the publicly released Arx Fatalis source code.

%package devel
Summary: Header files and libraries for Arx Libertatis development
Requires: %{name}%{_isa} = %{version}-%{release}
%description devel
The arx-libertatis-devel package contains header files asnd libraries needed
to develop programs that use Arx Libertatis.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja
%cmake_build
%install
%cmake_install
%oreon_autofiles arx-libertatis-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/arx-libertatis.desktop
%files -f %{oreon_filedir}/main.list
%files -n arx-libertatis-devel -f %{oreon_filedir}/arx-libertatis-devel.list

%changelog

%autochangelog
