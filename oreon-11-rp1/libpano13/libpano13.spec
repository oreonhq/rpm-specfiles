%global source0_hash e7c076d37a14c39434962115e47ddbe18452ca3de5ce40e2aaefa7cf5815ea28
Summary:        Library for manipulating panoramic images
Name: libpano13
Version: 2.9.23
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://panotools.sourceforge.net/
Source0:        http://downloads.sourceforge.net/panotools/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  perl-podlators
BuildRequires:  suitesparse-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Helmut Dersch's Panorama Tools library.  Provides very high quality
manipulation, correction and stitching of panoramic photographs.

%package tools
Summary: Tools that use the libpano13 library
Requires: %{name} = %{version}-%{release}
%description tools
PTcrop, create cropped TIFF files from uncropped TIFF
PTuncrop, create uncropped TIFF files from cropped TIFF
PTtiffdump
PTinfo
PToptimizer, a command-line interface for control-point optimisation
PTblender, match colour histograms of overlapping TIFF files
PTtiff2psd, convert TIFF files to PSD
panoinfo, a tool for querying pano13 library capabilities
PTmasker 
PTmender, remaps photos between projections
PTroller, merges multiple TIFF with alpha masks to a single TIFF

%package devel
Summary: Development tools for programs which will use the libpano13 library
Requires: %{name} = %{version}-%{release}
Requires: libjpeg-devel, libtiff-devel, libpng-devel, zlib-devel
%description devel
The libpano13-devel package includes the header files necessary for developing
programs which will manipulate panoramas using the libpano13 library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DSUPPORT_JAVA_PROGRAMS=0 -DUSE_SPARSE_LEVMAR=1
%cmake_build
%check

%ctest
%install
%cmake_install
rm -f %{buildroot}/%{_libdir}/libpano13.a
rm -rf %{buildroot}%{_datadir}/pano13
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libpano13-tools -f %{oreon_filedir}/libpano13-tools.list
%files -n libpano13-devel -f %{oreon_filedir}/libpano13-devel.list

%changelog

%autochangelog
