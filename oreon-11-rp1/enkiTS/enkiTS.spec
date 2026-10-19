%global source0_hash 1d531d9e4aaeb2fdf2c643558d2578ae18f1adebe22a97168b9ba6451edcd87e
%global forgeurl  https://github.com/dougbinks/enkiTS
%global version0  1.11
%global commit 686d0ec31829e0d9e5edf9ceb68c40f9b9b20ea9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta
Name:           enkiTS
Version:        %{forgeversion}
Release:        1%{?dist}
Summary:        A C and C++ task scheduler for creating parallel programs
License:        Zlib
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
The primary goal of enkiTS is to help developers create programs which handle
both data and task level parallelism to utilize the full performance of
multicore CPUs, whilst being lightweight (only a small amount of code) and easy
to use.

%package devel
Summary:   A C and C++ task scheduler for creating parallel programs
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for enkiTS.

%package examples
Summary:   A C and C++ task scheduler for creating parallel programs
BuildArch:  noarch
%description examples
Examples for how to use enkiTS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

%build

%cmake -DENKITS_BUILD_SHARED=ON \
       -DENKITS_BUILD_C_INTERFACE=ON \
       -DENKITS_BUILD_EXAMPLES=ON \
       -DENKITS_INSTALL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{_vpath_builddir}/TestAll
%files -f %{oreon_filedir}/main.list
%files -n enkiTS-devel -f %{oreon_filedir}/enkiTS-devel.list
%files -n enkiTS-examples -f %{oreon_filedir}/enkiTS-examples.list

%changelog

%autochangelog
