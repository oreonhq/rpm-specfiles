%global source0_hash c3b06d077e680d112abf9f027d8a558f1176ee4a55a7c523577833391d8c2249
Name: HdrHistogram_c
Version: 0.11.10
Release:        1%{?dist}
Summary:        C port of the HdrHistogram
License: BSD-2-Clause
URL: https://github.com/HdrHistogram/%{name}
Source0:        https://github.com/HdrHistogram/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  zlib-devel
# /oreon:deps
%description
C port of High Dynamic Range (HDR) Histogram.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake -DHDR_HISTOGRAM_INSTALL_STATIC=OFF .
%cmake_build
%check

%ctest
%install
rm -rf $RPM_BUILD_ROOT
%cmake_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT
%ldconfig_post
%ldconfig_postun
%oreon_autofiles HdrHistogram_c-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n HdrHistogram_c-devel -f %{oreon_filedir}/HdrHistogram_c-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.8-10
- Prepare for Oreon 11 (RP1)
