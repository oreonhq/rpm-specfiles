%global source0_hash 1644308279a975799049e4826af2cfc787cad2abb11aa14562e402521f86992a
Name:		SDL_mixer
Version:	1.2.12
Release:        37%{?dist}
Summary:        Simple DirectMedia Layer - Sample Mixer Library
License:	LGPL-2.0-only
URL:		http://www.libsdl.org/projects/SDL_mixer/
Source0:        http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz
Patch0:         SDL_mixer-MikMod-1.patch
Patch1:         SDL_mixer-MikMod-2.patch
Patch2:         SDL_mixer-c99.patch
Patch3:         SDL_mixer-fix-double-free.patch
Requires:	libvorbis
Requires:	libmikmod
Requires:	fluidsynth
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  flac-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  mikmod-devel
# /oreon:deps
%description
A simple multi-channel audio mixer for SDL. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD, Timidity MIDI and Ogg Vorbis libraries.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.10
Requires:	libvorbis-devel
Requires:	libmikmod-devel
Requires:	fluidsynth-devel
Requires:	pkgconfig
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-dependency-tracking	\
	   --disable-static 			\
	   --enable-music-libmikmod
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} LDFLAGS=-lm
%install
%makeinstall install-bin
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles SDL_mixer-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SDL_mixer-devel -f %{oreon_filedir}/SDL_mixer-devel.list

%changelog

%autochangelog
