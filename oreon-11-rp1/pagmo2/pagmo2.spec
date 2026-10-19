%global source0_hash cd2d5eada6b97367360b3a84ace6193ceb80d9c451c68c1b1ad3f2ce49d0a0c2
%global gitdate 20251028
%global commit 39b8965fa2cad6de9f609a3796b16efaf64fb2e8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           pagmo2
Version:        2.19.1^%{gitdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        A C++ platform to perform parallel computations of optimisation tasks
License:        LGPL-3.0-or-later OR GPL-3.0-or-later
URL:            https://github.com/esa/pagmo2
Source0:        https://github.com/esa/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%ifnarch %{ix86}
%endif
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(ipopt)
BuildRequires:  pkgconfig(nlopt)
BuildRequires:  tbb-devel
# /oreon:deps
%description
pagmo is a C++ scientific library for massively parallel optimization. It is
built around the idea of providing a unified interface to optimization
algorithms and to optimization problems and to make their deployment in
massively parallel environments easy.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%oreon_prep
%build

%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DPAGMO_BUILD_TESTS=ON \
    -DPAGMO_WITH_EIGEN3=ON \
    -DPAGMO_WITH_NLOPT=ON \
%ifnarch %{ix86}
    -DPAGMO_WITH_IPOPT=ON \
%endif
    -DPAGMO_ENABLE_IPO=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest -E bfe
%files -f %{oreon_filedir}/main.list
%files -n pagmo2-devel -f %{oreon_filedir}/pagmo2-devel.list

%changelog

%autochangelog
