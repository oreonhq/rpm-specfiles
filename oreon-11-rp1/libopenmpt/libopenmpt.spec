# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 caa2fa959e389f4374d9e2df3af5c633452c12dd80442cba2e89cb7ff2b93c5b
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name: libopenmpt
Version: 0.8.6
Release: 1%{?dist}

%global tar_root %{name}-%{version}+release.autotools

License: BSD-3-Clause
Summary: C/C++ library to decode tracker music module (MOD) files

URL: https://lib.openmpt.org/libopenmpt/

Source0: https://lib.openmpt.org/files/libopenmpt/src/%{tar_root}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: chrpath
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(zlib)

# for command-line player audio output
BuildRequires: pulseaudio-libs-devel
# don't build with niche options
#BuildRequires: portaudio-devel
#BuildRequires: SDL-devel
#BuildRequires: SDL2-devel

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
%oreon_verify_sources
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


%files -n openmpt123
%{_bindir}/openmpt123
%{_mandir}/man1/*

%files
%license LICENSE
%{_libdir}/*.so.0*
%{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/examples

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_docdir}/%{name}/examples/


%changelog
* Sun Apr 19 2026 Brandon Lester <blester@oreonhq.com> - 0.8.6-1
- import
