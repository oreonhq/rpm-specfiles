%global source0_hash fa2315f28379b430a6e6605b4284b07be06a3ef422d4f5e1c9bb24714c4cf6dd

Summary:        Image loading, saving, rendering, and manipulation library
Name:           imlib2
Version:        1.12.5
Release:        2%{?dist}
License:        Imlib2
URL:            http://docs.enlightenment.org/api/imlib2/html/
Source0:        http://downloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.xz

BuildRequires:  doxygen
BuildRequires:  giflib-devel
BuildRequires:  freetype-devel >= 2.1.9-4
BuildRequires:  libtool
BuildRequires:  bzip2-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libheif-devel
BuildRequires:  libjxl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libspectre-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libwebp-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  pkgconfig
BuildRequires:  make

%description
Imlib 2 is a library that does image file loading and saving as well
as rendering, manipulation, arbitrary polygon support, etc.  It does
ALL of these operations FAST. Imlib2 also tries to be highly
intelligent about doing them, so writing naive programs can be done
easily, without sacrificing speed.  This is a complete rewrite over
the Imlib 1.x series. The architecture is more modular, simple, and
flexible.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel
Requires:       libXext-devel
Requires:       freetype-devel >= 2.1.9-4

%description devel
This package contains development files for %{name}.

Imlib 2 is a library that does image file loading and saving as well
as rendering, manipulation, arbitrary polygon support, etc.  It does
ALL of these operations FAST. Imlib2 also tries to be highly
intelligent about doing them, so writing naive programs can be done
easily, without sacrificing speed.  This is a complete rewrite over
the Imlib 1.x series. The architecture is more modular, simple, and
flexible.

%package id3tag-loader
Summary:        Imlib2 id3tag-loader
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description id3tag-loader
This package contains a plugin which makes imlib2 capable of parsing id3 tags
of mp3 files. This plugin is packaged separately because it links with
libid3tag which is GPLv2+, thus making imlib2 and apps using it subject to the
conditions of the GPL version 2 (or at your option) any later version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
asmopts="--disable-mmx --disable-amd64"
%ifarch x86_64
asmopts="--disable-mmx --enable-amd64"
%else
%ifarch %{ix86}
asmopts="--enable-mmx --disable-amd64"
%endif
%endif

# can be dropped once upstream moves to autoconf 2.69
autoreconf -ifv

# stop -L/usr/lib[64] getting added to imlib2-config
export x_libs=" "
%configure \
 --disable-static \
 --enable-doc-build \
 --with-pic \
 $asmopts
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{make_build}

%install
%{make_install}

# remove demos and their dependencies
rm $RPM_BUILD_ROOT%{_bindir}/imlib2_*
rm -rf $RPM_BUILD_ROOT%{_datadir}/imlib2/

# remove static libraries
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f \{\} \;

%ldconfig_scriptlets

%files
%doc AUTHORS README TODO
%license COPYING
%{_libdir}/libImlib2.so.*
%{_libdir}/imlib2/
%exclude %{_libdir}/imlib2/loaders/id3.*

%files devel
%doc doc/html
%{_includedir}/Imlib2*.h
%{_libdir}/libImlib2.so
%{_libdir}/pkgconfig/imlib2.pc

%files id3tag-loader
%{_libdir}/imlib2/loaders/id3.*

%changelog
%autochangelog
