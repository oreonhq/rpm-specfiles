%global source0_hash 7a265e1cd58b317d8c9175816a54e0ab14199c21d81eb779047d7088fca52ae4

%bcond check 0

Name:        gpac
Summary:     MPEG-4 multimedia framework
Version:     26.02.0
Release:     1%{?dist}
License:     LGPL-2.0-or-later
URL:         https://gpac.io/
Source0:     https://github.com/gpac/gpac/archive/v%{version}/gpac-%{version}.tar.gz

# drop -O3 from CFLAGS
Patch0:      gpac-noopt.patch
# skip adding standard rpath
Patch1:      gpac-norpath.patch

BuildRequires:  SDL2-devel
BuildRequires:  a52dec-devel
BuildRequires:  librsvg2-devel >= 2.5.0
BuildRequires:  libGLU-devel
BuildRequires:  freetype-devel >= 2.1.4
BuildRequires:  faad2-devel
BuildRequires:  libcaca-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel >= 1.2.5
BuildRequires:  libmad-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libnghttp3-devel
BuildRequires:  xvidcore-devel >= 1.0.0
BuildRequires:  pkgconfig(libavcodec) pkgconfig(libavdevice) pkgconfig(libavformat) pkgconfig(libavfilter) pkgconfig(libavutil) pkgconfig(libswscale)
BuildRequires:  libxml2-devel
# Requires ngtcp2 linked with quictls
#BuildRequires:  ngtcp2-devel
BuildRequires:  openssl-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  zlib-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libtheora-devel
BuildRequires:  libXt-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXv-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  xmlrpc-c-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  gcc-c++

%description
GPAC is a multimedia framework based on the MPEG-4 Systems standard developed
from scratch in ANSI C.  The original development goal is to provide a clean,
small and flexible alternative to the MPEG-4 Systems reference software.

GPAC features the integration of recent multimedia standards (SVG/SMIL, VRML,
X3D, SWF, 3GPP(2) tools and more) into a single framework. GPAC also features
MPEG-4 Systems encoders/multiplexers, publishing tools for content distribution
for MP4 and 3GPP(2) files and many tools for scene descriptions
(MPEG4 <-> VRML <-> X3D converters, SWF -> MPEG-4, etc).

%package        libs
Summary:        Library for %{name}

%description    libs
The %{name}-libs package contains library for %{name}.

%package  devel
Summary:  Development libraries and files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description  devel
Development libraries and files for gpac.

%package  doc
Summary:  Documentation for %{name}

%description  doc
Documentation for %{name}.

%package  static
Summary:  Development libraries and files for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-devel-static < %{version}-%{release}
Provides:  %{name}-devel-static = %{version}-%{release}

%description  static
Static library for gpac.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -rv extra_lib/
pushd share/doc
# Fix encoding warnings
iconv -f ISO-8859-1 -t UTF8 ipmpx_syntax.bt >  ipmpx_syntax.bt.utf8
touch -r ipmpx_syntax.bt{,.utf8}
mv ipmpx_syntax.bt{.utf8,}
popd

%build
%configure \
  --extra-cflags="%{optflags} -D_FILE_OFFSET_BITS=64 -D_LARGE_FILES -D_LARGEFILE_SOURCE=1 -D_GNU_SOURCE=1 $(pkg-config --cflags libavformat)" \
  --extra-ldflags="$(pkg-config --libs jack)" \
  --X11-path=%{_prefix} \
  --libdir=%{_lib} \
  --disable-oss \
  --enable-pic \
%if %{with check}
  --unittests \
%endif
  --verbose

sed -ie 's/DEBUGBUILD=no/DEBUGBUILD=yes/' config.mak

#Avoid mess with setup.h
cp -p config.h include/gpac

%make_build all
%make_build sggen

## kwizart - build doxygen doc for devel
pushd share/doc
doxygen
popd

%install
%make_install install-lib

#Install generated sggen binaries
#for b in MPEG4 SVG X3D; do
for b in MPEG4 X3D; do
  pushd applications/generators/${b}
    install -pm 0755 ${b}Gen %{buildroot}%{_bindir}
  popd
done

#Fix doxygen timestamp
touch -r Changelog share/doc/html-libgpac/*

#config.h like but not only
#Usual multilib bug https://bugzilla.rpmfusion.org/show_bug.cgi?id=270
sed -i -e '/GPAC_CONFIGURATION/d' %{buildroot}%{_includedir}/gpac/configuration.h
touch -r Changelog %{buildroot}%{_includedir}/gpac/*.h
touch -r Changelog %{buildroot}%{_includedir}/gpac/internal/*.h
touch -r Changelog %{buildroot}%{_includedir}/gpac/modules/*.h
rm %{buildroot}%{_includedir}/gpac/config.h
# do not include in gpac, only here to create doxygen group for doc ordering
rm %{buildroot}%{_includedir}/gpac/00_doxy.h

%if %{with check}
%check
%make_build unit_tests
%endif

%files
%doc Changelog README.md
%license COPYING
%{_bindir}/gpac
%{_bindir}/MP4Box
%{_bindir}/MPEG4Gen
%{_bindir}/X3DGen
%{_datadir}/gpac/
%{_mandir}/man1/gpac-filters.1.*
%{_mandir}/man1/gpac.1.*
%{_mandir}/man1/mp4box.1.*
%{_datadir}/applications/gpac.desktop
%{_datadir}/icons/hicolor/*/apps/gpac.png

%files libs
%{_libdir}/libgpac.so.16{,.*}
%dir %{_libdir}/gpac
%{_libdir}/gpac/gm_caca_out.so
%{_libdir}/gpac/gm_ft_font.so
%{_libdir}/gpac/gm_jack.so
%{_libdir}/gpac/gm_pulseaudio.so
%{_libdir}/gpac/gm_sdl_out.so
%{_libdir}/gpac/gm_validator.so
%{_libdir}/gpac/gm_x11_out.so

%files doc
%doc share/doc/html-libgpac/*

%files devel
%doc share/doc/CODING_STYLE share/doc/ipmpx_syntax.bt
%{_includedir}/gpac/
%{_libdir}/libgpac.so
%{_libdir}/pkgconfig/gpac.pc

%files static
%{_libdir}/libgpac_static.a

%changelog
%autochangelog
