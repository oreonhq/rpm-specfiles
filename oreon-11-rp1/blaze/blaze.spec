%global source0_hash 4c4e1915971efbedab95790e4c5cf017d8448057fa8f8c62c46e1643bf72cbb1
%global debug_package %{nil}
Name:           blaze
Version:        3.8.2
Release:        9%{?dist}
Summary:        An high-performance C++ math library for dense and sparse arithmetic
License:        LicenseRef-Callaway-BSD
URL:            https://bitbucket.org/blaze-lib/blaze
Source0:        https://bitbucket.org/blaze-lib/blaze/downloads/%{name}-%{version}.tar.gz
%global blaze_desc \
Blaze is an open-source, high-performance C++ math library for dense and \
sparse arithmetic. With its state-of-the-art Smart Expression Template \
implementation Blaze combines the elegance and ease of use of a \
domain-specific language with HPC-grade performance, making it one of \
the most intuitive and fastest C++ math libraries available. \
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description 
%{blaze_desc}

%package devel
Summary:    Development headers for BLAZE
Provides:   blaze-static = %{version}-%{release}
Requires: flexiblas-devel
Requires: boost
%description devel
%{blaze_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

pushd blaze
%{cmake} -DLIB=%{_lib} -DBLA_VENDOR=FlexiBLAS %{?cmake_opts:%{cmake_opts}} ..
cd %{__cmake_builddir}
%make_build
cd ..
popd
%install
pushd blaze
cd %{__cmake_builddir}
%make_install
cd ..
popd
rm -rf %{_includedir}/%{name}/CMakeFiles/3.12.2
rm -rf %{_includedir}/%{name}/CMakeFiles/FindOpenMP
%oreon_autofiles blaze-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n blaze-devel -f %{oreon_filedir}/blaze-devel.list

%changelog

%autochangelog
