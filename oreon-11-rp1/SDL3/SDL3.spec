# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f3bb06f55bed9557227a700af2ea62e49497ebdf58037732a731a5fb3ef8581f
%global source1_hash 776200b5c71f8c0168c0e89d8fb78103623dc15e284e9daf0a0eceb4e43d5533
%global source10_hash 0ee36c0330b7273f46deda3e98bd8e5ecf891f4a40854ac1fd0817f31d1e2953
%global source2_hash a93347116e97b14d8d0ad66709b889f21eedede2388f661b1db95274bc2ef52a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif

%global libdecor_majver 0

%if 0%{?rhel}
%bcond_with static
%bcond_with xscrnsaver
%else
%bcond_without static
%bcond_without xscrnsaver
%endif

Name:           SDL3
Version:        3.4.20
Release:        1%{?dist}
Summary:        Cross-platform multimedia library
License:        Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 OR MIT)
URL:            http://www.libsdl.org/

Source0:        http://www.libsdl.org/release/%{name}-%{version}.tar.gz
Source1:        http://www.libsdl.org/release/%{name}-%{version}.tar.gz.sig
Source2:        SDL3.pgp

Source10:       SDL3_revision.h

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  gnupg2
BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  alsa-lib-devel
BuildRequires:  fribidi-devel
BuildRequires:  libthai-devel
BuildRequires:  liburing-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  libXext-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
%if %{with xscrnsaver}
BuildRequires:  libXScrnSaver-devel
%endif
BuildRequires:  libXinerama-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXfixes-devel
BuildRequires:  systemd-devel
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(dbus-1)
%if !0%{?oreon}
BuildRequires:  pkgconfig(ibus-1.0)
%endif
BuildRequires:  pkgconfig(libdecor-%{libdecor_majver})
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libdrm-devel
BuildRequires:	libXtst-devel

Requires:       (libdecor-%{libdecor_majver}.so.%{libdecor_majver}%{libsymbolsuffix} if libwayland-client)

Provides:       bundled(hidraw)

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
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source10_hash}  %{SOURCE10}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -S git_am
sed -e 's/\r//g' -i README.md WhatsNew.txt BUGS.txt LICENSE.txt CREDITS.md

%build
export LDFLAGS="%{shrink:%{build_ldflags}}"

%cmake \
    -DSDL_INSTALL_DOCS=ON \
%if 0%{?oreon}
    -DSDL_IBUS=OFF \
%endif
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
install -p -m 644 %{SOURCE10} %{buildroot}%{_includedir}/SDL3/SDL_revision.h

%check
%ctest

%files
%license LICENSE.txt
%doc BUGS.txt CREDITS.md README.md
%{_libdir}/libSDL3.so.0{,.*}

%files devel
%doc README.md WhatsNew.txt
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/sdl3.pc
%dir %{_libdir}/cmake/SDL3
%{_libdir}/cmake/SDL3/SDL3Config*.cmake
%{_libdir}/cmake/SDL3/SDL3headersTargets*.cmake
%{_libdir}/cmake/SDL3/SDL3sharedTargets*.cmake
%{_includedir}/SDL3
%{_mandir}/man3/SDL*.3*

%if %{with static}
%files static
%license LICENSE.txt
%{_libdir}/libSDL3.a
%{_libdir}/cmake/SDL3/SDL3staticTargets*.cmake
%endif

%files test
%license LICENSE.txt
%{_libdir}/libSDL3_test.a
%{_libdir}/cmake/SDL3/SDL3testTargets*.cmake

%changelog
%autochangelog
