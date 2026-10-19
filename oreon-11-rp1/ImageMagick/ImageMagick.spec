%global source1_hash 01aee712e8b65d567f7301eded87cf015936b5e4ad52e950d7a1362509a7f903
%global source0_hash 9f32b378f14e6a5357b5b901351ebe8d8c8b86e6b7a4299b3c95336ecfc92642
%bcond_without tests
%bcond_without libheif
%if 0%{?flatpak}
%bcond_with perl
%else
%bcond_without perl
%endif
%global __brp_remove_la_files %nil
Name:           ImageMagick
Epoch:          1
Version:        7.1.2.32
Release:        1%{?dist}
Summary:        An X application for displaying and manipulating images
%global VER %(foo=%{version}; echo ${foo:0:5})
%global Patchlevel %(foo=%{version}; echo ${foo:6})
%global libsover 10
%global subsover VERS_10.0
%global libcxxsover 5
License:        ImageMagick
URL:            https://imagemagick.org/
Source0:        https://download.imagemagick.org/archive/releases/%{name}-%{VER}-%{Patchlevel}.tar.xz
Source1:        https://download.imagemagick.org/archive/releases/%{name}-%{VER}-%{Patchlevel}.tar.xz.asc
Source2:        ImageMagick.keyring
%if %{with perl}
%endif
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}7            < %{epoch}:%{version}-%{release}
Provides:       %{name}7            = %{epoch}:%{version}-%{release}
Provides:       perl(Image::Magick)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  giflib-devel
BuildRequires:  gnupg2
BuildRequires:  jbigkit-devel
BuildRequires:  libgs-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(jasper)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcgraph)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libuhdr)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwmf)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lqr-1)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(raqm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  urw-base35-fonts-devel
# /oreon:deps
%description
ImageMagick is an image display and manipulation tool for the X
Window System. ImageMagick can read and write JPEG, TIFF, PNM, GIF,
and Photo CD image formats. It can resize, rotate, sharpen, color
reduce, or add special effects to an image, and when finished you can
either save the completed work in the original format or a different
one. ImageMagick also includes command line programs for creating
animated or transparent .gifs, creating composite images, creating
thumbnail images, and more.

ImageMagick is one of your choices if you need a program to manipulate
and display images. If you want to develop your own applications
which use ImageMagick code or APIs, you need to install
ImageMagick-devel as well.

%package devel
Summary:        Library links and header files for ImageMagick app development
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}7-devel       < %{epoch}:%{version}-%{release}
Provides:       %{name}7-devel       = %{epoch}:%{version}-%{release}
%description devel
ImageMagick-devel contains the library links and header files you'll
need to develop ImageMagick applications. ImageMagick is an image
manipulation program.

If you want to create applications that will use ImageMagick code or
APIs, you need to install ImageMagick-devel as well as ImageMagick.
You do not need to install it if you just want to use ImageMagick,
however.

%package libs
Summary: ImageMagick libraries to link with
Obsoletes: %{name}7-libs < %{epoch}:%{version}-%{release}
Provides:  %{name}7-libs = %{epoch}:%{version}-%{release}
Recommends: urw-base35-fonts
Recommends: open-sans-fonts
%description libs
This packages contains a shared libraries to use within other applications.

%package djvu
Summary: DjVu plugin for ImageMagick
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: %{name}7-djvu       < %{epoch}:%{version}-%{release}
Provides:  %{name}7-djvu       = %{epoch}:%{version}-%{release}
%description djvu
This packages contains a plugin for ImageMagick which makes it possible to
save and load DjvU files from ImageMagick and libMagickCore using applications.

%if %{with libheif}
%package heic
Summary: HEIC plugin for ImageMagick
BuildRequires:  pkgconfig(libheif) >= 1.4.0
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description heic
This packages contains a plugin for ImageMagick which makes it possible to
save and load HEIC files from ImageMagick and libMagickCore using applications.
%endif

%package doc
Summary: ImageMagick html documentation
Obsoletes: %{name}7-doc < %{epoch}:%{version}-%{release}
Provides:  %{name}7-doc = %{epoch}:%{version}-%{release}
%description doc
ImageMagick documentation, this package contains usage (for the
commandline tools) and API (for the libraries) documentation in html format.
Note this documentation can also be found on the ImageMagick website:
http://www.imagemagick.org/

%if %{with perl}
%package perl
Summary:        ImageMagick perl bindings
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}7-perl        < %{epoch}:%{version}-%{release}
Provides:       %{name}7-perl        = %{epoch}:%{version}-%{release}
%description perl
Perl bindings to ImageMagick.

Install ImageMagick-perl if you want to use any perl scripts that use
ImageMagick.
%endif

%package c++
Summary:        ImageMagick Magick++ library (C++ bindings)
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}7-c++         < %{epoch}:%{version}-%{release}
Provides:       %{name}7-c++         = %{epoch}:%{version}-%{release}
%description c++
This package contains the Magick++ library, a C++ binding to the ImageMagick
graphics manipulation library.

Install ImageMagick-c++ if you want to use any applications that use Magick++.

%package c++-devel
Summary:        C++ bindings for the ImageMagick library
Requires:       %{name}-c++%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}7-c++-devel    < %{epoch}:%{version}-%{release}
Provides:       %{name}7-c++-devel    = %{epoch}:%{version}-%{release}
%description c++-devel
ImageMagick-devel contains the static libraries and header files you'll
need to develop ImageMagick applications using the Magick++ C++ bindings.
ImageMagick is an image manipulation program.

If you want to create applications that will use Magick++ code
or APIs, you'll need to install ImageMagick-c++-devel, ImageMagick-devel and
ImageMagick.
You don't need to install it if you just want to use ImageMagick, or if you
want to develop/compile applications using the ImageMagick C interface,
however.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -p1 -n %{name}-%{VER}-%{Patchlevel}

%build

autoconf -f -i -v
export CFLAGS="%{optflags} -DIMPNG_SETJMP_IS_THREAD_SAFE"
%configure \
        --enable-shared \
        --disable-static \
        --with-modules \
%if %{with perl}
        --with-perl \
        --with-perl-options="INSTALLDIRS=vendor %{?perl_prefix} CC='%__cc -L$PWD/magick/.libs' LDDLFLAGS='-shared -L$PWD/magick/.libs'" \
%endif
        --with-x \
        --with-threads \
        --with-magick_plus_plus \
        --with-gslib \
        --with-pango \
        --with-fftw \
        --with-wmf \
        --with-webp \
        --with-openexr \
        --with-rsvg \
        --with-xml \
        --with-urw-base35-font-dir="%{urw_base35_fontpath}" \
        --without-dps \
        --enable-openmp \
        --without-gcc-arch \
        --with-jbig \
        --with-jxl \
        --with-openjp2 \
        --with-raw \
        --with-gvc \
        --with-raqm \
%if %{with libheif}
           --with-heic \
%endif
make
make html-local
%install
%make_install
ln -sr %{buildroot}%{_includedir}/%{name}-7/MagickCore %{buildroot}%{_includedir}/%{name}-7/magick
ln -sr %{buildroot}%{_includedir}/%{name}-7/MagickWand %{buildroot}%{_includedir}/%{name}-7/wand
rm %{buildroot}%{_libdir}/*.la
%if %{with perl}
chmod 755 %{buildroot}%{perl_vendorarch}/auto/Image/Magick/Q16HDRI/Q16HDRI.so
%{__perl} -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)' PerlMagick/demo/*.pl
find %{buildroot} -name "*.bs" |xargs rm -f
find %{buildroot} -name ".packlist" |xargs rm -f
find %{buildroot} -name "perllocal.pod" |xargs rm -f
find %{buildroot}/%{_libdir}/perl* -type f -print \
        | sed "s@^%{buildroot}@@g" > perl-pkg-files
find %{buildroot}%{perl_vendorarch} -type d -print \
        | sed "s@^%{buildroot}@%dir @g" \
        | grep -v '^%dir %{perl_vendorarch}$' \
        | grep -v '/auto$' >> perl-pkg-files
if [ -z perl-pkg-files ] ; then
        echo "ERROR: EMPTY FILE LIST"
        exit -1
fi
%endif
function multilibFileVersions(){
mv $1 ${1%%.h}-%{__isa_bits}.h
local basename=$(basename $1)
cat >$1 <<EOF
EOF
}
multilibFileVersions %{buildroot}%{_includedir}/%{name}-7/MagickCore/magick-config.h
multilibFileVersions %{buildroot}%{_includedir}/%{name}-7/MagickCore/magick-baseconfig.h
multilibFileVersions %{buildroot}%{_includedir}/%{name}-7/MagickCore/version.h
find %{buildroot} -type f -name "*%{subsover}*" >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo Error: No files containing %{subsover} found
    exit 1
fi
%oreon_autofiles ImageMagick-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ImageMagick-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ImageMagick-djvu usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ImageMagick-heic usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ImageMagick-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ImageMagick-perl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%make_build check
%endif
rm PerlMagick/demo/Generic.ttf
%files -f %{oreon_filedir}/main.list
%files -n ImageMagick-devel -f %{oreon_filedir}/ImageMagick-devel.list
%files -n ImageMagick-libs -f %{oreon_filedir}/ImageMagick-libs.list
%files -n ImageMagick-djvu -f %{oreon_filedir}/ImageMagick-djvu.list
%files -n ImageMagick-heic -f %{oreon_filedir}/ImageMagick-heic.list
%files -n ImageMagick-doc -f %{oreon_filedir}/ImageMagick-doc.list
%files -n ImageMagick-perl -f %{oreon_filedir}/ImageMagick-perl.list

%changelog

%autochangelog
