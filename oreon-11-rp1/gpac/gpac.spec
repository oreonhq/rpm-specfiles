%global source0_hash 57822c1a74dcb83d76ff1f671e1b4fae2e7614e8194a5adb9f20661e0e9421dd
%bcond check 0
Name:        gpac
Summary:        MPEG-4 multimedia framework
Version:     26.07.0
Release:        1%{?dist}
License:     LGPL-2.0-or-later
URL:         https://gpac.io/
Source0:        https://github.com/gpac/gpac/archive/v%{version}/gpac-%{version}.tar.gz
Patch0:      gpac-noopt.patch
Patch1:      gpac-norpath.patch
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  a52dec-devel
BuildRequires:  doxygen
BuildRequires:  faad2-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libGLU-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  libXv-devel
BuildRequires:  libcaca-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmad-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libnghttp3-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  openssl-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  xmlrpc-c-devel
BuildRequires:  xvidcore-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
cp -p config.h include/gpac
%make_build all
%make_build sggen
pushd share/doc
doxygen
popd
%install
%make_install install-lib
for b in MPEG4 X3D; do
  pushd applications/generators/${b}
    install -pm 0755 ${b}Gen %{buildroot}%{_bindir}
  popd
done
touch -r Changelog share/doc/html-libgpac/*
sed -i -e '/GPAC_CONFIGURATION/d' %{buildroot}%{_includedir}/gpac/configuration.h
touch -r Changelog %{buildroot}%{_includedir}/gpac/*.h
touch -r Changelog %{buildroot}%{_includedir}/gpac/internal/*.h
touch -r Changelog %{buildroot}%{_includedir}/gpac/modules/*.h
rm %{buildroot}%{_includedir}/gpac/config.h
rm %{buildroot}%{_includedir}/gpac/00_doxy.h
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%make_build unit_tests
%endif
%files -f %{oreon_filedir}/main.list
%files -n gpac-libs -f %{oreon_filedir}/gpac-libs.list
%files -n gpac-devel -f %{oreon_filedir}/gpac-devel.list
%files -n gpac-doc -f %{oreon_filedir}/gpac-doc.list
%files -n gpac-static -f %{oreon_filedir}/gpac-static.list

%changelog

%autochangelog
