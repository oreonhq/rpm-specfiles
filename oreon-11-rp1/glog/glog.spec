%global source0_hash 00e4a87e87b7e7612f519a41e491f16623b12423620006f59f5688bfd8d13b08
Name:           glog
Version:        0.7.1
Release:        1%{?dist}
Summary:        A C++ application logging library
License:        BSD-3-Clause AND Apache-2.0
URL:            https://github.com/google/glog
Source0:        https://github.com/google/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(gflags)
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
# /oreon:deps
%description
Google glog is a library that implements application-level
logging. This library provides logging APIs based on C++-style
streams and various helper macros.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup

%conf
%cmake -DWITH_PKGCONFIG=ON

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest --exclude-regex 'logging|stacktrace|symbolize'
%files -f %{oreon_filedir}/main.list
%files -n glog-devel -f %{oreon_filedir}/glog-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.1-1
- Prepare for Oreon 11 (RP1)
