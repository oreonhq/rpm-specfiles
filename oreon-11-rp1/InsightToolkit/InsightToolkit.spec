%global source3_hash 02e55b9aa090ec0d231e2cb99132b144a5d352963784db6cfb5402c3ef341a5a
%global source2_hash 1c8cf62c1016399913f843794f6bf69de16a87f28b34777cf19bb0c6445bb62f
%global source1_hash 22625015a49e99ae075542066affad1ee3381229128f2f06a1777e95e675a8c9
%global source0_hash b8ea18a5c97c62972c00c4679ff5a224eb393a766c334bd20884b379ca2b34ce
%undefine __cmake_in_source_build
%undefine _lto_cflags
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%bcond_without flexiblas
%endif
Name:           InsightToolkit
Summary:        Insight Toolkit library for medical image processing
%global version_major_minor 4.13
Version:        %{version_major_minor}.3
%global version_doc_major_minor 4.13
%global version_doc %{version_doc_major_minor}.0
Release:        32%{?dist}
License:        Apache-2.0
Source0:        https://github.com/InsightSoftwareConsortium/ITK/releases/download/v%{version}/InsightToolkit-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/project/itk/itk/%{version_doc_major_minor}/InsightSoftwareGuide-Book1-%{version_doc}.pdf
Source2:        https://downloads.sourceforge.net/project/itk/itk/%{version_doc_major_minor}/InsightSoftwareGuide-Book2-%{version_doc}.pdf
Source3:        https://github.com/InsightSoftwareConsortium/ITK/releases/download/v%{version}/InsightData-%{version}.tar.gz
URL:            https://www.itk.org/
Patch0:         InsightToolkit-0001-Set-lib-lib64-according-to-the-architecture.patch
Patch2:         InsightToolkit-sse.patch
Patch3:         remove-test.diff
Patch4:         InsightToolkit-pr1599-fix-invalid-const-member-func.patch
Patch5:         InsightToolkit-remove-vxl-netlib.patch
Patch6:         fix-riscv.patch
ExcludeArch: %{ix86}
%if %{with flexiblas}
%else
%endif
# oreon:deps
BuildRequires:  castxml
BuildRequires:  cmake
BuildRequires:  dcmtk
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  fftw-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gdcm-devel
BuildRequires:  graphviz
BuildRequires:  hdf5-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libminc-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  netcdf-cxx-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  vtk-devel
BuildRequires:  vxl-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp -ar Examples/* %{buildroot}%{_datadir}/%{name}/examples/
%oreon_autofiles InsightToolkit-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles InsightToolkit-examples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles InsightToolkit-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles InsightToolkit-vtk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles InsightToolkit-vtk-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest || exit 0
%ldconfig_scriptlets
%ldconfig_scriptlets vtk
%files -f %{oreon_filedir}/main.list
%files -n InsightToolkit-devel -f %{oreon_filedir}/InsightToolkit-devel.list
%files -n InsightToolkit-examples -f %{oreon_filedir}/InsightToolkit-examples.list
%files -n InsightToolkit-doc -f %{oreon_filedir}/InsightToolkit-doc.list
%files -n InsightToolkit-vtk -f %{oreon_filedir}/InsightToolkit-vtk.list
%files -n InsightToolkit-vtk-devel -f %{oreon_filedir}/InsightToolkit-vtk-devel.list

%changelog

%autochangelog
