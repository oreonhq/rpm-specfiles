%global source0_hash 332cb37d0be20cb9541739c61f79bae5a477427d79ae85e352089afdaf6666e4
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif
%global libdecor_majver 0
Name:           SDL2
Version:        2.28.5
Release:        1%{?dist}
Summary:        Cross-platform multimedia library
License:        Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 OR MIT)
URL:            https://www.libsdl.org/
Source0:        https://www.libsdl.org/release/SDL2-2.28.5.tar.gz
Source1:        SDL_config.h
Source2:        SDL_revision.h
Patch0:         multilib.patch
Patch1:         SDL2-2.0.22-prefer-wayland.patch
Requires:       (libdecor-%{libdecor_majver}.so.%{libdecor_majver}%{libsymbolsuffix} if libwayland-client)
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libdrm-devel
BuildRequires:  make
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libgbm-devel
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
Requires:       mesa-libEGL-devel%{?_isa}
Requires:       mesa-libGLES-devel%{?_isa}
Requires:       libX11-devel%{?_isa}
Conflicts:      %{name}-static < 2.0.18-4
%description devel
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library designed
to provide fast access to the graphics frame buffer and audio device. This
package provides the libraries, include files, and other resources needed for
developing SDL applications.

%package static
Summary:        Static libraries for SDL2
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Conflicts:      %{name}-devel < 2.0.18-4
%description static
Static libraries for SDL2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git
sed -i -e 's/\r//g' TODO.txt README.md WhatsNew.txt BUGS.txt LICENSE.txt CREDITS.txt README-SDL.txt

%build

export LDFLAGS="%{shrink:%{build_ldflags}}"
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DSDL_DLOPEN=ON \
    -DSDL_VIDEO_KMSDRM=ON \
    -DSDL_ARTS=OFF \
    -DSDL_ESD=OFF \
    -DSDL_NAS=OFF \
    -DSDL_PULSEAUDIO_SHARED=ON \
    -DSDL_JACK_SHARED=ON \
    -DSDL_PIPEWIRE=OFF \
    -DSDL_PIPEWIRE_SHARED=OFF \
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
mv %{buildroot}%{_includedir}/SDL2/SDL_config.h %{buildroot}%{_includedir}/SDL2/SDL_config-%{_arch}.h
install -p -m 644 %{SOURCE1} %{buildroot}%{_includedir}/SDL2/SDL_config.h
mv %{buildroot}%{_includedir}/SDL2/SDL_revision.h %{buildroot}%{_includedir}/SDL2/SDL_revision-%{_arch}.h
install -p -m 644 %{SOURCE2} %{buildroot}%{_includedir}/SDL2/SDL_revision.h
%oreon_autofiles SDL2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles SDL2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n SDL2-devel -f %{oreon_filedir}/SDL2-devel.list
%files -n SDL2-static -f %{oreon_filedir}/SDL2-static.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.28.5-1
- Import
