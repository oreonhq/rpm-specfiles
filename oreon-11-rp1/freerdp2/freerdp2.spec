%global source0_hash 8a3e9a29b0deb647daa27c6d2a3be3bd2ab8e4a53c8680ef996f74b77a1e9f71
%{!?rhel:%global _with_soxr 1}
%global build_type_safety_c 2
Name:           freerdp2
Version:        2.11.8
Release:        1%{?dist}
Summary:        Free implementation of the Remote Desktop Protocol (RDP)
License:        Apache-2.0 AND HPND AND ISC-Veillard AND LGPL-2.1-or-later
URL:            http://www.freerdp.com/
Source0:        FreeRDP-%{version}-repack.tar.gz
Source1:        freerdp_download_and_repack.sh
%{?_with_server:BuildRequires:  libXtst-devel}
%{?_with_opencl:BuildRequires: opencl-headers >= 3.0}
%{?_with_opencl:BuildRequires: ocl-icd-devel}
%{?_with_x264:BuildRequires:  x264-devel}
%{?_with_server:BuildRequires:  pam-devel}
%{?_with_gss:BuildRequires:  pkgconfig(krb5) >= 1.13}
%{?_with_soxr:BuildRequires:  pkgconfig(soxr)}
%{?_with_ffmpeg:
}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  cups-devel
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
BuildRequires:  libXv-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  multilib-rpm-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(soxr)
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
Requires:       libwinpr2%{?_isa} = %{version}-%{release}
%description    libs
libfreerdp-core can be embedded in applications.

libfreerdp-channels and libfreerdp-kbd might be convenient to use in X
applications together with libfreerdp-core.

libfreerdp-core can be extended with plugins handling RDP channels.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake >= 2.8
Conflicts:      freerdp-devel
%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}-libs.

%package -n     libwinpr2
Summary:        Windows Portable Runtime
%description -n libwinpr2
WinPR provides API compatibility for applications targeting non-Windows
environments. When on Windows, the original native API is being used instead of
the equivalent WinPR implementation, without having to modify the code using it.

%package -n     libwinpr2-devel
Summary:        Windows Portable Runtime development files
Requires:       libwinpr2%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake >= 2.8
Conflicts:      libwinpr-devel
%description -n libwinpr2-devel
The %{name}-libwinpr-devel package contains libraries and header files for
developing applications that use %{name}-libwinpr.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n FreeRDP-%{version}

# Rpmlint fixes
find . -name "*.h" -exec chmod 664 {} \;
find . -name "*.c" -exec chmod 664 {} \;

%build

%cmake %{?_cmake_skip_rpath} \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DWITH_ALSA=ON \
    -DWITH_CAIRO=ON \
    -DWITH_CUPS=ON \
    -DWITH_CHANNELS=ON -DBUILTIN_CHANNELS=OFF \
    -DWITH_CLIENT=OFF \
    -DWITH_DIRECTFB=OFF \
    -DWITH_DSP_FFMPEG=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
    -DWITH_FFMPEG=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
    -DWITH_GSM=ON \
    -DWITH_GSSAPI=%{?_with_gss:ON}%{?!_with_gss:OFF} \
    -DWITH_ICU=ON \
    -DWITH_IPP=OFF \
    -DWITH_JPEG=ON \
    -DWITH_LAME=ON \
    -DWITH_MANPAGES=OFF \
    -DWITH_OPENCL=%{?_with_opencl:ON}%{?!_with_opencl:OFF} \
    -DWITH_OPENH264=ON \
    -DWITH_OPENSSL=ON \
    -DWITH_PCSC=ON \
    -DWITH_PULSE=ON \
    -DWITH_SERVER=%{?_with_server:ON}%{?!_with_server:OFF} \
    -DWITH_SERVER_INTERFACE=%{?_with_server:ON}%{?!_with_server:OFF} \
    -DWITH_SHADOW_X11=%{?_with_server:ON}%{?!_with_server:OFF} \
    -DWITH_SHADOW_MAC=%{?_with_server:ON}%{?!_with_server:OFF} \
    -DWITH_SOXR=%{?_with_soxr:ON}%{?!_with_soxr:OFF} \
    -DWITH_WAYLAND=ON \
    -DWITH_X11=ON \
    -DWITH_XCURSOR=ON \
    -DWITH_XEXT=ON \
    -DWITH_XKBFILE=ON \
    -DWITH_XI=ON \
    -DWITH_XINERAMA=ON \
    -DWITH_XRENDER=ON \
    -DWITH_XTEST=%{?_with_server:ON}%{?!_with_server:OFF} \
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
    %{nil}
%cmake_build
%install
%cmake_install
find %{buildroot} -name "*.a" -delete
%multilib_fix_c_header --file %{_includedir}/freerdp2/freerdp/build-config.h
rm -rfv %{buildroot}%{_bindir}
%oreon_autofiles libwinpr2 usr/*/lib*.so.*
%oreon_autofiles libwinpr2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n freerdp2-libs -f %{oreon_filedir}/freerdp2-libs.list
%files -n freerdp2-devel -f %{oreon_filedir}/freerdp2-devel.list
%files -n libwinpr2 -f %{oreon_filedir}/libwinpr2.list
%files -n libwinpr2-devel -f %{oreon_filedir}/libwinpr2-devel.list

%changelog

%autochangelog
