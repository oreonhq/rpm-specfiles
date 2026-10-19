%global source1_hash 54ff2db5511f01eecc5d012f46083382ce49348b9e1ce62db87b06e5d860890f
%global source0_hash d88519a094797c645ca34797a24a14efc10965829c4c3352c8ef33782a556336
%bcond_without tests
%bcond_with texdocs
Name:       gdcm
Version:    3.0.24
Release:        1%{?dist}
Summary:        Grassroots DiCoM is a C++ library to parse DICOM medical files
License:    BSD-3-Clause
URL:        https://sourceforge.net/projects/gdcm/
Source0:        https://github.com/malaterre/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    http://downloads.sourceforge.net/project/gdcm/gdcmData/gdcmData/gdcmData.tar.gz
Patch1: 0001-3.0.1-Use-copyright.patch
Patch2: 0002-Fix-export-variables.patch
Patch3: 0003-fix-set-C-23-for-poppler-usage.patch
Patch4: 0004-fix-GooString-use-std-string-size.patch
%if %{with texdocs}
%endif
# oreon:deps
BuildRequires:  CharLS-devel
BuildRequires:  cmake
BuildRequires:  dcmtk-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook5-style-xsl
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gl2ps-devel
BuildRequires:  graphviz
BuildRequires:  json-c-devel
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  poppler-devel
BuildRequires:  python3-devel
BuildRequires:  sqlite-devel
BuildRequires:  swig
# /oreon:deps
%description
Grassroots DiCoM (GDCM) is a C++ library for DICOM medical files.
It supports ACR-NEMA version 1 and 2 (huffman compression is not supported),
RAW, JPEG, JPEG 2000, JPEG-LS, RLE and deflated transfer syntax.
It comes with a super fast scanner implementation to quickly scan hundreds of
DICOM files. It supports SCU network operations (C-ECHO, C-FIND, C-STORE,
C-MOVE). PS 3.3 & 3.6 are distributed as XML files.
It also provides PS 3.15 certificates and password based mechanism to
anonymize and de-identify DICOM datasets.

%package    doc
Summary:    Includes html documentation for gdcm
BuildArch:  noarch
Provides:   %{name}-examples = %{version}-%{release}
Obsoletes:  %{name}-examples < %{version}-%{release}
%description doc
You should install the gdcm-doc package if you would like to
access upstream documentation for gdcm.
Includes CSharp, C++, Java, PHP and Python example programs for GDCM
in html pages

%package    applications
Summary:    Includes command line programs for GDCM
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description applications
You should install the gdcm-applications package if you would like to
use command line programs part of GDCM. Includes tools to convert,
anonymize, manipulate, concatenate, and view DICOM files.

%package    devel
Summary:    Libraries and headers for GDCM
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   %{name}-applications%{?_isa} = %{version}-%{release}
%description devel
You should install the gdcm-devel package if you would like to
compile applications based on gdcm

%package -n python3-gdcm
Summary:    Python binding for GDCM
%{?python_provide:%python_provide python3-gdcm}
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description -n python3-gdcm
You should install the python3-gdcm package if you would like to
used this library with python

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n GDCM-%{version} -S git
# Data source
%setup -n GDCM-%{version} -q -T -D -a 1

# deps not available
%if %{with texdocs}
sed -i.backup 's/^GENERATE_LATEX.*=.*YES/GENERATE_LATEX = NO/' Utilities/doxygen/doxyfile.in
%endif

# Remove bundled utilities (we use Fedora's ones)
rm -rf Utilities/gdcmexpat
rm -rf Utilities/gdcmopenjpeg-v1
rm -rf Utilities/gdcmopenjpeg-v2
rm -rf Utilities/gdcmzlib
rm -rf Utilities/gdcmuuid
rm -rf Utilities/gdcmcharls

# Remove bundled utilities (we don't use them)
rm -rf Utilities/getopt
rm -rf Utilities/pvrg
rm -rf Utilities/rle
rm -rf Utilities/wxWidgets

# Needed for testing:
#rm -rf Utilities/gdcmmd5

# cmake version changed, need to update minimum version
sed -i -e 's@cmake_minimum_required(VERSION 2.8.7)@cmake_minimum_required(VERSION 3.5)@' Examples/CMakeLists.txt

%build

%cmake \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DGDCM_INSTALL_PACKAGE_DIR=%{_libdir}/cmake/%{name} \
    -DGDCM_INSTALL_INCLUDE_DIR=%{_includedir}/%{name} \
    -DGDCM_INSTALL_DOC_DIR=%{_docdir}/%{name} \
    -DGDCM_INSTALL_MAN_DIR=%{_mandir} \
    -DGDCM_INSTALL_LIB_DIR=%{_libdir} \
    -DGDCM_BUILD_TESTING:BOOL=ON \
    -DGDCM_DATA_ROOT=../gdcmData/ \
    -DGDCM_BUILD_EXAMPLES:BOOL=ON \
    -DGDCM_DOCUMENTATION:BOOL=OFF \
    -DGDCM_WRAP_PYTHON:BOOL=ON \
    -DPYTHON_EXECUTABLE=%{python3} \
    -DGDCM_INSTALL_PYTHONMODULE_DIR=%{python3_sitearch} \
    -DGDCM_WRAP_JAVA:BOOL=OFF \
    -DGDCM_WRAP_CSHARP:BOOL=OFF \
    -DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
    -DGDCM_BUILD_APPLICATIONS:BOOL=ON \
    -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
    -DGDCM_USE_VTK:BOOL=OFF \
    -DGDCM_USE_SYSTEM_CHARLS:BOOL=ON \
    -DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
    -DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
    -DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
    -DGDCM_USE_SYSTEM_UUID:BOOL=ON \
    -DGDCM_USE_SYSTEM_LJPEG:BOOL=OFF \
    -DGDCM_USE_SYSTEM_OPENSSL:BOOL=ON \
    -DGDCM_USE_JPEGLS:BOOL=ON \
    -DGDCM_USE_SYSTEM_LIBXML2:BOOL=ON \
    -DGDCM_USE_SYSTEM_JSON:BOOL=ON \
    -DGDCM_USE_SYSTEM_POPPLER:BOOL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles python3-gdcm usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

make test -C %{__cmake_builddir} || exit 0
%endif
%files -f %{oreon_filedir}/main.list
%files -n gdcm-doc -f %{oreon_filedir}/gdcm-doc.list
%files -n gdcm-applications -f %{oreon_filedir}/gdcm-applications.list
%files -n gdcm-devel -f %{oreon_filedir}/gdcm-devel.list
%files -n python3-gdcm -f %{oreon_filedir}/python3-gdcm.list

%changelog

%autochangelog
