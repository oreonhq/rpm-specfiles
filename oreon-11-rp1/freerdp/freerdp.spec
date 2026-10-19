%global source0_hash 8803dd26ec9660550252f255cf2d672a785ddd8f544bb475834993e96807c87f
%global _with_static_uwac 1
%{!?rhel:%global _with_aom 1}
%{!?rhel:%global _with_openh264 1}
%{!?rhel:%global _with_sdl_client 1}
%{!?rhel:%global _with_soxr 1}
%{!?rhel:%global _with_uriparser 1}
Name:           freerdp
Epoch:          2
Version:        3.32.1
Release:        1%{?dist}
Summary:        Free implementation of the Remote Desktop Protocol (RDP)
License:        Apache-2.0 AND HPND AND LGPL-2.1-or-later AND LicenseRef-Public-Domain AND OFL-1.1
URL:            http://www.freerdp.com/
Source0:        https://github.com/FreeRDP/FreeRDP/archive/%{version}/FreeRDP-%{version}.tar.gz#/freerdp-%{version}.tar.gz
%{?_with_opencl:BuildRequires: opencl-headers >= 3.0}
%{?_with_opencl:BuildRequires: ocl-icd-devel}
%{?_with_openh264:BuildRequires:  pkgconfig(openh264)}
%{?_with_x264:BuildRequires:  x264-devel}
%{?_with_uriparser:BuildRequires:  (cmake(uriparser) and uriparser-devel)}
%{?_with_aom:BuildRequires:  pkgconfig(aom)}
%{?_with_aom:BuildRequires:  pkgconfig(libyuv)}
%{?_with_sdl_client:BuildRequires:  cmake(SDL3)}
%{?_with_sdl_client:BuildRequires:  cmake(SDL3_image)}
%{?_with_sdl_client:BuildRequires:  cmake(SDL3_ttf)}
%{?_with_soxr:BuildRequires:  pkgconfig(soxr)}
%{?_with_webview:BuildRequires:  pkgconfig(webkit2gtk-4.0)}
%{?_with_ffmpeg:
}
Provides:       xfreerdp = %{?epoch}:%{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       libwinpr%{?_isa} = %{?epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  (cmake(uriparser) and uriparser-devel)
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  cmake(SDL3)
BuildRequires:  cmake(SDL3_image)
BuildRequires:  cmake(SDL3_ttf)
BuildRequires:  cmake(json-c)
BuildRequires:  cups-devel
BuildRequires:  curl
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gsm-devel
BuildRequires:  lame-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXv-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  multilib-rpm-config
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libcbor)
BuildRequires:  pkgconfig(libfido2)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libyuv)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(sso-mib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  xmlto
BuildRequires:  zlib-devel
# /oreon:deps
%description
The xfreerdp & wlfreerdp Remote Desktop Protocol (RDP) clients from the FreeRDP
project.

xfreerdp & wlfreerdp can connect to RDP servers such as Microsoft Windows
machines, xrdp and VirtualBox.

%package        libs
Summary:        Core libraries implementing the RDP protocol
Requires:       libwinpr%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-plugins < 1:1.1.0
Provides:       %{name}-plugins = %{?epoch}:%{version}-%{release}
%description    libs
libfreerdp-core can be embedded in applications.

libfreerdp-channels and libfreerdp-kbd might be convenient to use in X
applications together with libfreerdp-core.

libfreerdp-core can be extended with plugins handling RDP channels.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig
Requires:       cmake >= 3.13
%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}-libs.

%package        server
Summary:        Server support for %{name}
Requires:       libwinpr%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{?epoch}:%{version}-%{release}
%description    server
The %{name}-server package contains servers which can export a desktop via
the RDP protocol.

%package -n     libwinpr
Summary:        Windows Portable Runtime
Provides:       %{name}-libwinpr = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-libwinpr < 1:1.2.0
%description -n libwinpr
WinPR provides API compatibility for applications targeting non-Windows
environments. When on Windows, the original native API is being used instead of
the equivalent WinPR implementation, without having to modify the code using it.

%package -n     libwinpr-devel
Summary:        Windows Portable Runtime development files
Requires:       libwinpr%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig
Requires:       cmake >= 3.13
%description -n libwinpr-devel
The %{name}-libwinpr-devel package contains libraries and header files for
developing applications that use %{name}-libwinpr.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n FreeRDP-%{version}
rm -f winpr/libwinpr/crt/unicode_builtin.c
%autopatch -p1

# Rpmlint fixes
find . -name "*.h" -exec chmod 664 {} \;
find . -name "*.c" -exec chmod 664 {} \;

%conf
%cmake \
    -DBUILD_TESTING=ON \
    -DBUILD_TESTING_NO_H264=ON \
    -DCHANNEL_RDP2TCP=ON \
    -DCHANNEL_RDP2TCP_CLIENT=ON \
    -DCHANNEL_RDPEWA=ON \
    -DCHANNEL_RDPEWA_CLIENT=ON \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DWITH_ALSA=ON \
    -DWITH_AAD=ON \
    -DWITH_CAIRO=ON \
    -DWITH_CUPS=ON \
    -DWITH_CHANNELS=ON \
    -DWITH_CLIENT=ON \
    -DWITH_CLIENT_SDL=%{?_with_sdl_client:ON}%{?!_with_sdl_client:OFF} \
    -DWITH_SDL_IMAGE_DIALOGS=%{?_with_sdl_client:ON}%{?!_with_sdl_client:OFF} \
    -DWITH_DSP_FFMPEG=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
    -DWITH_FDK_AAC=ON \
    -DWITH_FFMPEG=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
    -DWITH_FUSE=ON \
    -DWITH_GSM=ON \
    -DWITH_GFX_AV1=%{?_with_aom:ON}%{?!_with_aom:OFF} \
    -DWITH_IPP=OFF \
    -DWITH_JPEG=ON \
    -DWITH_JSONC_REQUIRED=ON \
    -DWITH_KEYBOARD_LAYOUT_FROM_FILE=ON \
    -DWITH_KRB5=ON \
    -DWITH_LAME=ON \
    -DWITH_MANPAGES=ON \
    -DWITH_OPENCL=%{?_with_opencl:ON}%{?!_with_opencl:OFF} \
    -DWITH_OPENH264=%{?_with_openh264:ON}%{?!_with_openh264:OFF} \
    -DWITH_OPENSSL=ON \
    -DWITH_OPUS=ON \
    -DWITH_PCSC=ON \
    -DWITH_PKCS11=ON \
    -DWITH_PULSE=ON \
    -DWITH_RDTK=ON \
    -DWITH_SAMPLE=OFF \
    -DWITH_SERVER=ON \
    -DWITH_SERVER_INTERFACE=ON \
    -DWITH_SHADOW_X11=ON \
    -DWITH_SHADOW_MAC=ON \
    -DWITH_SOXR=%{?_with_soxr:ON}%{?!_with_soxr:OFF} \
    -DWITH_SSO_MIB=ON \
    -DWITH_SWSCALE=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
    -DWITH_TIMEZONE_COMPILED=OFF \
    -DWITH_TIMEZONE_FROM_FILE=ON \
    -DWITH_URIPARSER=%{?_with_uriparser:ON}%{?!_with_uriparser:OFF} \
    -DWITH_VERBOSE_WINPR_ASSERT=OFF \
    -DWITH_VIDEO_FFMPEG=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
    -DWITH_WAYLAND=ON \
    -DWITH_WEBVIEW=%{?_with_webview:ON}%{?!_with_webview:OFF} \
    -DWITH_X11=ON \
    -DWITH_XCURSOR=ON \
    -DWITH_XEXT=ON \
    -DWITH_XKBFILE=ON \
    -DWITH_XI=ON \
    -DWITH_XINERAMA=ON \
    -DWITH_XRENDER=ON \
    -DWITH_XTEST=ON \
    -DWITH_XV=ON \
    -DWITH_ZLIB=ON \
%ifarch x86_64
    -DWITH_SSE2=ON \
    -DWITH_VAAPI=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
%else
    -DWITH_SSE2=OFF \
%endif
%ifarch armv7hl
    -DARM_FP_ABI=hard \
    -DWITH_NEON=OFF \
%endif
%ifarch armv7hnl
    -DARM_FP_ABI=hard \
    -DWITH_NEON=ON \
%endif
%ifarch armv5tel armv6l armv7l
    -DARM_FP_ABI=soft \
    -DWITH_NEON=OFF \
%endif
    -DUWAC_FORCE_STATIC_BUILD=%{?_with_static_uwac:ON}%{?!_with_static_uwac:OFF} \
    -DWINPR_UTILS_IMAGE_PNG=ON \
    -DWINPR_UTILS_IMAGE_WEBP=ON \
    -DWINPR_UTILS_IMAGE_JPEG=ON \
    %{nil}

%build

%cmake_build
%check

export CTEST_OUTPUT_ON_FAILURE=1
%cmake_build --target test
%install
%cmake_install
find %{buildroot} -name "*.a" -delete
%multilib_fix_c_header --file %{_includedir}/freerdp3/freerdp/build-config.h
%oreon_autofiles libwinpr usr/*/lib*.so.*
%oreon_autofiles libwinpr-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n freerdp-libs -f %{oreon_filedir}/freerdp-libs.list
%files -n freerdp-devel -f %{oreon_filedir}/freerdp-devel.list
%files -n freerdp-server -f %{oreon_filedir}/freerdp-server.list
%files -n libwinpr -f %{oreon_filedir}/libwinpr.list
%files -n libwinpr-devel -f %{oreon_filedir}/libwinpr-devel.list

%changelog

%autochangelog
