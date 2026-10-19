%global source0_hash 19d6dbd9c901c74441d9888c13cb1399f614fe8993d59062a72cfbceb00fed04
Name:           SFML2
Version:        2.6.2
Release:        1%{?dist}
Summary:        Simple and Fast Multimedia Library, 2.x compatibility version
License:        Zlib AND Apache-2.0 AND CC0-1.0 AND MIT AND (MIT AND Apache-2.0) AND LicenseRef-Fedora-Public-Domain
URL:            http://www.sfml-dev.org/
Source0:        https://www.sfml-dev.org/files/SFML-%{version}-sources.zip
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  stb_image-devel
BuildRequires:  stb_image_write-devel
# /oreon:deps
%description
SFML is a portable and easy to use multimedia API written in C++. You can see
it as a modern, object-oriented alternative to SDL.
This is the 2.x series kept for applications not yet ported to SFML 3.
SFML is composed of several packages to perfectly suit your needs. You can use
SFML as a minimal windowing system to interface with OpenGL, or as a
fully-featured multimedia library for building games or interactive programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cmake
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that still use the SFML 2.x API.
Headers are in %{_includedir}/SFML2, the CMake config in
%{_libdir}/cmake/SFML2 and pkg-config files in %{_libdir}/SFML2/pkgconfig.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n SFML-%{version} -p1
# fixup non needed executable permission on regular files
find -type f -print0 | xargs -0 chmod -x

# use system-wide extlibs; so, delete everything except glad, minimp3 and vulkan header files
pushd extlibs
shopt -s extglob
rm -r !(headers)
cd headers/
rm -r !(glad|minimp3|vulkan)
shopt -u extglob
popd

%build

%cmake -DSFML_BUILD_DOC=FALSE -DCMAKE_INSTALL_INCLUDEDIR=include/SFML2 -DSFML_MISC_INSTALL_PREFIX=%{_datadir}/doc/SFML2
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_libdir}/cmake/SFML %{buildroot}%{_libdir}/cmake/SFML2
mkdir -p %{buildroot}%{_libdir}/SFML2
mv %{buildroot}%{_libdir}/pkgconfig %{buildroot}%{_libdir}/SFML2/pkgconfig
sed -i 's|^libdir=.*|libdir=%{_libdir}/SFML2|;s|^includedir=.*|includedir=%{_includedir}/SFML2|' %{buildroot}%{_libdir}/SFML2/pkgconfig/*.pc
for l in %{buildroot}%{_libdir}/libsfml-*.so; do
  ln -s ../$(readlink $l) %{buildroot}%{_libdir}/SFML2/$(basename $l)
  rm $l
done
%oreon_autofiles SFML2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SFML2-devel -f %{oreon_filedir}/SFML2-devel.list

%changelog

%autochangelog
