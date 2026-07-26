%global source0_hash b20cee717e11416d2f96ccc7d184f63730ca8cb2f03bfd0c4ed77fbc909c0bff

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:		tkimg
Version:	2.1.0
Release:	2%{?dist}
Summary:	Image support library for Tk
# The core tkimg code is TCL
# tiff/ is libtiff
# gif/gif.c is HPND-Pbmplus AND URT-RLE
# compat/libjpeg is IJG AND HPND-Pbmplus
# compat/libpng is libpng-2.0 AND libpng-1.6.35 AND (BSD-4-Clause OR GPL-2.0-or-later) AND BSD-4-Clause AND MIT
# compat/libtiff is libtiff AND MIT
#   ... (yes, the SPDX MIT)
# compat/zlib is Zlib
#   ... the dotzlib stuff is BSL-1.0, but I know it's not used here.
License:	TCL AND libtiff AND HPND-Pbmplus AND URT-RLE AND IJG AND libpng-2.0 AND libpng-1.6.35 AND (BSD-4-Clause OR GPL-2.0-or-later) AND BSD-4-Clause AND MIT AND Zlib
# Try saying that three times fast.
URL:		http://sourceforge.net/projects/tkimg
Source0:	https://downloads.sourceforge.net/project/tkimg/tkimg/2.1.0/Img-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	tcl-devel tk-devel tcllib

# tkimg builds its own bundled copies of the zlib, libjpeg, libpng,
# and libtiff libraries. From the README:
#  Note that you have to build these libraries to
#  support the named formats, even if your system already has shared
#  libraries for these formats. This is because the libraries here are
#  built such that they can be loaded as packages by the Tcl/Tk core,
#  making the handling of the various dependencies much easier. An
#  earlier version, 1.2.4, used a modified copy of Tcl's functions for
#  loading of shared libraries to load the support libraries at runtime.
#  These have been abandoned in favor of the new approach.

# Pulling in our own copy of libtiff 4.7.1 to fix a LOT of CVEs.
Source1:	http://download.osgeo.org/libtiff/tiff-4.7.1.tar.gz

# Patching things to apply to the libtiff 4.7.1 API
Patch0:		tkimg-2.1.0-libtiff-4.7.1.patch

# Pulling in our own copy of libpng 1.6.53 for some CVEs
Source2:	https://github.com/pnggroup/libpng/archive/refs/tags/v1.6.53.tar.gz

# the tkimg copy of libpng disables some externs in a header
Patch1:		tkimg-2.1.0-libpng-1.6.53.patch

Provides: bundled(zlib) = 1.3.1
Provides: bundled(libjpeg) = 9f
Provides: bundled(libpng) = 1.6.53
Provides: bundled(libtiff) = 4.7.1
Requires: tcl(abi) = 9.0
Requires: tk >= 9.0

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

# I have no idea why html files are getting installed into the mandir.
rm -rf %{buildroot}%{_mandir}/html

%files
%doc README.md
%{tcl_sitearch}/Img%{version}
%{_mandir}/mann/img*
%exclude %{tcl_sitearch}/Img%{version}/*.a

%files devel
%doc README.md
%{_includedir}/*
%{tcl_sitearch}/*.sh
%{tcl_sitearch}/Img%{version}/*.a

%changelog
%autochangelog
