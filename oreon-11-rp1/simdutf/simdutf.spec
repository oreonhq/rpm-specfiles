%global source0_hash b4b4f397065bb8f2ba2386feb40e58e27654c71c6f7521d9cbd32a16142bd040
%global lib_ver 34.0.0
%global so_ver 34
Name:		simdutf
Version:	9.2.0
Release:        1%{?dist}
Summary:        Unicode validation and transcoding at billions of characters per second
License:	Apache-2.0 AND BSD-3-Clause
URL:		https://github.com/simdutf/simdutf
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%ifnarch %{arm}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libasan
BuildRequires:  make
# /oreon:deps
%description
Unicode (UTF8, UTF16, UTF32) validation and transcoding at billions of 
characters per second using SSE2, AVX2, NEON, AVX-512.

%package devel
Summary: Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description devel
The package contains libraries and header files for developing applications
that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DSIMDUTF_BENCHMARKS=OFF \
	-DSIMDUTF_TOOLS=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n simdutf-devel -f %{oreon_filedir}/simdutf-devel.list

%changelog

%autochangelog

