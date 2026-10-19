%global source0_hash b85ab92280c30d22f5c8fe2f68b809cddb7eaac437d8c33474475dac84ddc574
%global vips_version_base 8.18
%global vips_version %{vips_version_base}.0
%global vips_soname_major 42
Name:		vips
Version:	%{vips_version}
Release:        1%{?dist}
Summary:        C/C++ library for processing large images
License:	LGPL-2.1-or-later
URL:		https://www.libvips.org/
Source0:        https://github.com/libvips/libvips/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:		pr-4816.patch
Patch1:		pr-4836.patch
Provides:	bundled(libnsgif)
Recommends: %{name}-jxl
Recommends: %{name}-heif
Recommends: %{name}-magick
Recommends: %{name}-openslide
Recommends: %{name}-poppler
# oreon:deps
BuildRequires:  bc
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  nifticlib-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Imath)
BuildRequires:  pkgconfig(MagickWand)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(cgif)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(imagequant)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libhwy)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(matio)
BuildRequires:  pkgconfig(openslide)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
VIPS is an image processing library. It is good for very large images
(even larger than the amount of RAM in your machine), and for working
with color.

This package should be installed if you want to use a program compiled
against VIPS.

%package devel
Summary:	Development files for %{name}
Requires:	vips%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains the header files and
libraries necessary for developing programs using VIPS.

%package tools
Summary:	Command-line tools for %{name}
Requires:	vips%{?_isa} = %{version}-%{release}
%description tools
The %{name}-tools package contains command-line tools for working with VIPS.

%package doc
Summary:	Documentation for %{name}
BuildArch:	noarch
Conflicts:	%{name} < %{version}-%{release}, %{name} > %{version}-%{release}
%description doc
The %{name}-doc package contains extensive HTML documentation about VIPS and
its C++ API.

%package jxl
Summary:	JPEG XL support for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description jxl
The %{name}-jxl package contains the jxl module for VIPS, providing JPEG XL
support.

%package heif
Summary:	HEIF support for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description heif
The %{name}-heif package contains the heif module for VIPS, providing AVIF
support.

%package openslide
Summary:	OpenSlide support for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description openslide
The %{name}-openslide package contains the OpenSlide module for VIPS.

%package poppler
Summary:	Poppler support for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description poppler
The %{name}-poppler package contains the Poppler module for VIPS.

%package magick
Summary:	Magick support for %{name} using ImageMagick7
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description magick
The %{name}-magick package contains the Magick module for VIPS using
ImageMagick7.

%prep
%oreon_prep
%build

export CFLAGS="%{optflags} -ftree-vectorize"
export CXXFLAGS="%{optflags} -ftree-vectorize"
%meson \
    -Dnifti-prefix-dir=/usr \
    -Dcpp-docs=true \
    -Ddocs=true \
    -Dpdfium=disabled \
    -Duhdr=disabled \
    %{nil}
%meson_build
%install
%meson_install
%find_lang vips%{vips_version_base}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n vips-devel -f %{oreon_filedir}/vips-devel.list
%files -n vips-tools -f %{oreon_filedir}/vips-tools.list
%files -n vips-doc -f %{oreon_filedir}/vips-doc.list
%files -n vips-jxl -f %{oreon_filedir}/vips-jxl.list
%files -n vips-heif -f %{oreon_filedir}/vips-heif.list
%files -n vips-openslide -f %{oreon_filedir}/vips-openslide.list
%files -n vips-poppler -f %{oreon_filedir}/vips-poppler.list
%files -n vips-magick -f %{oreon_filedir}/vips-magick.list

%changelog

%autochangelog
