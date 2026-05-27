%global source0_hash 332cb37d0be20cb9541739c61f79bae5a477427d79ae85e352089afdaf6666e4

# For the generated library symbol suffix
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif

# For declaring rich dependency on libdecor
%global libdecor_majver 0

Name:           SDL2
Version:        2.28.5
Release:        1%{?dist}
Summary:        Cross-platform multimedia library
License:        Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 OR MIT)
URL:            http://www.libsdl.org/
Source0:        http://www.libsdl.org/release/%{name}-%{version}.tar.gz
Source1:        SDL_config.h
Source2:        SDL_revision.h

Patch0:         multilib.patch
# Prefer Wayland by default
Patch1:         SDL2-2.0.22-prefer-wayland.patch

BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  libXext-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXcursor-devel
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(libusb-1.0)
# PulseAudio
BuildRequires:  pkgconfig(libpulse-simple)
# Jack
BuildRequires:  pkgconfig(jack)
# PipeWire
BuildRequires:  pkgconfig(libpipewire-0.3)
# D-Bus
BuildRequires:  pkgconfig(dbus-1)
# IBus
BuildRequires:  pkgconfig(ibus-1.0)
# Wayland
BuildRequires:  pkgconfig(libdecor-%{libdecor_majver})
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
# Vulkan
BuildRequires:  vulkan-devel
# KMS
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libdrm-devel

# Ensure libdecor is pulled in when libwayland-client is (rhbz#1992804)
Requires:       (libdecor-%{libdecor_majver}.so.%{libdecor_majver}%{libsymbolsuffix} if libwayland-client)

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device.

%package devel
Summary:        Files needed to develop Simple DirectMedia Layer applications
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mesa-libEGL-devel%{?_isa}
Requires:       mesa-libGLES-devel%{?_isa}
Requires:       libX11-devel%{?_isa}
# Conflict with versions before libSDLmain moved here
Conflicts:      %{name}-static < 2.0.18-4

%description devel
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device. This
package provides the libraries, include files, and other resources needed for
developing SDL applications.

%package static
Summary:        Static libraries for SDL2
# Needed to keep CMake happy
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
# Conflict with versions before libSDLmain moved to -devel
Conflicts:      %{name}-devel < 2.0.18-4

%description static
Static libraries for SDL2.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git
sed -i -e 's/\r//g' TODO.txt README.md WhatsNew.txt BUGS.txt LICENSE.txt CREDITS.txt README-SDL.txt

%build
# Deal with new CMake policy around whitespace in LDFLAGS...
export LDFLAGS="%{shrink:%{build_ldflags}}"

%cmake \
    -DSDL_DLOPEN=ON \
    -DSDL_VIDEO_KMSDRM=ON \
    -DSDL_ARTS=OFF \
    -DSDL_ESD=OFF \
    -DSDL_NAS=OFF \
    -DSDL_PULSEAUDIO_SHARED=ON \
    -DSDL_JACK_SHARED=ON \
    -DSDL_PIPEWIRE_SHARED=ON \
    -DSDL_ALSA=ON \
    -DSDL_VIDEO_WAYLAND=ON \
    -DSDL_LIBDECOR_SHARED=ON \
    -DSDL_VIDEO_VULKAN=ON \
    -DSDL_SSE3=OFF \
    -DSDL_RPATH=OFF \
    -DSDL_STATIC=ON \
    -DSDL_STATIC_PIC=ON \
%ifarch ppc64le
    -DSDL_ALTIVEC=OFF \
%endif

%cmake_build

%install
%cmake_install

# Rename SDL_config.h to SDL_config-<arch>.h to avoid file conflicts on
# multilib systems and install SDL_config.h wrapper
mv %{buildroot}%{_includedir}/SDL2/SDL_config.h %{buildroot}%{_includedir}/SDL2/SDL_config-%{_arch}.h
install -p -m 644 %{SOURCE1} %{buildroot}%{_includedir}/SDL2/SDL_config.h

# Rename SDL_revision.h to SDL_revision-<arch>.h to avoid file conflicts on
# multilib systems and install SDL_revision.h wrapper
# TODO: Figure out how in the hell the SDL_REVISION changes between architectures on the same SRPM.
mv %{buildroot}%{_includedir}/SDL2/SDL_revision.h %{buildroot}%{_includedir}/SDL2/SDL_revision-%{_arch}.h
install -p -m 644 %{SOURCE2} %{buildroot}%{_includedir}/SDL2/SDL_revision.h

%files
%license LICENSE.txt
%doc BUGS.txt CREDITS.txt README-SDL.txt
%{_libdir}/libSDL2-2.0.so.0*

%files devel
%doc README.md TODO.txt WhatsNew.txt
%{_bindir}/*-config
%{_libdir}/lib*.so
%{_libdir}/libSDL2main.a
%{_libdir}/pkgconfig/sdl2.pc
%dir %{_libdir}/cmake/SDL2
%{_libdir}/cmake/SDL2/SDL2Config*.cmake
%{_libdir}/cmake/SDL2/SDL2Targets*.cmake
%{_libdir}/cmake/SDL2/SDL2mainTargets*.cmake
%{_libdir}/cmake/SDL2/sdlfind.cmake
%{_includedir}/SDL2
%{_datadir}/aclocal/*
%{_libdir}/libSDL2_test.a
%{_libdir}/cmake/SDL2/SDL2testTargets*.cmake

%files static
%license LICENSE.txt
%{_libdir}/libSDL2.a
%{_libdir}/cmake/SDL2/SDL2staticTargets*.cmake

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.28.5-1
- Import
