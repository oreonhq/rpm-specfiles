%global source0_hash 373fb5ad9d3a2a17e9919ec7cfa5e7314945f3ab669b1eba8a5618cb1f71312c
%global debug_package %{nil}
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%bcond_without flexiblas
%endif
Name:           CImg
Epoch:          1
Version:        4.0.5
Release:        1%{?dist}
Summary:        C++ Template Image Processing Toolkit
License:        ( CECILL-2.0 OR CECILL-C ) AND LGPL-3.0-only
URL:            https://github.com/dtschump/CImg
Source0:        https://github.com/GreycLab/CImg/archive/v.%{version}/CImg-%{version}.zip
%if %{with flexiblas}
%else
%endif
# oreon:deps
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  cmake
BuildRequires:  fftw-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  opencv-devel
BuildRequires:  openexr-devel
BuildRequires:  zlib-devel
# /oreon:deps
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

%install
install -pdm755 %{buildroot}%{_includedir}/%{name}/plugins
install -pm644 CImg.h %{buildroot}%{_includedir}/
install -pm644 plugins/*.h %{buildroot}%{_includedir}/%{name}/plugins/
%oreon_autofiles CImg-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make -C examples linux %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list
%files -n CImg-devel -f %{oreon_filedir}/CImg-devel.list

%changelog

%autochangelog
