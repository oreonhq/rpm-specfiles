# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c20492bc8ebb96c87fa2e52a0926e1cda8cde95d66145e018ac713fed5da38cf

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global gs_tag 10080
%global urw_fontdir %{_fontbasedir}/urw-base35

Name:           ghostscript
Version:        10.08.0
Release:        1%{?dist}
Summary:        Interpreter for PostScript language and PDF
License:        AGPL-3.0-or-later AND MIT AND Apache-2.0
URL:            https://ghostscript.com/
Source0:        https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs%{gs_tag}/ghostscript-%{version}.tar.xz

BuildRequires:  brotli-devel
BuildRequires:  cups-devel
BuildRequires:  dbus-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  jbig2dec-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpaper-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  openjpeg-devel
BuildRequires:  oreon-rpm-macros
BuildRequires:  pkgconf
BuildRequires:  urw-base35-fonts
BuildRequires:  zlib-devel

Requires:       libgs%{?_isa} = %{version}-%{release}

%description
Ghostscript is a suite of software based on an interpreter for Adobe Systems'
PostScript and Portable Document Format (PDF) page description languages. Its
primary purpose includes the rasterization or rendering of such page
descriptions into either raster images or high level page description
languages, as well as conversion between the two.

%package -n     libgs
Summary:        Ghostscript shared library and its data files
Requires:       urw-base35-fonts
Requires:       fontconfig
Provides:       bundled(lcms2mt)
Provides:       bundled(ijs)
Provides:       bundled(extract)

%description -n libgs
The Ghostscript interpreter as a shared library together with the resource
files, ICC profiles and PostScript library files that it needs at run time.

%package -n     libgs-devel
Summary:        Development files for the Ghostscript library
Requires:       libgs%{?_isa} = %{version}-%{release}

%description -n libgs-devel
Header files and the shared library link for developing applications that use
the Ghostscript interpreter library.

%package        x11
Summary:        Ghostscript front end with X11 display support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    x11
The gsx program, a Ghostscript front end that is able to open X11 windows to
display the rendered pages.

%package        doc
Summary:        Documentation for Ghostscript
BuildArch:      noarch

%description    doc
The Ghostscript manual, the color management guide and the release notes.

%prep
%oreon_sha256
%autosetup

rm -rf brotli freetype jbig2dec jpeg leptonica libpng openjpeg tesseract tiff zlib

%build
%configure \
        --enable-cups \
        --enable-dbus \
        --enable-fontconfig \
        --enable-freetype \
        --enable-openjpeg \
        --disable-gtk \
        --with-fontpath=%{urw_fontdir} \
        --with-ijs \
        --with-jbig2dec \
        --with-libpaper \
        --with-system-libtiff \
        --with-x \
        --without-libidn \
        --without-tesseract
%make_build so

%install
make DESTDIR=%{buildroot} soinstall

mv %{buildroot}%{_bindir}/gsc %{buildroot}%{_bindir}/gs

for font in %{buildroot}%{_datadir}/ghostscript/%{version}/Resource/Font/*; do
  name=$(basename "$font")
  ln -sf "%{urw_fontdir}/$name.t1" "$font"
done

%check
for font in %{buildroot}%{_datadir}/ghostscript/%{version}/Resource/Font/*; do
  test -e "$font"
done

export LD_LIBRARY_PATH=$PWD/sobin
gs="./sobin/gsc -q -dNOPAUSE -dBATCH -dSAFER -I./lib -I./Resource/Init -sGenericResourceDir=./Resource/"
mkdir gstest

$gs -sDEVICE=pdfwrite -sOutputFile=gstest/tiger.pdf examples/tiger.eps
test -s gstest/tiger.pdf
head -c 5 gstest/tiger.pdf | grep -q '%%PDF-'

$gs -sDEVICE=png16m -r72 -sOutputFile=gstest/tiger.png gstest/tiger.pdf
test -s gstest/tiger.png

$gs -sDEVICE=tiff24nc -sOutputFile=gstest/tiger.tif examples/tiger.eps
test -s gstest/tiger.tif

$gs -sDEVICE=jpeg -sOutputFile=gstest/tiger.jpg examples/tiger.eps
test -s gstest/tiger.jpg

$gs -sDEVICE=pwgraster -sOutputFile=gstest/tiger.pwg examples/tiger.eps
test -s gstest/tiger.pwg

$gs -sDEVICE=txtwrite -sOutputFile=gstest/alphabet.txt examples/alphabet.ps
grep -q '0123456789' gstest/alphabet.txt

%ldconfig_scriptlets -n libgs

%files
%license LICENSE
%{_bindir}/gs
%{_bindir}/dvipdf
%{_bindir}/eps2eps
%{_bindir}/gsbj
%{_bindir}/gsdj
%{_bindir}/gsdj500
%{_bindir}/gslj
%{_bindir}/gslp
%{_bindir}/gsnd
%{_bindir}/lprsetup.sh
%{_bindir}/pdf2dsc
%{_bindir}/pdf2ps
%{_bindir}/pf2afm
%{_bindir}/pfbtopfa
%{_bindir}/pphs
%{_bindir}/printafm
%{_bindir}/ps2ascii
%{_bindir}/ps2epsi
%{_bindir}/ps2pdf
%{_bindir}/ps2pdf12
%{_bindir}/ps2pdf13
%{_bindir}/ps2pdf14
%{_bindir}/ps2pdfwr
%{_bindir}/ps2ps
%{_bindir}/ps2ps2
%{_bindir}/unix-lpr.sh
%{_mandir}/man1/*.1*

%files -n libgs
%license LICENSE
%{_libdir}/libgs.so.10*
%dir %{_datadir}/ghostscript
%{_datadir}/ghostscript/%{version}

%files -n libgs-devel
%{_includedir}/ghostscript
%{_libdir}/libgs.so

%files x11
%{_bindir}/gsx

%files doc
%{_docdir}/ghostscript

%changelog
%autochangelog
