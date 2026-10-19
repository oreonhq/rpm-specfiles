%global source0_hash 47efbf42c77c19a05d22e627d42873e991ec0c1357219c0d74ce6a2948cb2def
%{?mingw_package_header}
%global datetag 20210406
Name:           mingw-portaudio
Version:        19
Release:        1%{?dist}
Summary:        Free, cross platform, open-source, audio I/O library
License:        LGPL-2.0-or-later
URL:            http://www.portaudio.com/
Source0:        http://files.portaudio.com/archives/pa_stable_v%{version}0700_%{datetag}.tgz
Patch3:         portaudio-audacity.patch
Patch100:       portaudio-mingw64.patch
Patch101:       portaudio-win-headers.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
PortAudio is a portable audio I/O library designed for cross-platform support of
audio. It uses a callback mechanism to request audio processing. Audio can be
generated in various formats, including 32 bit floating point, and will be
converted to the native format internally.

%package -n mingw32-portaudio
Summary:        Free, cross platform, open-source, audio I/O library
%description -n mingw32-portaudio
PortAudio is a portable audio I/O library designed for cross-platform support of
audio. It uses a callback mechanism to request audio processing. Audio can be
generated in various formats, including 32 bit floating point, and will be
converted to the native format internally.

# Win64
%package -n mingw64-portaudio
Summary:       MinGW compiled portaudio for the Win64 target
%description -n mingw64-portaudio
MinGW compiled portaudio for the Win64 target.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n portaudio -p1
autoreconf -fiv

%build

%mingw_configure \
  --enable-shared --disable-static \
  --with-winapi=directx,wdmks,wmme,wasapi
%mingw_make_build
%install
%mingw_make_install
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-portaudio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-portaudio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-portaudio -f %{oreon_filedir}/mingw32-portaudio.list
%files -n mingw64-portaudio -f %{oreon_filedir}/mingw64-portaudio.list

%changelog

%autochangelog
