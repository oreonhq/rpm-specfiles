%global source0_hash none


%global _with_quantum_depth --with-quantum-depth=16
%global _enable_quantum_library_names --enable-quantum-library-names
%global libQ -Q16

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

%if ! 0%{?flatpak}
%global perl 1
%endif

%if 0%{?rhel} > 7
%global urw_font_bundle 1
%endif

%global multilib_archs x86_64 %{ix86} ppc64 ppc64le ppc s390x s390 sparc64 sparcv9

%global __provides_exclude_from ^%{_libdir}/GraphicsMagick-%{version}/.*\\.(la|so)$

Name: GraphicsMagick
Version: 1.3.45
Release: 7%{?dist}
Summary: An ImageMagick fork, offering faster image generation and better quality
Url: http://www.graphicsmagick.org/
License: MIT

Source0: http://downloads.sourceforge.net/sourceforge/graphicsmagick/GraphicsMagick-%{version}.tar.xz
# bundle urw-fonts if needed
Source1: urw-fonts-1.0.7pre44.tar.bz2

# workaround multilib conflicts with GraphicsMagick-config
Patch100: GraphicsMagick-1.3.42-multilib.patch

# upstreamable patches
Patch50: GraphicsMagick-1.3.31-perl_linkage.patch

BuildRequires: bzip2-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: giflib-devel
BuildRequires: jasper-devel
BuildRequires: jbigkit-devel
BuildRequires: lcms2-devel
BuildRequires: libheif-devel
BuildRequires: libjpeg-devel
BuildRequires: libjxl-devel
BuildRequires: libpng-devel
BuildRequires: librsvg2-devel
BuildRequires: libtiff-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: libwebp-devel
BuildRequires: libwmf-devel
BuildRequires: libxml2-devel
BuildRequires: libX11-devel libXext-devel libXt-devel
BuildRequires: lpr
BuildRequires: make
BuildRequires: p7zip
%if 0%{?perl}
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
%endif
BuildRequires: xdg-utils
BuildRequires: xz-devel
BuildRequires: zlib-devel
## %%check stuff
BuildRequires: time

%if 0%{?urw_font_bundle}
%global urw_font_path %{_datadir}/GraphicsMagick-%{version}/urw-fonts
%else
%global urw_font_path %{_datadir}/X11/fonts/urw-fonts
BuildRequires: urw-base35-fonts-legacy
Requires: urw-base35-fonts-legacy
%endif

Provides:       perl(Graphics::Magick)
%description
GraphicsMagick is a comprehensive image processing package which is initially
based on ImageMagick 5.5.2, but which has undergone significant re-work by
the GraphicsMagick Group to significantly improve the quality and performance
of the software.

%package devel
Summary: Libraries and header files for GraphicsMagick app development
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
GraphicsMagick-devel contains the Libraries and header files you'll
need to develop GraphicsMagick applications. GraphicsMagick is an image
manipulation program.

If you want to create applications that will use GraphicsMagick code or
APIs, you need to install GraphicsMagick-devel as well as GraphicsMagick.
You do not need to install it if you just want to use GraphicsMagick,
however.

%package doc
Summary: GraphicsMagick documentation
BuildArch: noarch

%description doc
Documentation for GraphicsMagick.

%if 0%{?perl}
%package perl
Summary: GraphicsMagick perl bindings
Requires: %{name}%{?_isa} = %{version}-%{release}

%description perl
Perl bindings to GraphicsMagick.

Install GraphicsMagick-perl if you want to use any perl scripts that use
GraphicsMagick.
%endif

%package c++
Summary: GraphicsMagick Magick++ library (C++ bindings)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description c++
This package contains the GraphicsMagick++ library, a C++ binding to the 
GraphicsMagick graphics manipulation library.

Install GraphicsMagick-c++ if you want to use any applications that use 
GraphicsMagick++.

%package c++-devel
Summary: C++ bindings for the GraphicsMagick library
Requires: %{name}-c++%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description c++-devel
GraphicsMagick-devel contains the Libraries and header files you'll
need to develop GraphicsMagick applications using the Magick++ C++ bindings.
GraphicsMagick is an image manipulation program.

If you want to create applications that will use Magick++ code
or APIs, you'll need to install GraphicsMagick-c++-devel, ImageMagick-devel and
GraphicsMagick.
You don't need to install it if you just want to use GraphicsMagick, or if you
want to develop/compile applications using the GraphicsMagick C interface,
however.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%if 0%{?urw_font_bundle}
mkdir -p urw-fonts
tar --directory=urw-fonts/ -xf %{SOURCE1}
rm -f urw-fonts/ChangeLog urw-fonts/README* urw-fonts/fonts*
%endif

for f in ChangeLog.{2006,2008,2009,2012} NEWS.txt ; do
    iconv -f iso-8859-2 -t utf8 < $f > $f.utf8
    touch -r $f $f.utf8 ; mv -f $f.utf8 $f
done

# Avoid lib64 rpaths (FIXME: recheck this on newer releases)
%if "%{_libdir}" != "/usr/lib"
sed -i.rpath -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif


%build
%configure \
           --enable-shared --disable-static \
           --docdir=%{_pkgdocdir} \
           --with-lcms2 \
           --with-magick_plus_plus \
           --with-modules \
%if 0%{?flatpak}
           --without-perl \
%else
           --with-perl \
           --with-perl-options="INSTALLDIRS=vendor %{?perl_prefix}" \
%endif
           %{?_with_quantum_depth} \
           %{?_enable_quantum_library_names} \
           --with-threads \
           --with-wmf \
           --with-x \
           --with-xml \
           --without-dps \
           --without-gslib \
           --with-gs-font-dir=%{urw_font_path}

%make_build
%if 0%{?perl}
%make_build perl-build
%endif


%install
%make_install

%if 0%{?perl}
%make_install -C PerlMagick

# perlmagick: fix perl path of demo files
%{__perl} -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)' PerlMagick/demo/*.pl

find %{buildroot} -name "*.bs" |xargs rm -fv
find %{buildroot} -name ".packlist" |xargs rm -fv
find %{buildroot} -name "perllocal.pod" |xargs rm -fv

ls -l %{buildroot}%{perl_vendorarch}/auto/Graphics/Magick/Magick.so
chmod 755 %{buildroot}%{perl_vendorarch}/auto/Graphics/Magick/Magick.so

# perlmagick: build files list
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

rm -rfv %{buildroot}%{_datadir}/GraphicsMagick
# Keep config
rm -rfv %{buildroot}%{_datadir}/%{name}-%{version}/[a-b,d-z,A-Z]*
rm -fv  %{buildroot}%{_libdir}/lib*.la

%if 0%{?urw_font_bundle}
mkdir -p %{buildroot}%{urw_font_path}/
install -p -m644 urw-fonts/* \
  %{buildroot}%{urw_font_path}/
%endif

# fix multilib issues
%ifarch %{multilib_archs}
mv %{buildroot}%{_includedir}/GraphicsMagick/magick/magick_types.h \
   %{buildroot}%{_includedir}/GraphicsMagick/magick/magick_types-%{__isa_bits}.h

cat >%{buildroot}%{_includedir}/GraphicsMagick/magick/magick_types.h <<EOF
#ifndef MAGICK_TYPES_MULTILIB
#define MAGICK_TYPES_MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "magick/magick_types-32.h"
#elif __WORDSIZE == 64
# include "magick/magick_types-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif
EOF
%endif


%check
%if 0%{?perl}
make test -C PerlMagick ||:
%endif
time \
%make_build check ||:
# multilib hack only supports 32/64 bits for now
%ifarch %{multilib_archs}
%if ! (%{__isa_bits} == 32 || %{__isa_bits} == 64)
echo "multilib hack currently only supports 64/32 bits, not %{__isa_bits} (yet)"
exit 1
%endif
%endif


%ldconfig_scriptlets

%files
%dir %{_pkgdocdir}
%license %{_pkgdocdir}/Copyright.txt
%{_libdir}/libGraphicsMagick%{?libQ}.so.3*
%{_libdir}/libGraphicsMagickWand%{?libQ}.so.2*
%{_bindir}/[a-z]*
%{_libdir}/GraphicsMagick-%{version}/
%{_datadir}/GraphicsMagick-%{version}/
%{_mandir}/man[145]/[a-z]*

%files devel
%{_bindir}/GraphicsMagick-config
%{_bindir}/GraphicsMagickWand-config
%{_libdir}/libGraphicsMagick.so
%{_libdir}/libGraphicsMagickWand.so
%{_libdir}/pkgconfig/GraphicsMagick.pc
%{_libdir}/pkgconfig/GraphicsMagickWand.pc
%dir %{_includedir}/GraphicsMagick/
%{_includedir}/GraphicsMagick/magick/
%{_includedir}/GraphicsMagick/wand/
%{_mandir}/man1/GraphicsMagick-config.*
%{_mandir}/man1/GraphicsMagickWand-config.*

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/ChangeLog*
%{_pkgdocdir}/*.txt
%{_pkgdocdir}/www/

%ldconfig_scriptlets c++

%files c++
%{_libdir}/libGraphicsMagick++%{?libQ}.so.12*

%files c++-devel
%{_bindir}/GraphicsMagick++-config
%{_includedir}/GraphicsMagick/Magick++/
%{_includedir}/GraphicsMagick/Magick++.h
%{_libdir}/libGraphicsMagick++.so
%{_libdir}/pkgconfig/GraphicsMagick++.pc
%{_mandir}/man1/GraphicsMagick++-config.*

%if 0%{?perl}
%files perl -f perl-pkg-files
%{_mandir}/man3/*
%doc PerlMagick/demo/ PerlMagick/Changelog PerlMagick/README.txt
%endif


%changelog
%autochangelog

