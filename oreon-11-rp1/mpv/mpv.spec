%global source0_hash ee21092a5ee427353392360929dc64645c54479aefdb5babc5cfbb5fad626209
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]
Name:           mpv
Version:        0.41.0
Release:        6%{?dist}
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
Summary:        Movie player playing most video formats and DVDs
URL:            https://%{name}.io/
Source0:        https://github.com/%{name}-player/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with x11}
%endif
Requires:       hicolor-icon-theme
Provides:       mplayer-backend
Recommends:     (yt-dlp or youtube-dl)
Suggests:       yt-dlp
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  libatomic
BuildRequires:  meson
BuildRequires:  perl(Encode)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigRat)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(ffnvcodec)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libplacebo)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(lua-5.1)
BuildRequires:  pkgconfig(mujs)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xpresent)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-docutils
# /oreon:deps
%description
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

Mpv has an OpenGL, Vulkan, and D3D11 based video output that is capable of many
features loved by videophiles, such as video scaling with popular high quality
algorithms, color management, frame timing, interpolation, HDR, and more.

While mpv strives for minimalism and provides no real GUI, it has a small
controller on top of the video for basic control.

Mpv can leverage most hardware decoding APIs on all platforms. Hardware
decoding can be enabled at runtime on demand.

Powerful scripting capabilities can make the player do almost anything. There
is a large selection of user scripts on the wiki.

A straightforward C API was designed from the ground up to make mpv usable as
a library and facilitate easy integration into other applications.

%package libs
Summary: Dynamic library for Mpv frontends
Recommends: (yt-dlp or youtube-dl)
Suggests: yt-dlp
%description libs
This package contains the dynamic library libmpv, which provides access to Mpv.

%package devel
Summary: Development package for libmpv
Provides: %{name}-libs-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-libs-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
This package contains development header files and libraries for Mpv.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -e "s|/usr/local/etc|%{_sysconfdir}/%{name}|" -i etc/%{name}.conf

%build

%meson --auto-features=auto \
    -Dalsa=enabled \
    -Dbuild-date=false \
    -Dcaca=enabled \
    -Dcdda=enabled \
    -Dcplayer=true \
    -Dcplugins=enabled \
    -Dcuda-hwaccel=enabled \
    -Dcuda-interop=enabled \
    -Ddmabuf-wayland=enabled \
    -Ddrm=enabled \
    -Ddvbin=enabled \
    -Ddvdnav=enabled \
    -Degl-drm=enabled \
    -Degl-wayland=enabled \
%if %{with x11}
    -Degl-x11=enabled \
    -Dgl-x11=enabled \
    -Dvaapi-x11=enabled \
    -Dvdpau-gl-x11=enabled \
    -Dvdpau=enabled \
    -Dx11=enabled \
    -Dxv=enabled \
%endif
    -Degl=enabled \
    -Dgbm=enabled \
    -Dgl=enabled \
    -Dhtml-build=enabled \
    -Diconv=enabled \
    -Djack=enabled \
    -Djavascript=enabled \
    -Djpeg=enabled \
    -Dlcms2=enabled \
    -Dlibarchive=enabled \
    -Dlibavdevice=enabled \
    -Dlibbluray=enabled \
    -Dlibmpv=true \
    -Dlua=enabled \
    -Dmanpage-build=enabled \
    -Dopenal=enabled \
    -Dopensles=disabled \
    -Doss-audio=disabled \
    -Dpipewire=enabled \
    -Dplain-gl=enabled \
    -Dpulse=enabled \
    -Drubberband=enabled \
    -Dsdl2-audio=enabled \
    -Dsdl2-gamepad=enabled \
    -Dsdl2-video=enabled \
    -Dshaderc=disabled \
    -Dsndio=disabled \
    -Dspirv-cross=disabled \
    -Duchardet=enabled \
    -Dvaapi-drm=enabled \
    -Dvaapi-wayland=enabled \
    -Dvaapi=enabled \
    -Dvapoursynth=enabled \
    -Dvector=enabled \
    -Dvulkan=enabled \
    -Dwayland=enabled \
    -Dwerror=false \
    -Dzimg=enabled \
    -Dzlib=enabled
%meson_build
%install
%meson_install
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n mpv-libs -f %{oreon_filedir}/mpv-libs.list
%files -n mpv-devel -f %{oreon_filedir}/mpv-devel.list

%changelog

%autochangelog

