%global source0_hash a580ac3a2df1d7b3ccef3b92147d41d5418eb22af0a2a5b893ea2e508b5765bf
%global upstream_version        1.0.3
Name:                   redisx
Version:                1.0.3
Release:        1%{?dist}
Summary:        An independent C/C++ Redis/Valkey client library and toolkit
License:                Unlicense
URL:                    https://sigmyne.github.io/redisx
Source0:        https://github.com/Sigmyne/%{name}/archive/refs/tags/v%{version}.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libbsd-devel
BuildRequires:  libomp-devel
BuildRequires:  libxchange-devel
BuildRequires:  openssl-devel
BuildRequires:  popt-devel
BuildRequires:  readline-devel
BuildRequires:  sed
# /oreon:deps
%description

RedisX is a free, light-weight Redis / Valkey client library for C/C++. It 
supports both interactive and batch Redis queries, managing and processing 
subscriptions, atomic execution blocks, and LUA script loading. It can be used 
with multiple Redis servers simultaneously also. RedisX is free to use, in any 
way you like, without licensing restrictions.

%package devel
Summary:                C development files for the RedisX C/C++ library
Requires:               %{name}%{_isa} = %{version}-%{release}
Requires:               libbsd-devel%{_isa}
Requires:               libomp-devel%{_isa}
Requires:               libxchange-devel%{_isa} >= 1.0.1
Requires:               openssl-devel%{_isa}
Requires:               popt-devel%{_isa}
Requires:               readline-devel%{_isa}
%description devel
This sub-package provides C headers and non-versioned shared library symbolic 
links for the RedisX C/C++ library.

%package doc
Summary:                Documentation for the RedisX C/C++ library
BuildArch:              noarch
%description doc
This package provides HTML documentation and examples for the RedisX C/C++ 
library. The HTML API documentation can also be used with the Eclipse IDE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install libdir=%{_libdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=$(pwd)/lib
make test
%files -f %{oreon_filedir}/main.list
%files -n redisx-devel -f %{oreon_filedir}/redisx-devel.list
%files -n redisx-doc -f %{oreon_filedir}/redisx-doc.list

%changelog

%autochangelog
