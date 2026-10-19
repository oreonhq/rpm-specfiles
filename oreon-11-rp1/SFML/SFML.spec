%global source0_hash 4a76170c75daabf9a05807ea838e63f93fbb34efa7b5f60bfc2b508f8cb06b6e
Name:           SFML
Version:        3.1.0
Release:        1%{?dist}
Summary:        Simple and Fast Multimedia Library
License:        Zlib AND Apache-2.0 AND CC0-1.0 AND MIT AND (MIT AND Apache-2.0) AND LicenseRef-Fedora-Public-Domain
URL:            http://www.sfml-dev.org/
Source0:        https://www.sfml-dev.org/files/%{name}-%{version}-sources.zip
Provides:       bundled(miniaudio)
Provides:       bundled(dr_mp3)
Provides:       bundled(stb_image)
Provides:       bundled(qoi)
Provides:       bundled(glad)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mbedtls)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
# /oreon:deps
%description
SFML is a portable and easy to use multimedia API written in C++. You can see
it as a modern, object-oriented alternative to SDL.
SFML is composed of several packages to perfectly suit your needs. You can use
SFML as a minimal windowing system to interface with OpenGL, or as a
fully-featured multimedia library for building games or interactive programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cmake
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# fixup non needed executable permission on regular files
find -type f -print0 | xargs -0 chmod -x

# drop Windows-only bundled headers
rm -r extlibs/headers/mingw extlibs/headers/wepoll

%build

%cmake -DSFML_BUILD_DOC=TRUE
%cmake_build
%install
%cmake_install
%oreon_autofiles SFML-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SFML-devel -f %{oreon_filedir}/SFML-devel.list

%changelog

%autochangelog
