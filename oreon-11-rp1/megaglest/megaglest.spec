%global source0_hash e02e58c2329558cc5d67374b5e5f9b3cfaafc300b96feff71df8d4b0d39e1eaa

Name:       megaglest
Version:    3.13.0
Release:    32%{?dist}
Summary:    Open Source 3d real time strategy game
License:    GPL-3.0-or-later AND GPL-1.0-or-later
Url:        http://megaglest.org/
Source0:        https://github.com/MegaGlest/%{name}-source/archive/%{version}/%{name}-source-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  subversion
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  ftgl-devel
BuildRequires:  gnutls-devel
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libircclient-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  lua-devel
BuildRequires:  openssl-devel
BuildRequires:  xerces-c-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
Requires:   glx-utils
Requires:   %{name}-data = %{version}
Requires:   p7zip
Obsoletes:  glest <= 3.2.2

# Correct use of XERCESC_INCLUDE and XERCESC_INCLUDE_DIR that
# should have the same value if xerces is found.
Patch0:     %{name}-xerces.patch
# Correct usage of xvfb-run when generating manpages
Patch1:     %{name}-help2man.patch
# Do not fail with cryptic message if there are missing translations
# just use english text
Patch2:     %{name}-translation-missing.patch
# Build with lua5.2
Patch3:     %{name}-lua.patch
# Add extra libraries to link command line to satisfy unresolved symbols
Patch4:     %{name}-underlink.patch
# Prevent multiple definitions of symbols
Patch5:     %{name}-feathery_ftp.patch
# Fix lua version ordering so 5.4 is preferred over 5.3
Patch6:     %{name}-fix-lua-version-ordering.patch
# Ignore GLEW_ERROR_NO_GLX_DISPLAY (we can continue with this on Wayland)
Patch7:     %{name}-ignore-GLEW_ERROR_NO_GLX_DISPLAY.patch
# Support wxWidgets 3.2 (next 4 patches from upstream)
Patch8:         e09ba53c436279588f769d6ce8852e74d58f8391.patch
Patch9:         fbd0cfb17ed759d24aeb577a602b0d97f7895cc2.patch
Patch10:        5801b1fafff8ad9618248d4d5d5c751fdf52be2f.patch
Patch11:        789e1cdf371137b729e832e28a5feb6e97a3a243.patch
# Add missing includes to fix build with GCC 15
# https://github.com/MegaGlest/megaglest-source/pull/295
# https://bugzilla.redhat.com/show_bug.cgi?id=2340839
Patch12:        0001-Add-missing-string-includes-for-memcpy.patch

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
# TODO: Please submit an issue to upstream (rhbz#2380894)
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

%files
%doc docs/AUTHORS.source_code.txt
%doc docs/CHANGELOG.txt
%doc docs/COPYRIGHT.source_code.txt
%doc docs/gnu_gpl_3.0.txt
%doc docs/README.txt
%{_bindir}/*
%{_mandir}/man6/*.6*
%{_datadir}/%{name}/

%changelog
%autochangelog
