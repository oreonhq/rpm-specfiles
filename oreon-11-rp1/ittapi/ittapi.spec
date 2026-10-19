%global source0_hash 70572732cdf41c2625fe18c8f3d4f71533b114cb6889fba18495422973560ca3
%global desc %{expand: \
The Instrumentation and Tracing Technology (ITT) API enables your application
to generate and control the collection of trace data during its execution
across different Intel tools.}
Name:		ittapi
Version:	3.28.4
Release:        1%{?dist}
Summary:        Intel Instrumentation and Tracing Technology and Just-In-Time API
License:	BSD-3-Clause and GPL-2.0-only
URL:		https://github.com/intel/ittapi
Source0:        https://github.com/intel/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	test.cpp
Patch0:		ittapi-fedora.patch
ExclusiveArch:	x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{desc}
	
%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp %{SOURCE1} .

%build

%cmake \
	-DITT_API_IPT_SUPPORT=1 \
	-DITT_API_FORTRAN_SUPPORT=0
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

$CXX -I%{buildroot}%{_includedir} -L%{buildroot}%{_libdir} -littnotify -o test test.cpp
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./test
%files -f %{oreon_filedir}/main.list
%files -n ittapi-devel -f %{oreon_filedir}/ittapi-devel.list

%changelog

%autochangelog
