%global source0_hash 75565e2d4cc8e3ce2dd7927f5c75cc5ebbd3b620468cb0226501dae68d8fe1cd
%bcond check 1
Name:		ada-url
Version:	3.3.0
%global forgeurl https://github.com/%{name}/ada
%forgemeta
Release:        1%{?dist}
Summary:        WHATWG-compliant and fast URL parser written in modern C++
License:	Apache-2.0 OR MIT
URL:		https://www.ada-url.com/
Source0:        %{forgeurl}/archive/v%{version}/ada-%{version}.tar.gz
Patch0:		1000-Remove-cmake-CPM.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(cxxopts)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(simdjson)
BuildRequires:  cmake(simdutf)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
# /oreon:deps
%description
Ada is a fast and spec-compliant URL parser written in C++.
Specification for URL parser can be found from the WHATWG website.

The Ada library passes the full range of tests from the specification,
across a wide range of platforms.
It fully supports the relevant Unicode Technical Standard.

%package tools
Summary:	Tools for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description tools
This package contains command line utility for parsing URL.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:	Developer documentation for %{name}
Recommends:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
The %{name}-doc package contains developer documentation for
the %{name} package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake \
  -DADA_TOOLS:BOOL=ON \
%if %{with check}
  -DADA_TESTING:BOOL=ON \
%endif
  -DADA_USE_SIMDUTF:BOOL=ON
%cmake_build
doxygen ./doxygen
%install
%cmake_install
%oreon_autofiles ada-url-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ada-url-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ada-url-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n ada-url-tools -f %{oreon_filedir}/ada-url-tools.list
%files -n ada-url-devel -f %{oreon_filedir}/ada-url-devel.list
%files -n ada-url-doc -f %{oreon_filedir}/ada-url-doc.list

%changelog

%autochangelog
