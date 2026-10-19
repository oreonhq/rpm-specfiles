%global source0_hash 63547d58d0185c833213885b635a2c0548201cc8f301e6587c0be1a67e1e045d
Name:       SDL3_ttf
Version:    3.2.2
Release:        1%{?dist}
Summary:        Support for TrueType (.ttf) font files with Simple Directmedia Layer
License:    Zlib AND MIT
URL:        https://github.com/libsdl-org/SDL_ttf
Source0:        https://github.com/libsdl-org/SDL_ttf/releases/download/release-%{version}/%{name}-%{version}.tar.gz
Patch0:     https://github.com/libsdl-org/SDL_ttf/commit/81c273d952b9946a48b99e990c66fb49a76de9b5.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(SDL3)
BuildRequires:  cmake(zlib)
BuildRequires:  dejavu-sans-fonts
BuildRequires:  dos2unix
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  harfbuzz-devel
BuildRequires:  libGL-devel
BuildRequires:  perl-base
BuildRequires:  plutosvg-devel
# /oreon:deps
%description
This library is a wrapper around the FreeType and Harfbuzz libraries, allowing
you to use TrueType fonts to render text in SDL applications.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:   SDL3-devel%{?_isa}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

dos2unix CHANGES.txt README.md

%build

%cmake \
    -DSDLTTF_HARFBUZZ:BOOL=ON \
    -DSDLTTF_INSTALL:BOOL=ON \
    -DSDLTTF_INSTALL_CPACK:BOOL=ON \
    -DSDLTTF_INSTALL_MAN:BOOL=ON \
    -DSDLTTF_PLUTOSVG:BOOL=ON \
    -DSDLTTF_RELOCATABLE:BOOL=OFF \
    -DSDLTTF_SAMPLES:BOOL=ON \
    -DSDLTTF_SAMPLES_INSTALL:BOOL=ON \
    -DSDLTTF_STRICT:BOOL=ON \
    -DSDLTTF_VENDORED:BOOL=OFF \
    -DSDLTTF_WERROR:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles SDL3_ttf-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

env -C %{_vpath_builddir}/ SDL_VIDEODRIVER=dummy ./showfont --dump /usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf
file %{_vpath_builddir}/glyph-100.bmp | grep -q "PC bitmap, Windows 3.x format"
%files -f %{oreon_filedir}/main.list
%files -n SDL3_ttf-devel -f %{oreon_filedir}/SDL3_ttf-devel.list

%changelog

%autochangelog
