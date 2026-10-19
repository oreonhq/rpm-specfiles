%global source0_hash 5af29ba58bbdbb7bbcefaaecc77ec8fc413f0db6f4c4e286c40c3e1b83174fa0
Name:           portaudio
Version:        19.7.0
Release:        1%{?dist}
Summary:        Free, cross platform, open-source, audio I/O library
License:        MIT
URL:            http://www.portaudio.com/
VCS:            https://github.com/PortAudio/portaudio
Source0:        https://github.com/PortAudio/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          portaudio-pkgconfig-alsa.patch
Patch:          portaudio-audacity.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

%package devel
Summary:        Development files for the portaudio audio I/O library
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

This package contains files required to build applications that will use the
portaudio library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
# Needed for patch3
autoreconf -fiv
# With autoconf-2.71 we need to run this twice for things to work ?? (rhbz#1943118)
autoreconf -fiv

%build

%configure --disable-static --enable-cxx
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' bindings/cpp/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' bindings/cpp/libtool
make
doxygen
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n portaudio-devel -f %{oreon_filedir}/portaudio-devel.list

%changelog

%autochangelog
