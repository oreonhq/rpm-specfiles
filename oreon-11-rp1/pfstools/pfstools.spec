%global source0_hash 9bf6844985663226c21998eeb43c261acb8e4b3891b9a91b729554406289d7ca

Name:		pfstools
Version:	2.2.0
Release:	25%{?dist}
Summary:	Programs for handling high-dynamic range images

License:	GPL-2.0-or-later
URL:		http://pfstools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Patch0:		pfstools-freeglut.patch
# From https://sourceforge.net/p/pfstools/bugs/54
Patch1:		0001-Prefer-upstream-CMake-Config-Mode-files-for-OpenEXR.patch
# From openSUSE
Patch2:		pfstools-ImageMagick7.patch

BuildRequires:  make
BuildRequires:	cmake
BuildRequires:	libtiff-devel
BuildRequires:	cmake(OpenEXR)
BuildRequires:	octave-devel
BuildRequires:	libGL-devel
BuildRequires:	ImageMagick-devel
BuildRequires:	freeglut-devel
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	perl-generators
BuildRequires:	pkgconfig(Qt5)
BuildRequires:	libXi-devel
BuildRequires:	netpbm-devel
BuildRequires:	texlive-latex
BuildRequires:	gsl-devel
BuildRequires:	fftw-devel
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

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

%autosetup -p1

%build
# TODO: Please submit an issue to upstream (rhbz#2381359)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%{cmake} -DBUILD_SHARED_LIBS=ON \
	-DLIB_DIR=%{_lib} \
	-DWITH_OpenCV=OFF \
	%if "%{?_lib}" == "lib64"
		%{?_cmake_lib_suffix64} \
	%endif

# Not parallel build safe
%global _smp_build_ncpus 1
%{cmake_build}

%install
%{cmake_install}

# XXX Nuke unpackaged files
{ cd ${RPM_BUILD_ROOT}
  rm -f .%{_libdir}/libpfs-1.2.la
  rm -f .%{_mandir}/man1/pfsinjpeghdr.1
  rm -f .%{_mandir}/man1/pfsoutjpeghdr.1
}

%ldconfig_scriptlets libs

%files
%doc README
%{_bindir}/pfsabsolute
%{_bindir}/pfscat
%{_bindir}/pfsclamp
%{_bindir}/pfscut
%{_bindir}/pfsextractchannels
%{_bindir}/pfsdisplayfunction
%{_bindir}/pfsflip
%{_bindir}/pfsgamma
%{_bindir}/pfsin
%{_bindir}/pfsindcraw
%{_bindir}/pfsinpfm
%{_bindir}/pfsinppm
%{_bindir}/pfsinrgbe
%{_bindir}/pfsintiff
%{_bindir}/pfsinyuv
%{_bindir}/pfsout
%{_bindir}/pfsouthdrhtml
%{_bindir}/pfsoutpfm
%{_bindir}/pfsoutppm
%{_bindir}/pfsoutrgbe
%{_bindir}/pfsouttiff
%{_bindir}/pfsoutyuv
%{_bindir}/pfspad
%{_bindir}/pfspanoramic
%{_bindir}/pfsrotate
%{_bindir}/pfssize
%{_bindir}/pfstag
%{_bindir}/pfscolortransform
%{_bindir}/pfsretime
%{_bindir}/pfs_automerge
%{_bindir}/pfs_split_exposures.py
%{_datadir}/pfstools/hdrhtml_c_b2.csv
%{_datadir}/pfstools/hdrhtml_c_b3.csv
%{_datadir}/pfstools/hdrhtml_c_b4.csv
%{_datadir}/pfstools/hdrhtml_c_b5.csv
%{_datadir}/pfstools/hdrhtml_default_templ/
%{_datadir}/pfstools/hdrhtml_hdrlabs_templ/
%{_datadir}/pfstools/hdrhtml_t_b2.csv
%{_datadir}/pfstools/hdrhtml_t_b3.csv
%{_datadir}/pfstools/hdrhtml_t_b4.csv
%{_datadir}/pfstools/hdrhtml_t_b5.csv
%{_mandir}/man1/pfsabsolute.1.gz
%{_mandir}/man1/pfscat.1.gz
%{_mandir}/man1/pfsclamp.1.gz
%{_mandir}/man1/pfscut.1.gz
%{_mandir}/man1/pfsdisplayfunction.1.gz
%{_mandir}/man1/pfsextractchannels.1.gz
%{_mandir}/man1/pfsflip.1.gz
%{_mandir}/man1/pfsgamma.1.gz
%{_mandir}/man1/pfsin.1.gz
%{_mandir}/man1/pfsindcraw.1.gz
%{_mandir}/man1/pfsinpfm.1.gz
%{_mandir}/man1/pfsinppm.1.gz
%{_mandir}/man1/pfsinrgbe.1.gz
%{_mandir}/man1/pfsintiff.1.gz
%{_mandir}/man1/pfsinyuv.1.gz
%{_mandir}/man1/pfsout.1.gz
%{_mandir}/man1/pfsouthdrhtml.1.gz
%{_mandir}/man1/pfsoutpfm.1.gz
%{_mandir}/man1/pfsoutppm.1.gz
%{_mandir}/man1/pfsoutrgbe.1.gz
%{_mandir}/man1/pfsouttiff.1.gz
%{_mandir}/man1/pfsoutyuv.1.gz
%{_mandir}/man1/pfspad.1.gz
%{_mandir}/man1/pfspanoramic.1.gz
%{_mandir}/man1/pfsrotate.1.gz
%{_mandir}/man1/pfssize.1.gz
%{_mandir}/man1/pfstag.1.gz
%{_mandir}/man1/pfscolortransform.1.gz
%{_mandir}/man1/pfsretime.1.gz
%{_mandir}/man1/pfs_automerge.1.gz
%doc

%files -n pfscalibration
%{_bindir}/dcraw2hdrgen
%{_bindir}/jpeg2hdrgen
%{_bindir}/pfshdrcalibrate
%{_bindir}/pfsinhdrgen
%{_bindir}/pfsinme
%{_bindir}/pfsplotresponse
%{_mandir}/man1/dcraw2hdrgen.1.gz
%{_mandir}/man1/jpeg2hdrgen.1.gz
%{_mandir}/man1/pfshdrcalibrate.1.gz
%{_mandir}/man1/pfsinhdrgen.1.gz
%{_mandir}/man1/pfsinme.1.gz
%{_mandir}/man1/pfsplotresponse.1.gz

%files -n pfstmo
%{_bindir}/pfstmo_reinhard05
%{_bindir}/pfstmo_pattanaik00
%{_bindir}/pfstmo_mantiuk06
%{_bindir}/pfstmo_fattal02
%{_bindir}/pfstmo_drago03
%{_bindir}/pfstmo_reinhard02
%{_bindir}/pfstmo_durand02
%{_bindir}/pfstmo_mantiuk08
%{_bindir}/pfstmo_ferradans11
%{_bindir}/pfstmo_mai11
%{_mandir}/man1/pfstmo_reinhard05.1.gz
%{_mandir}/man1/pfstmo_pattanaik00.1.gz
%{_mandir}/man1/pfstmo_mantiuk06.1.gz
%{_mandir}/man1/pfstmo_fattal02.1.gz
%{_mandir}/man1/pfstmo_drago03.1.gz
%{_mandir}/man1/pfstmo_reinhard02.1.gz
%{_mandir}/man1/pfstmo_durand02.1.gz
%{_mandir}/man1/pfstmo_mantiuk08.1.gz
%{_mandir}/man1/pfstmo_ferradans11.1.gz
%{_mandir}/man1/pfstmo_mai11.1.gz

%files libs
%{_libdir}/libpfs.so.2.0.0
%{_libdir}/libpfs.so.2

%files qt
%{_bindir}/pfsv
%{_bindir}/pfsview
%{_mandir}/man1/pfsview.1.gz

%files glview
%{_bindir}/pfsglview
%{_mandir}/man1/pfsglview.1.gz

%files exr
%{_bindir}/pfsinexr
%{_bindir}/pfsoutexr
%{_mandir}/man1/pfsinexr.1.gz
%{_mandir}/man1/pfsoutexr.1.gz

%files imgmagick
%{_bindir}/pfsinimgmagick
%{_bindir}/pfsoutimgmagick
%{_mandir}/man1/pfsinimgmagick.1.gz
%{_mandir}/man1/pfsoutimgmagick.1.gz

%files octave
%{_bindir}/pfsoctavelum
%{_bindir}/pfsoctavergb
%{_bindir}/pfsstat
%{_libdir}/octave/*/site/oct/*/pfstools
%{_datadir}/octave/*/site/m/pfstools
%{_mandir}/man1/pfsoctavelum.1.gz
%{_mandir}/man1/pfsoctavergb.1.gz
%{_mandir}/man1/pfsstat.1.gz

%files devel
#%doc doc/pfs_format_spec.pdf
%{_libdir}/libpfs.so
%{_libdir}/pkgconfig/pfs.pc
%{_includedir}/pfs

%changelog
%autochangelog
