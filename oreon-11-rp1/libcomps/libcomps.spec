%global source0_hash c24a81dea8e9f7f3c877618d3812a5293df772abc6b90fad1d34fa62326141bc
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}
%global py3_sitearch %{_libdir}/python%(python3 -c 'import sys;print("%d.%d"%sys.version_info[:2])' 2>/dev/null)/site-packages

Name: libcomps
Version: 0.1.24
Release: 6%{?dist}
Summary: Comps XML library
License: GPL-2.0-or-later
URL: https://github.com/rpm-software-management/libcomps
Source0: https://github.com/rpm-software-management/libcomps/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: expat-devel
BuildRequires: libxml2-devel
BuildRequires: zlib-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: patchelf

%description
libcomps reads and writes comps XML.

%package devel
Summary: Comps XML library
Requires: libcomps%{?_isa} = %{version}-%{release}

%description devel
libcomps reads and writes comps XML.

%package -n python3-libcomps
Summary: Python 3 bindings for libcomps
Requires: libcomps%{?_isa} = %{version}-%{release}

%description -n python3-libcomps
Python 3 bindings for the libcomps library.

%prep
%oreon_sha256
%autosetup -p1

%build
cd libcomps
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DENABLE_TESTS=OFF \
  -DENABLE_DOCS=OFF \
  -DBUILD_LIBCOMPS_SHARED=ON
%oreon_cmake_build

%install
cd libcomps
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libcomps.so.0

%files devel
%{_includedir}/libcomps/
%{_libdir}/libcomps.so
%{_libdir}/pkgconfig/libcomps.pc

%files -n python3-libcomps
%{py3_sitearch}/libcomps/
%{py3_sitearch}/libcomps-%{version}-py*.egg-info/
