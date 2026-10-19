%global source0_hash 9bf6844985663226c21998eeb43c261acb8e4b3891b9a91b729554406289d7ca
Name:		pfstools
Version:	2.2.0
Release:        25%{?dist}
Summary:        Programs for handling high-dynamic range images
License:	GPL-2.0-or-later
URL:		http://pfstools.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Patch0:		pfstools-freeglut.patch
Patch1:		0001-Prefer-upstream-CMake-Config-Mode-files-for-OpenEXR.patch
Patch2:		pfstools-ImageMagick7.patch
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  ImageMagick-devel
BuildRequires:  cmake
BuildRequires:  cmake(OpenEXR)
BuildRequires:  fftw-devel
BuildRequires:  freeglut-devel
BuildRequires:  gsl-devel
BuildRequires:  libGL-devel
BuildRequires:  libXi-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  netpbm-devel
BuildRequires:  octave-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  texlive-latex
# /oreon:deps
%description
pfstools is a set of command line programs for reading,
writing, manipulating and viewing high-dynamic range (HDR) images and
video frames. All programs in the package exchange data using unix
pipes and a simple generic HDR image format (pfs). The concept of the
pfstools is similar to netpbm package for low-dynamic range images.

%package -n pfscalibration
Summary:	Scripts and programs for photometric calibration
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	perl-interpreter
Requires:	dcraw
Requires:	jhead
%description -n pfscalibration
PFScalibration package provides an implementation of the Robertson et al. 2003
method for the photometric calibration of cameras, Mitsunaga and Nayar's
algorithm "Radiometric Self Calibration", and for the recovery of high dynamic
range (HDR) images from the set of low dynamic range (LDR) exposures.

%package -n pfstmo
Summary:	PFS tone mapping operators
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description -n pfstmo
The pfstmo package contains the implementation of state-of-the-art tone
mapping operators. The motivation here is to provide an implementation of
tone mapping operators suitable for convenient processing of both static
images and animations.

%package libs
Summary:	Libraries for HDR processing
License:	LGPLv2+
%description libs
The pfstools-libs package contains a runtime library of functions for
handling HDR graphics files.

%package qt
Summary:	Qt-based viewer for HDR files
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description qt
The pfstools-qt package contains viewer programs based on Qt5 for
viewing HDR graphics files.

%package glview
Summary:	GL-based viewer for HDR files
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description glview
The pfstools-glview package contains viewer programs based on OpenGL for
viewing HDR graphics files.

%package exr
Summary:	EXR file import for PFS tools
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description exr
The pfstools-exr package contains input and output filters for EXR files
to and from the HDR graphics file format used in pfstools.

%package imgmagick
Summary:	ImageMagick file import for PFS tools
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description imgmagick
The pfstools-exr package contains input and output filters based in
ImageMagick to and from the HDR graphics file format used in pfstools.

%package octave
Summary:	Octave interaction with PFS tools
Requires:	octave(api) = %{octave_api}
%description octave
The pfstools-octave package contains programs to process red, green and blue
channels or luminance channels in pfs stream using Octave.

%package devel
Summary:	Files for development with PFS tools
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The netpbm-devel package contains the header files and link libraries,
etc., for developing programs which can handle HDR graphics files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%{cmake} -DBUILD_SHARED_LIBS=ON \
	-DLIB_DIR=%{_lib} \
	-DWITH_OpenCV=OFF \
	%if "%{?_lib}" == "lib64"
		%{?_cmake_lib_suffix64} \
	%endif
%global _smp_build_ncpus 1
%{cmake_build}
%install
%{cmake_install}
{ cd ${RPM_BUILD_ROOT}
  rm -f .%{_libdir}/libpfs-1.2.la
  rm -f .%{_mandir}/man1/pfsinjpeghdr.1
  rm -f .%{_mandir}/man1/pfsoutjpeghdr.1
}
%ldconfig_scriptlets libs
%oreon_autofiles pfscalibration usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pfstmo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pfscalibration -f %{oreon_filedir}/pfscalibration.list
%files -n pfstmo -f %{oreon_filedir}/pfstmo.list
%files -n pfstools-libs -f %{oreon_filedir}/pfstools-libs.list
%files -n pfstools-qt -f %{oreon_filedir}/pfstools-qt.list
%files -n pfstools-glview -f %{oreon_filedir}/pfstools-glview.list
%files -n pfstools-exr -f %{oreon_filedir}/pfstools-exr.list
%files -n pfstools-imgmagick -f %{oreon_filedir}/pfstools-imgmagick.list
%files -n pfstools-octave -f %{oreon_filedir}/pfstools-octave.list
%files -n pfstools-devel -f %{oreon_filedir}/pfstools-devel.list

%changelog

%autochangelog
