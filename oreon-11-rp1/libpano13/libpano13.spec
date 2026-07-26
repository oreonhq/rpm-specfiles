%global source0_hash e7c076d37a14c39434962115e47ddbe18452ca3de5ce40e2aaefa7cf5815ea28

Summary: Library for manipulating panoramic images
Name: libpano13
Version: 2.9.23
Release: 2%{?dist}
License: GPL-2.0-or-later
URL: http://panotools.sourceforge.net/
Source: http://downloads.sourceforge.net/panotools/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: libjpeg-devel, libtiff-devel, libpng-devel, zlib-devel
BuildRequires: cmake, suitesparse-devel perl-podlators

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

%autosetup -p1

%build
%cmake -DSUPPORT_JAVA_PROGRAMS=0 -DUSE_SPARSE_LEVMAR=1
%cmake_build

%check
%ctest

%install
%cmake_install
rm -f %{buildroot}/%{_libdir}/libpano13.a
rm -rf %{buildroot}%{_datadir}/pano13

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libpano13.so.3*

%files tools
%doc doc/Optimize.txt doc/stitch.txt doc/PTblender.readme doc/PTmender.readme
%{_bindir}/PTcrop
%{_bindir}/PTtiffdump
%{_bindir}/PTinfo
%{_bindir}/PToptimizer
%{_bindir}/PTblender
%{_bindir}/PTtiff2psd
%{_bindir}/panoinfo
%{_bindir}/PTmasker
%{_bindir}/PTmender
%{_bindir}/PTroller
%{_bindir}/PTuncrop
%{_mandir}/man1/*.1.gz

%files devel
%doc COPYING
%{_includedir}/pano13
%{_libdir}/libpano13.so
%{_libdir}/pkgconfig/libpano13.pc

%changelog
%autochangelog
