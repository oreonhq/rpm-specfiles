%global source0_hash e02e58c2329558cc5d67374b5e5f9b3cfaafc300b96feff71df8d4b0d39e1eaa
Name:       megaglest
Version:    3.13.0
Release:        32%{?dist}
Summary:        Open Source 3d real time strategy game
License:    GPL-3.0-or-later AND GPL-1.0-or-later
Url:        http://megaglest.org/
Source0:        https://github.com/MegaGlest/%{name}-source/archive/%{version}/%{name}-source-%{version}.tar.gz
Requires:   glx-utils
Requires:   %{name}-data = %{version}
Requires:   p7zip
Obsoletes:  glest <= 3.2.2
Patch0:     %{name}-xerces.patch
Patch1:     %{name}-help2man.patch
Patch2:     %{name}-translation-missing.patch
Patch3:     %{name}-lua.patch
Patch4:     %{name}-underlink.patch
Patch5:     %{name}-feathery_ftp.patch
Patch6:     %{name}-fix-lua-version-ordering.patch
Patch7:     %{name}-ignore-GLEW_ERROR_NO_GLX_DISPLAY.patch
Patch8:         e09ba53c436279588f769d6ce8852e74d58f8391.patch
Patch9:         fbd0cfb17ed759d24aeb577a602b0d97f7895cc2.patch
Patch10:        5801b1fafff8ad9618248d4d5d5c751fdf52be2f.patch
Patch11:        789e1cdf371137b729e832e28a5feb6e97a3a243.patch
Patch12:        0001-Add-missing-string-includes-for-memcpy.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  help2man
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libircclient-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  subversion
BuildRequires:  wxGTK-devel
BuildRequires:  xerces-c-devel
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  zlib-devel
# /oreon:deps
%description
MegaGlest is an entertaining free (freeware and free software) and
open source cross-platform 3D real-time strategy (RTS) game, where
you control the armies of one of seven different factions: Tech,
Magic, Egypt, Indians, Norsemen, Persian or Romans. The game is
setup in one of 17 naturally looking settings, which -like the
unit models- are crafted with great appreciation for detail.
A lot of additional game data can be downloaded from within the
game at no cost.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-source-%{version}

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
mkdir -p %{_vpath_builddir}
export XERCESC_INCLUDE_DIR=%{_includedir}/xercesc-2.7.0
export XERCESC_LIBRARY_DIR=%{_libdir}/xerces-c-2.7.0
%cmake \
  -DMEGAGLEST_BIN_INSTALL_PATH=%{_bindir} \
  -DWANT_GIT_STAMP=OFF
%cmake_build
%install
%cmake_install
install -d %{buildroot}/%{_datadir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
