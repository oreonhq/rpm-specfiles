%global source0_hash 1644308279a975799049e4826af2cfc787cad2abb11aa14562e402521f86992a

Name:		SDL_mixer
Version:	1.2.12
Release:	37%{?dist}
Summary:	Simple DirectMedia Layer - Sample Mixer Library

License:	LGPL-2.0-only
URL:		http://www.libsdl.org/projects/SDL_mixer/
Source0:	http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz

# MikMod-related fixes from trunk
Patch0:         SDL_mixer-MikMod-1.patch
Patch1:         SDL_mixer-MikMod-2.patch
Patch2:         SDL_mixer-c99.patch
Patch3:         SDL_mixer-fix-double-free.patch

BuildRequires:	gcc make
BuildRequires:	SDL-devel >= 1.2.10 
BuildRequires:	libvorbis-devel
BuildRequires:	flac-devel
BuildRequires:	mikmod-devel >= 3.1.10
BuildRequires:	fluidsynth-devel
# Require libvorbis since we build it with dynamically load support.
Requires:	libvorbis
Requires:	libmikmod
Requires:	fluidsynth

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

%autosetup -p1

%build
%configure --disable-dependency-tracking	\
	   --disable-static 			\
	   --enable-music-libmikmod

# Remove rpath as per https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# Upstream bug for proper fixing of the lack of -lm:
# http://bugzilla.libsdl.org/show_bug.cgi?id=1010
make %{?_smp_mflags} LDFLAGS=-lm

%install
%makeinstall install-bin

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc README CHANGES
%license COPYING
%{_bindir}/playmus
%{_bindir}/playwave
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/SDL

%changelog
%autochangelog
