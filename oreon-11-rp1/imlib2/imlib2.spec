%global source0_hash fa2315f28379b430a6e6605b4284b07be06a3ef422d4f5e1c9bb24714c4cf6dd
Summary:        Image loading, saving, rendering, and manipulation library
Name:           imlib2
Version:        1.12.5
Release:        1%{?dist}
License:        Imlib2
URL:            http://docs.enlightenment.org/api/imlib2/html/
Source0:        http://downloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  giflib-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libheif-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libjxl-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libspectre-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libwebp-devel
BuildRequires:  make
BuildRequires:  openjpeg2-devel
BuildRequires:  pkgconfig
# /oreon:deps
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
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description id3tag-loader
This package contains a plugin which makes imlib2 capable of parsing id3 tags
of mp3 files. This plugin is packaged separately because it links with
libid3tag which is GPLv2+, thus making imlib2 and apps using it subject to the
conditions of the GPL version 2 (or at your option) any later version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

asmopts="--disable-mmx --disable-amd64"
%ifarch x86_64
asmopts="--disable-mmx --enable-amd64"
%else
%ifarch %{ix86}
asmopts="--enable-mmx --disable-amd64"
%endif
%endif
autoreconf -ifv
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
rm $RPM_BUILD_ROOT%{_bindir}/imlib2_*
rm -rf $RPM_BUILD_ROOT%{_datadir}/imlib2/
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f \{\} \;
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n imlib2-devel -f %{oreon_filedir}/imlib2-devel.list
%files -n imlib2-id3tag-loader -f %{oreon_filedir}/imlib2-id3tag-loader.list

%changelog

%autochangelog
