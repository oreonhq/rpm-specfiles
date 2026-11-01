%global source0_hash 815bfe6792aa11a13a133b86e7f0f45edc5d71eb78f5fb6686c49c7f792b9049
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: toml11
Version: 4.4.0
Release: 1%{?dist}
Summary: Header-only TOML library for C++11
License: MIT
URL: https://github.com/ToruNiina/toml11
Source0: https://github.com/ToruNiina/toml11/archive/v%{version}/toml11-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc-c++
BuildRequires: make
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: cmake
BuildRequires: ninja-build
%endif

%description
toml11 is a header-only C++11 TOML parser and serializer.

%package devel
Summary: Header-only TOML library for C++11
Provides: toml11-static = %{version}-%{release}
Provides: cmake(toml11)

%description devel
toml11 is a header-only C++11 TOML parser and serializer.

%prep
%oreon_sha256
%autosetup -n toml11-%{version} -p1

%build
%oreon_cmake -DTOML11_BUILD_TESTS=OFF -DTOML11_BUILD_EXAMPLES=OFF
%oreon_cmake_build

%install
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist

%files devel -f %{_builddir}/%{name}.files
%license LICENSE
