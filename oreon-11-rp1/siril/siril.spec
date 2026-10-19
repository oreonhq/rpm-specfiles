%global source0_hash b1682f2129d2e06b034445ed225766a06e38cfaa7451b92d606a3ee36eb077a4
ExcludeArch:    %{ix86}
Name:           siril
Version:        1.4.4
Release:        1%{?dist}
Summary:        Astronomical image processing software
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND BSL-1.0 AND Zlib
URL:            https://siril.org
Source0:        https://free-astro.org/download/%{name}-%{version}.tar.bz2
Recommends:     gvfs
Recommends:     python3dist(astropy-healpix)
Provides:       bundled(htmesh) = 1.0.0
Provides:       bundled(kplot) = 0.1.14
# oreon:deps
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg-free-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(healpix_cxx)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxisf)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(rtprocess)
BuildRequires:  pkgconfig(wcslib)
BuildRequires:  pkgconfig(yyjson)
# /oreon:deps
%description
Siril is an image processing tool specially tailored for noise reduction and
improving the signal/noise ratio of an image from multiple captures, as
required in astronomy. Siril can align automatically or manually, stack and
enhance pictures from various file formats, even images sequences (movies and
SER files)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove bundled subprojects
# just to be sure we're not accidentally use them
rm -rf subprojects/healpix_cxx
rm -rf subprojects/librtprocess
rm -rf subprojects/wcslib
rm -rf subprojects/yyjson

%build

%meson \
    -Drelocatable-bundle=no
%meson_build
%install
%meson_install
rm -rf %{buildroot}%{_pkgdocdir}/python_module/locale
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.siril.Siril.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.siril.Siril.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
