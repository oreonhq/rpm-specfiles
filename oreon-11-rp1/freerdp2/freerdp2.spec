%global source0_hash 8a3e9a29b0deb647daa27c6d2a3be3bd2ab8e4a53c8680ef996f74b77a1e9f71

# Can be rebuilt with FFmpeg support enabled by passing
# "--with=ffmpeg" to mock/rpmbuild; or by globally
# setting these variables:
# https://bugzilla.redhat.com/show_bug.cgi?id=2242028
#global _with_ffmpeg 1

# Can be rebuilt with OpenCL support enabled by passing # "--with=opencl"
# or by globally setting:
#global _opencl 1

# Momentarily disable GSS support
# https://github.com/FreeRDP/FreeRDP/issues/4348
#global _with_gss 1

# Disable server support in RHEL
# https://bugzilla.redhat.com/show_bug.cgi?id=1639165
%if 0%{?fedora} || 0%{?rhel} >= 10
%global _with_server 1
%endif

# Disable support for missing codecs in RHEL
%{!?rhel:%global _with_soxr 1}

# FIXME: GCC 14.x says there's lots of incompatible pointer casts going on...
%global build_type_safety_c 2

Name:           freerdp2
Version:        2.11.7
Release:        11%{?dist}
Summary:        Free implementation of the Remote Desktop Protocol (RDP)

# The effective license is Apache-2.0 but:
# uwac/libuwac/* is HPND
# winpr/libwinpr/utils/trio/* is ISC-Veillard
# uwac/protocols/server-decoration.xml is LGPL-2.1-or-later
License:        Apache-2.0 AND HPND AND ISC-Veillard AND LGPL-2.1-or-later
URL:            http://www.freerdp.com/

# The license of the winpr/libwinpr/crt/utf.[h|c] files is not allowed.
# See: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/498
# Run the ./freerdp_download_and_repack.sh script to prepare tarball.
Source0:        FreeRDP-%{version}-repack.tar.gz
Source1:        freerdp_download_and_repack.sh

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake >= 2.8
BuildRequires:  cups-devel
BuildRequires:  gsm-devel
BuildRequires:  lame-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXrandr-devel
%{?_with_server:BuildRequires:  libXtst-devel}
BuildRequires:  libXv-devel
%{?_with_opencl:BuildRequires: opencl-headers >= 3.0}
%{?_with_opencl:BuildRequires: ocl-icd-devel}
BuildRequires:  pkgconfig(openh264)
%{?_with_x264:BuildRequires:  x264-devel}
%{?_with_server:BuildRequires:  pam-devel}
BuildRequires:  xmlto
BuildRequires:  zlib-devel
BuildRequires:  multilib-rpm-config

BuildRequires:  pkgconfig(cairo)
%{?_with_gss:BuildRequires:  pkgconfig(krb5) >= 1.13}
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(openssl)
%{?_with_soxr:BuildRequires:  pkgconfig(soxr)}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%{?_with_ffmpeg:
BuildRequires:  pkgconfig(libavcodec) >= 57.48.101
BuildRequires:  pkgconfig(libavutil)
}

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

# Delete executables we do not need
rm -rfv %{buildroot}%{_bindir}

%files libs
%license LICENSE
%doc README.md ChangeLog
%{_libdir}/freerdp2/
%{_libdir}/libfreerdp-client2.so.*
%{?_with_server:
%{_libdir}/libfreerdp-server2.so.*
%{_libdir}/libfreerdp-shadow2.so.*
%{_libdir}/libfreerdp-shadow-subsystem2.so.*
}
%{_libdir}/libfreerdp2.so.*
%{_libdir}/libuwac0.so.*

%files devel
%{_includedir}/freerdp2/
%{_includedir}/uwac0/
%{_libdir}/cmake/FreeRDP2/
%{_libdir}/cmake/FreeRDP-Client2/
%{?_with_server:
%{_libdir}/cmake/FreeRDP-Server2/
%{_libdir}/cmake/FreeRDP-Shadow2/
}
%{_libdir}/cmake/uwac0/
%{_libdir}/libfreerdp-client2.so
%{?_with_server:
%{_libdir}/libfreerdp-server2.so
%{_libdir}/libfreerdp-shadow2.so
%{_libdir}/libfreerdp-shadow-subsystem2.so
}
%{_libdir}/libfreerdp2.so
%{_libdir}/libuwac0.so
%{_libdir}/pkgconfig/freerdp2.pc
%{_libdir}/pkgconfig/freerdp-client2.pc
%{?_with_server:
%{_libdir}/pkgconfig/freerdp-server2.pc
%{_libdir}/pkgconfig/freerdp-shadow2.pc
}
%{_libdir}/pkgconfig/uwac0.pc

%files -n libwinpr2
%license LICENSE
%doc README.md ChangeLog
%{_libdir}/libwinpr2.so.*
%{_libdir}/libwinpr-tools2.so.*

%files -n libwinpr2-devel
%{_libdir}/cmake/WinPR2/
%{_includedir}/winpr2/
%{_libdir}/libwinpr2.so
%{_libdir}/libwinpr-tools2.so
%{_libdir}/pkgconfig/winpr2.pc
%{_libdir}/pkgconfig/winpr-tools2.pc

%changelog
%autochangelog
