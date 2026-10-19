%global source0_hash d6b6ed375a8ddb962530ad42a9a861ec0e931d116f07c1e60bbf89f7ca3ce1c8
Name:           libcerf
%global rname   cerf
Version:        3.8
%global         sover 3
Release:        1%{?dist}
Summary:        A library that provides complex error functions
License:        MIT
URL:            https://jugit.fz-juelich.de/mlz/lib/cerf
Source0:        https://jugit.fz-juelich.de/mlz/lib/%{rname}/-/archive/v%{version}/%{rname}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  perl-Pod-Html
BuildRequires:  perl-podlators
BuildRequires:  pkgconfig
# /oreon:deps
%description
libcerf is a self-contained numeric library that provides an efficient
and accurate implementation of complex error functions, along with
Dawson, Faddeeva, and Voigt functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

%setup -q -n %{rname}-v%{version}

%build

%cmake -DCERF_COMPILE_OPTIONS='-Wall' \
    %{nil}
%cmake_build
%install
%cmake_install
mv $RPM_BUILD_ROOT/%{_datadir}/doc/cerf/html $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}-devel
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libcerf-devel -f %{oreon_filedir}/libcerf-devel.list

%changelog

%autochangelog
