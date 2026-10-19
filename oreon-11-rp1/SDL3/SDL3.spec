%global source0_hash 7322236cd12090c3eb40b9728be4d49c76f66ad17d04369584d4ecad5cf77c68
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif
%global libdecor_majver 0
%bcond_without static
%bcond_without xscrnsaver
Name:           SDL3
Version:        3.4.16
Release:        1%{?dist}
Summary:        Cross-platform multimedia library
License:        Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 OR MIT)
URL:            http://www.libsdl.org/
Source0:        http://www.libsdl.org/release/%{name}-%{version}.tar.gz
Source1:        SDL3_revision.h
%if %{with xscrnsaver}
%endif
Requires:       (libdecor-%{libdecor_majver}.so.%{libdecor_majver}%{libsymbolsuffix} if libwayland-client)
Provides:       bundled(hidraw)
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  fribidi-devel
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXtst-devel
BuildRequires:  libdrm-devel
BuildRequires:  libthai-devel
BuildRequires:  liburing-devel
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  perl-interpreter
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  systemd-devel
BuildRequires:  vulkan-devel
# /oreon:deps
%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device.

%package devel
Summary:        Files needed to develop Simple DirectMedia Layer applications
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)
%if ! %{with static}
Obsoletes:      %{name}-static < %{version}-%{release}
%endif
%description devel
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device. This
package provides the libraries, include files, and other resources needed for
developing SDL applications.

%if %{with static}
%package static
Summary:        Static libraries for SDL3
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Static libraries for SDL3.
%endif

%package test
Summary:        Testing libraries for SDL3
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description test
Testing libraries for SDL3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git_am
sed -e 's/\r//g' -i README.md WhatsNew.txt BUGS.txt LICENSE.txt CREDITS.md

%build

export LDFLAGS="%{shrink:%{build_ldflags}}"
%cmake \
    -DSDL_INSTALL_DOCS=ON \
    -DSDL_DEPS_SHARED=ON \
    -DSDL_SSE3=OFF \
    -DSDL_RPATH=OFF \
    -DSDL_VENDOR_INFO="%{?dist_vendor} %{version}-%{release}" \
    %{?with_static:-DSDL_STATIC=ON} \
    %{?with_static:-DCMAKE_POSITION_INDEPENDENT_CODE=ON} \
    %{!?with_xscrnsaver:-DSDL_X11_XSCRNSAVER=OFF} \
%ifarch ppc64le
    -DSDL_ALTIVEC=OFF \
%endif
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_includedir}/SDL3/SDL_revision.h %{buildroot}%{_includedir}/SDL3/SDL_revision-%{_arch}.h
install -p -m 644 %{SOURCE1} %{buildroot}%{_includedir}/SDL3/SDL_revision.h
%oreon_autofiles SDL3-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles SDL3-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles SDL3-test usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n SDL3-devel -f %{oreon_filedir}/SDL3-devel.list
%files -n SDL3-static -f %{oreon_filedir}/SDL3-static.list
%files -n SDL3-test -f %{oreon_filedir}/SDL3-test.list

%changelog

%autochangelog
