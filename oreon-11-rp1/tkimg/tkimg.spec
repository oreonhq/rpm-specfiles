%global source2_hash b20cee717e11416d2f96ccc7d184f63730ca8cb2f03bfd0c4ed77fbc909c0bff
%global source1_hash f698d94f3103da8ca7438d84e0344e453fe0ba3b7486e04c5bf7a9a3fabe9b69
%global source0_hash b20cee717e11416d2f96ccc7d184f63730ca8cb2f03bfd0c4ed77fbc909c0bff
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
Name:		tkimg
Version:	2.1.0
Release:        2%{?dist}
Summary:        Image support library for Tk
License:	TCL AND libtiff AND HPND-Pbmplus AND URT-RLE AND IJG AND libpng-2.0 AND libpng-1.6.35 AND (BSD-4-Clause OR GPL-2.0-or-later) AND BSD-4-Clause AND MIT AND Zlib
URL:		http://sourceforge.net/projects/tkimg
Source0:        https://downloads.sourceforge.net/project/tkimg/tkimg/2.1.0/Img-%{version}.tar.gz
Source1:	http://download.osgeo.org/libtiff/tiff-4.7.1.tar.gz
Patch0:		tkimg-2.1.0-libtiff-4.7.1.patch
Source2:	https://github.com/pnggroup/libpng/archive/refs/tags/v1.6.53.tar.gz
Patch1:		tkimg-2.1.0-libpng-1.6.53.patch
Provides: bundled(zlib) = 1.3.1
Provides: bundled(libjpeg) = 9f
Provides: bundled(libpng) = 1.6.53
Provides: bundled(libtiff) = 4.7.1
Requires: tcl(abi) = 9.0
Requires: tk >= 9.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel
BuildRequires:  tcllib
BuildRequires:  tk-devel
# /oreon:deps
%description
This package contains a collection of image format handlers for the Tk
photo image type, and a new image type, pixmaps.

%package devel
Summary:	Libraries, includes, etc. used to develop an application with %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	tcl-devel tk-devel
%description devel
These are the header files needed to develop a %{name} application

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Img-%{version}

pushd compat
rm -rf libtiff
tar xf %{SOURCE1}
mv tiff-4.7.1 libtiff
rm -rf libpng
tar xf %{SOURCE2}
mv libpng-1.6.53 libpng
popd

%patch -P0 -p1 -b .tiff471
%patch -P1 -p1 -b .libpng-1.6.53

%build

export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure --with-tcl=%{tcl_sitearch} --with-tk=%{_libdir} --libdir=%{tcl_sitearch} --disable-threads --enable-64bit
make %{?_smp_mflags}
%install
make %{?_smp_mflags} INSTALL_ROOT=%{buildroot} install
rm -rf %{buildroot}%{_mandir}/html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tkimg-devel -f %{oreon_filedir}/tkimg-devel.list

%changelog

%autochangelog
