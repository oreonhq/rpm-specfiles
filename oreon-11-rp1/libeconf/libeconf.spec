%global source0_hash 7c311d55237f1fc6ac437caca194d170c9cae314235d60a9fbf11e980114e25e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libeconf
Version: 0.8.4
Release: 1%{?dist}
Summary: Library for merging configuration files
License: MIT
URL: https://github.com/openSUSE/libeconf
Source0: https://github.com/openSUSE/libeconf/archive/refs/tags/v%{version}.tar.gz
Patch0: 0001-cmake-no-install-html.patch
Patch1: 0002-disable-test.patch

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: make
%endif

%description
libeconf reads and merges drop-in configuration files.

%package devel
Summary: Development files for libeconf
Requires: libeconf%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libeconf)

%description devel
Headers and the libeconf link library.

%prep
%oreon_sha256
%autosetup -n libeconf-%{version} -p1

%build
%oreon_cmake
%oreon_cmake_build

%install
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.a
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
