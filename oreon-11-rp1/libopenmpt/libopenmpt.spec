%global source0_hash d7ce84fd05d686c4bcf66af40eae857afa371442db60eeda3f874bd6cf6fc318
Name: libopenmpt
Version: 0.8.9
Release:        1%{?dist}
%global tar_root %{name}-%{version}+release.autotools
License: BSD-3-Clause
Summary:        C/C++ library to decode tracker music module (MOD) files
URL: https://lib.openmpt.org/libopenmpt/
Source0:        https://lib.openmpt.org/files/%{name}/src/%{tar_root}.tar.gz
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
libopenmpt is a cross-platform C++ and C library to decode tracked music
files (modules) into a raw PCM audio stream.

libopenmpt is based on the player code of the OpenMPT project (Open
ModPlug Tracker). In order to avoid code base fragmentation, libopenmpt is
developed in the same source code repository as OpenMPT.

%package -n openmpt123
Summary: Command-line tracker music player based on libopenmpt
Group: Applications/Multimedia
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n openmpt123
Openmpt123 is a cross-platform command-line or terminal based player
for tracker music (MOD) module files.

%package devel
Summary: Development files for the libopenmpt library
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files needed when building software which uses libopenmpt.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{tar_root}
sed -i 's/\r$//' LICENSE

%build

%configure  \
  --disable-static  \
  --without-sdl --without-sdl2 \
  --without-portaudio --without-portaudiocpp
make %{?_smp_mflags}
%install
%make_install
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
chrpath --delete ${RPM_BUILD_ROOT}%{_bindir}/openmpt123
%oreon_autofiles openmpt123 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n openmpt123 -f %{oreon_filedir}/openmpt123.list
%files -n libopenmpt-devel -f %{oreon_filedir}/libopenmpt-devel.list

%changelog

%autochangelog
