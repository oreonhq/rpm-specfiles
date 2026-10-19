%global source0_hash 57d807e86a353a93024a8849f5e21e2abea4f09f0be934e1f538bdc2b02f8885
%global upver release-%{version}
Name:           libminc
Version:        2.5.0
Release:        1%{?dist}
Summary:        Core library and API of the MINC toolkit
License:        MIT
URL:            https://github.com/BIC-MNI/libminc
Source0:        https://github.com/BIC-MNI/%{name}/archive/%{upver}/%{name}-%{version}.tar.gz
Patch0:         0001-install-cmake-files-in-private-directory.patch
Patch1:         %{url}/pull/129.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  hdf5-devel
BuildRequires:  netcdf-devel
BuildRequires:  nifticlib-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The MINC file format is a highly flexible medical image file format
built on the HDF5 generalized data format. The format is
simple, self-describing, extensible, portable and N-dimensional, with
programming interfaces for both low-level data access and high-level
volume manipulation. On top of the libraries is a suite of generic
image-file manipulation tools. The format, libraries and tools are
designed for use in a medical-imaging research environment : they are
simple and powerful and make no attempt to provide a pretty interface
to users.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nifticlib-devel%{?_isa}
Requires:       netcdf-devel%{?_isa}
Requires:       zlib-devel%{?_isa}
Requires:       hdf5-devel%{?_isa}
Requires:       cmake%{?_isa}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{upver} -S git
rm -rf build/
sed -i -e '/SET (LIBMINC_INSTALL_INCLUDE_DIR/s/include/include\/%{name}/' CMakeLists.txt
sed -i -e '/CMAKE_INSTALL_RPATH/d' CMakeLists.txt

%build

%cmake ../ \
-DLIBMINC_BUILD_SHARED_LIBS=ON \
-DLIBMINC_USE_SYSTEM_NIFTI=ON \
-DLIBMINC_MINC1_SUPPORT=ON \
-DLIBMINC_BUILD_EZMINC=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest || :
%files -f %{oreon_filedir}/main.list
%files -n libminc-devel -f %{oreon_filedir}/libminc-devel.list

%changelog

%autochangelog
