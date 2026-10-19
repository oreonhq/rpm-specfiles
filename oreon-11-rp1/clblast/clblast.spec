%global source0_hash cac83330a6110214f2b7efc8e46062536f40ba96122f3b2a074a51497d8ca9e7
%bcond check 1
%bcond_with pocl
Name:           clblast
Version:        1.7.0
Release:        1%{?dist}
Summary:        Tuned OpenCL BLAS routines
License:        Apache-2.0
URL:            https://cnugteren.github.io/clblast/clblast.html
Source0:        https://github.com/CNugteren/CLBlast/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-altivec.patch
%if %{with pocl}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  ocl-icd-devel
BuildRequires:  pkgconfig(flexiblas)
# /oreon:deps
%description
CLBlast is a modern, lightweight, performant and tunable OpenCL BLAS
library written in C++11.  It is designed to leverage the full
performance potential of a wide variety of OpenCL devices from different
vendors, including desktop and laptop GPUs, embedded GPUs, and other
accelerators.  CLBlast implements BLAS routines: basic linear algebra
subprograms operating on vectors and matrices.  See the CLBlast website
for performance reports on various devices as well as the latest CLBlast
news.

The library is not tuned for all possible OpenCL devices: if
out-of-the-box performance is poor, please run the tuners first.

%package devel
Summary:        Headers and libraries for CLBlast
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocl-icd-devel%{?_isa}
%description devel
Headers and libraries for developing applications that use CLBlast.

%package clients
Summary:        Clients for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description clients
Clients to test and compare performance of %{name} for your OpenCL device.

%package tuners
Summary:        Tuners for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tuners
Programs to tune %{name} for your OpenCL device.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n CLBlast-%{version}

# Fix the path to the openblas headers
sed -i 's,openblas/include,include/openblas,' cmake/Modules/FindCBLAS.cmake
# Add paths for FlexiBLAS
sed -i 's,include/openblas,include/openblas include/flexiblas,' cmake/Modules/FindCBLAS.cmake
sed -i 's,NAMES cblas blas,NAMES cblas blas flexiblas,' cmake/Modules/FindCBLAS.cmake
# For CMake 4
sed -i 's@cmake_minimum_required(VERSION 2.8.11@cmake_minimum_required(VERSION 3.5@' CMakeLists.txt
sed -i 's@cmake_minimum_required(VERSION 3.20@cmake_minimum_required(VERSION 3.5@' src/pyclblast/CMakeLists.txt

%build

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCLIENTS=ON \
  -DNETLIB=ON \
%if %{with check}
  -DTESTS=ON \
  -DCMAKE_CXX_FLAGS="%{optflags} -Wno-error=format-security" \
%else
  -DTESTS=OFF \
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles clblast-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles clblast-clients usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles clblast-tuners usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n clblast-devel -f %{oreon_filedir}/clblast-devel.list
%files -n clblast-clients -f %{oreon_filedir}/clblast-clients.list
%files -n clblast-tuners -f %{oreon_filedir}/clblast-tuners.list

%changelog

%autochangelog
