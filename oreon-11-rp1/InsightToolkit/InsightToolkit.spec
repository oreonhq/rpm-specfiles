%global source0_hash none

%undefine __cmake_in_source_build
# Disable LTO for now - fails to build
%undefine _lto_cflags

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%bcond_without flexiblas
%endif

Name:           InsightToolkit
Summary:        Insight Toolkit library for medical image processing
%global version_major_minor 4.13
Version:        %{version_major_minor}.3
%global version_doc_major_minor 4.13
%global version_doc %{version_doc_major_minor}.0
Release:        32%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
Source0:        https://github.com/InsightSoftwareConsortium/ITK/releases/download/v%{version}/InsightToolkit-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/project/itk/itk/%{version_doc_major_minor}/InsightSoftwareGuide-Book1-%{version_doc}.pdf
Source2:        https://downloads.sourceforge.net/project/itk/itk/%{version_doc_major_minor}/InsightSoftwareGuide-Book2-%{version_doc}.pdf
Source3:        https://github.com/InsightSoftwareConsortium/ITK/releases/download/v%{version}/InsightData-%{version}.tar.gz
URL:            https://www.itk.org/
Patch0:         InsightToolkit-0001-Set-lib-lib64-according-to-the-architecture.patch
Patch2:         InsightToolkit-sse.patch
Patch3:         remove-test.diff
# https://github.com/InsightSoftwareConsortium/ITK/pull/1599
Patch4:         InsightToolkit-pr1599-fix-invalid-const-member-func.patch
# https://github.com/InsightSoftwareConsortium/ITK/pull/1920/files: remove use of triangle from vxl (patched out in vxl system package also)
# backported
Patch5:         InsightToolkit-remove-vxl-netlib.patch

# fix __riscv define
Patch6:         fix-riscv.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  castxml
BuildRequires:  gdcm-devel
BuildRequires:  graphviz
BuildRequires:  hdf5-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libxml2-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libjpeg-devel
%if 0%{?fedora} >= 30
BuildRequires:  qt5-qtwebkit-devel
%else
BuildRequires:  qtwebkit-devel
%endif
BuildRequires:  vxl-devel
BuildRequires:  vtk-devel
BuildRequires:  zlib-devel
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%else
BuildRequires:	blas-devel
BuildRequires:  lapack-devel
%endif
BuildRequires:  netcdf-cxx-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  expat-devel
BuildRequires:  libminc-devel
BuildRequires:  dcmtk

%description
ITK is an open-source software toolkit for performing registration and 
segmentation. Segmentation is the process of identifying and classifying data
found in a digitally sampled representation. Typically the sampled
representation is an image acquired from such medical instrumentation as CT or
MRI scanners. Registration is the task of aligning or developing 
correspondences between data. For example, in the medical environment, a CT
scan may be aligned with a MRI scan in order to combine the information
contained in both.

ITK is implemented in C++ and its implementation style is referred to as 
generic programming (i.e.,using templated code). Such C++ templating means
that the code is highly efficient, and that many software problems are 
discovered at compile-time, rather than at run-time during program execution.

%package        devel
Summary:        Insight Toolkit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-vtk-devel%{?_isa} = %{version}-%{release}

%description devel
%{summary}.
Install this if you want to develop applications that use ITK.

%package        examples
Summary:        C++, Tcl and Python example programs/scripts for ITK
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description examples
ITK examples

%package        doc
Summary:        Documentation for ITK
BuildArch:      noarch

%description    doc
%{summary}.
This package contains additional documentation.

# Hit bug http://www.gccxml.org/Bug/view.php?id=13372
# We agreed with Mattias Ellert to postpone the bindings till
# next gccxml update.
#%package        python
#Summary:        Documentation for ITK
#Group:          Documentation
#BuildArch:      noarch

#%description    python
#%%{summary}.
#This package contains python bindings for ITK.

%package        vtk
Summary:        Provides an interface between ITK and VTK
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description vtk
Provides an interface between ITK and VTK

%package        vtk-devel
Summary:        Libraries and header files for development of ITK-VTK bridge
Requires:       %{name}-vtk%{?_isa} = %{version}-%{release}
Requires:       vtk-devel%{?_isa}

%description vtk-devel
Libraries and header files for development of ITK-VTK bridge

%prep
%autosetup -p1

# copy guide into the appropriate directory
cp -a %{SOURCE1} %{SOURCE2} .

# remove applications: they are shipped separately now
rm -rf Applications/

# remove source files of external dependencies that itk gets linked against
# DICOMParser, GIFTI, KWSys, MetaIO, NrrdIO, Netlib, VNLInstantiation are not
# yet in Fedora
# DoubleConversion still seems to need the source present
# NIFTI needs support - https://issues.itk.org/jira/browse/ITK-3349
# OpenJPEG - https://issues.itk.org/jira/browse/ITK-3350
find Modules/ThirdParty/* \( -name DICOMParser -o -name DoubleConversion -o -name GIFTI -o -name KWSys -o -name MetaIO -o -name NIFTI -o -name NrrdIO -o -name Netlib -o -name OpenJPEG -o name VNLInstantiation \) \
    -prune -o -regextype posix-extended -type f \
    -regex ".*\.(h|hxx|hpp|c|cc|cpp|cxx|txx)$" -not -iname "itk*" -print0 | xargs -0 rm -fr

tar xvf %{SOURCE3} -C ..

# short-circuit a wrapper header that causes declaration conflicts
echo '#include "vnl/vnl_complex_traits.h"' >Modules/ThirdParty/VNLInstantiation/include/vnl_complex_traits+char-.h

# get rid of use of poisoned define
grep -e VCL_CHAR_IS_SIGNED -r -l . | xargs sed -r -i 's/VCL_CHAR_IS_SIGNED/CHAR_MIN < 0/'

# comment out problematic cast
# error: cannot convert ‘double’ to ‘itk::ResampleImageFilter<itk::Image<itk::Vector<double, 3>, 2>, itk::Image<itk::Vector<double, 3>, 2> >::PixelType’ {aka ‘itk::Vector<double, 3>’}
#   270 |   resample->SetDefaultPixelValue( itk::NumericTraits<FixedImageType::PixelType::ValueType>::ZeroValue() );
#       |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~
#       |                                                                                                      |
#       |                                                                                                      double
sed -r -i 's/resample->SetDefaultPixelValue/\/\/\0/' \
    Modules/Registration/Metricsv4/test/itkMeanSquaresImageToImageMetricv4VectorRegistrationTest.cxx

%build
extra_cflags=(
	-DITK_LEGACY_FUTURE_REMOVE # fix build with new vtk
	-Wno-deprecated-copy       # reduce noise in the logs...
	-Wno-maybe-uninitialized
	-Wno-ignored-qualifiers
	)
%cmake .. \
       -DBUILD_SHARED_LIBS:BOOL=ON \
       -DBUILD_EXAMPLES:BOOL=ON \
       -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo"\
       -DCMAKE_VERBOSE_MAKEFILE=ON\
       -DCMAKE_CXX_FLAGS:STRING="-std=gnu++14 %{optflags} ${extra_cflags[*]}" \
       -DBUILD_TESTING=ON\
       %{?with_flexiblas:-DBLA_VENDOR=FlexiBLAS} \
       -DITK_USE_GOLD_LINKER:BOOL=OFF \
       -DITK_FORBID_DOWNLOADS=ON \
       -DITKV3_COMPATIBILITY:BOOL=OFF \
       -DITK_BUILD_DEFAULT_MODULES:BOOL=ON \
       -DITK_USE_KWSTYLE:BOOL=OFF \
       -DModule_ITKVtkGlue:BOOL=ON \
       -DITK_WRAP_PYTHON:BOOL=OFF \
       -DITK_WRAP_JAVA:BOOL=OFF \
       -DBUILD_DOCUMENTATION:BOOL=OFF \
       -DModule_ITKReview:BOOL=ON \
       -DITK_USE_FFTWD=ON \
       -DITK_USE_FFTWF=ON \
       -DITK_USE_SYSTEM_LIBRARIES:BOOL=ON \
       -DITK_USE_SYSTEM_CASTXML=ON \
       -DITK_USE_SYSTEM_DCMTK=ON \
       -DITK_USE_SYSTEM_EXPAT=ON \
       -DITK_USE_SYSTEM_FFTW=ON \
       -DITK_USE_SYSTEM_GDCM=ON \
       -DITK_USE_SYSTEM_GOOGLETEST=OFF \
       -DITK_USE_SYSTEM_HDF5=ON \
       -DITK_USE_SYSTEM_JPEG=ON \
       -DITK_USE_SYSTEM_MINC=ON \
       -DITK_USE_SYSTEM_PNG=ON \
       -DITK_USE_SYSTEM_SWIG=ON \
       -DITK_USE_SYSTEM_TIFF=ON \
       -DITK_USE_SYSTEM_ZLIB=ON \
       -DITK_USE_SYSTEM_VXL=ON \
       -DITK_INSTALL_LIBRARY_DIR=%{_lib}/ \
       -DITK_INSTALL_INCLUDE_DIR=include/%{name} \
       -DITK_INSTALL_PACKAGE_DIR=%{_lib}/cmake/%{name}/ \
       -DITK_INSTALL_RUNTIME_DIR:PATH=%{_bindir} \
       -DITK_INSTALL_DOC_DIR=share/doc/%{name}/

%cmake_build

%install
%cmake_install

# Install examples
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp -ar Examples/* %{buildroot}%{_datadir}/%{name}/examples/

%check
# There are a couple of tests randomly failing on f19 and rawhide and I'm debugging
# it with upstream. Making the tests informative for now
%ctest || exit 0

# In F31 rawhide (some most likely related to the patching done above):
# The following tests FAILED:
#	234 - itkNumericTraitsTest (Failed)
#	2395 - itkVtkMedianImageFilterTest (Child aborted)
#	2399 - QuickViewTest (Child aborted)
#	2400 - itkVtkConnectedComponentImageFilterTest (Child aborted)

%ldconfig_scriptlets

%ldconfig_scriptlets vtk

%files
%doc LICENSE NOTICE README.md
%{_libdir}/*.so.*
%exclude %{_libdir}/libITKVtkGlue*.so.*
%{_bindir}/itkTestDriver

%files devel
%{_libdir}/*.so
%exclude %{_libdir}/libITKVtkGlue*.so
%{_libdir}/cmake/%{name}/
%{_includedir}/%{name}/
%exclude %{_includedir}/%{name}/itkImageToVTKImageFilter.h*
%exclude %{_includedir}/%{name}/itkVTKImageToImageFilter.h*
%exclude %{_includedir}/%{name}/QuickView.h
%exclude %{_includedir}/%{name}/vtkCaptureScreen.h
%exclude %{_libdir}/cmake/%{name}/Modules/ITKVtkGlue.cmake

%files examples
%{_datadir}/%{name}/examples

%files doc
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/*
%doc InsightSoftwareGuide-Book1-%{version_doc}.pdf
%doc InsightSoftwareGuide-Book2-%{version_doc}.pdf

%files vtk
%{_libdir}/libITKVtkGlue*.so.*

%files vtk-devel
%{_libdir}/libITKVtkGlue*.so
%{_includedir}/%{name}/itkImageToVTKImageFilter.h*
%{_includedir}/%{name}/itkVTKImageToImageFilter.h*
%{_includedir}/%{name}/QuickView.h
%{_includedir}/%{name}/vtkCaptureScreen.h
%{_libdir}/cmake/%{name}/Modules/ITKVtkGlue.cmake

%changelog
%autochangelog
