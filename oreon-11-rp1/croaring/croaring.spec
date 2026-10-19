%global source0_hash none
%global forgeurl https://github.com/RoaringBitmap/CRoaring
Version:        5.2.2
%forgemeta
%global sover 18
Name:           croaring
Release:        1%{?dist}
Summary:        Roaring bitmaps in C (and C++), with SIMD (AVX2, AVX-512 and NEON) optimizations
License:        Apache-2.0 OR MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/CRoaring-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcmocka-devel
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%prep

%forgeautosetup -p1

%build

%cmake \
    -DROARING_USE_CPM=OFF \
    -DROARING_LIB_VERSION=%{version} \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n croaring-devel -f %{oreon_filedir}/croaring-devel.list

%changelog

%autochangelog
