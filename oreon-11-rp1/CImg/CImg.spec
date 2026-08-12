%global source0_hash bced3f716ba36da32ec0cecadfbdfaa8640416e0955acd1154e4899aad9dd6f3

%global debug_package %{nil}

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%bcond_without flexiblas
%endif

Name:           CImg
Epoch:          1
Version:        3.7.4
Release:        2%{?dist}
Summary:        C++ Template Image Processing Toolkit
# CImg.h: Dual licensed
# plugins/cimgmatlab.h: LGPLv3
License:        ( CECILL-2.0 OR CECILL-C ) AND LGPL-3.0-only
URL:            https://github.com/dtschump/CImg
Source0:        https://github.com/GreycLab/CImg/archive/v.%{version}/CImg-%{version}.zip
# This package has no dependencies actually, these below are 
# for %%check only.
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  fftw-devel
BuildRequires:  ImageMagick-c++-devel
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%else
BuildRequires:	blas-devel
BuildRequires:  lapack-devel
%endif
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrandr-devel
BuildRequires:  opencv-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  zlib-devel
BuildRequires:  make

%description
The CImg Library is an open-source C++ toolkit for image processing. 
It consists in a single header file 'CImg.h' providing a minimal set of C++ 
classes and methods that can be used in your own sources, to load/save, 
process and display images. Very portable, efficient and easy to use, 
it's a pleasant library for developping image processing algorithms in C++.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CImg-v.%{version}
sed -i 's|$(X11PATH)/lib|$(X11PATH)/%{_lib}|g' examples/Makefile
%if %{with flexiblas}
sed -i 's|-lblas -llapack|-lflexiblas|g' examples/Makefile
%endif

%build
# This is a headers only package.

%install
install -pdm755 %{buildroot}%{_includedir}/%{name}/plugins
install -pm644 CImg.h %{buildroot}%{_includedir}/
install -pm644 plugins/*.h %{buildroot}%{_includedir}/%{name}/plugins/

%check
# Build examples based on sources to verify the usability.
# CMake couldn't find -lfftw3_threads so I use
# make directly.
make -C examples linux %{?_smp_mflags}

%files devel
%doc *.txt
%{_includedir}/CImg.h
%{_includedir}/%{name}/

%changelog
%autochangelog
