%global source0_hash 497bc9d4d5846cb0eee71eaed2352d2350f789df3a913f423a3d6eed9ba428e8
%global srcname attract
%global forgeurl https://github.com/mickelson/%{srcname}
%global build_flags prefix="%{_prefix}" FE_HWACCEL_VAAPI=1 FE_HWACCEL_VDPAU=1
Name:           attract-mode
Version:        2.7.0
Release:        1%{?dist}
Summary:        A graphical front-end for command line emulators
License:        GPL-3.0-or-later AND BSL-1.0 AND LicenseRef-Fedora-Public-Domain AND MIT AND zlib
URL:            https://attractmode.org
Source0:        %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch:          %{forgeurl}/commit/659b66c6dc0e5598546ce987319adaf59cf01a0b.patch
Patch:          0001-Add-compatibility-with-FFMPEG-7.0.patch
Requires:       %{name}-data = %{version}-%{release}
Recommends:     gnu-free-sans-fonts
Recommends:     mame
Suggests:       atari800
Suggests:       dolphin-emu
Suggests:       dosbox-staging
Suggests:       mednafen
Suggests:       mupen64plus
Suggests:       scummvm
Provides:       bundled(boost-nowide) = 1.73.0.beta1
Provides:       bundled(gameswf) = 20090808
Provides:       bundled(squirrel-libs) = 3.0.4
Provides:       bundled(sqrat) = 0.8.92
Provides:       bundled(SFML) = 2.0
# oreon:deps
BuildRequires:  SFML2-devel
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libappstream-glib
BuildRequires:  libarchive-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openal-soft-devel
BuildRequires:  rapidjson-devel
BuildRequires:  stb_image-devel
BuildRequires:  stb_image-static
BuildRequires:  zlib-devel
# /oreon:deps
%description
Attract-Mode is a graphical frontend for command line emulators such as MAME,
MESS, and Nestopia. It hides the underlying operating system and is intended
to be controlled with a joystick, gamepad or spin dial, making it ideal for
use in arcade cabinet setups.

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
%description    data
This package contains layouts, plugins and other data files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

# remove unneeded bundled libraries
rm -r extlibs/{expat,nvapi} src/backward.{cpp,hpp}
# use system rapidjson
rm -r extlibs/rapidjson/include/rapidjson
ln -s %{_includedir}/rapidjson extlibs/rapidjson/include/
# bundled miniz is not used when building with system libarchive
rm extlibs/miniz/*
# use system stb_image
ln -sf %{_includedir}/stb_image.h src/

%build

export PKG_CONFIG_PATH=%{_libdir}/SFML2/pkgconfig
export CXXFLAGS="%{optflags} -I%{_includedir}/SFML2"
export LDFLAGS="%{?build_ldflags} -L%{_libdir}/SFML2"
export EXTRA_CXXFLAGS="%{optflags} -I%{_includedir}/SFML2"
%make_build %{build_flags} STRIP=/bin/true
%install
%make_install %{build_flags}
install -Dpm0644 -t %{buildroot}%{_datadir}/icons/hicolor/512x512/apps util/linux/%{name}.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications util/linux/%{name}.desktop
install -Dpm0644 -t %{buildroot}%{_metainfodir} util/linux/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%oreon_autofiles attract-mode-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n attract-mode-data -f %{oreon_filedir}/attract-mode-data.list

%changelog

%autochangelog
