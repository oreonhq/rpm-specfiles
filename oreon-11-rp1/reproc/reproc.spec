%global source0_hash d6ae44f96a5c33a43aec1c7fda735bb59f26bf4160531a3610ffedb77d792438
%global commit 1c07bdbec3f2ecba7125b9499b9a8a77bf9aa8c7
%global shortcommit %(c=%commit; echo ${c:0:7})
Name:           reproc
Version:        14.2.4
Release:        1%{?dist}
Summary:        A cross-platform (C99/C++11) process library
License:        MIT 
URL:            https://github.com/DaanDeMeyer/reproc
Source0:        https://github.com/DaanDeMeyer/%{name}/archive/%{commit}/%{name}-%{version}-1c07bdb.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
reproc (Redirected Process) is a cross-platform C/C++ library that simplifies
starting, stopping and communicating with external programs. The main use case
is executing command line applications directly from C or C++ code and
retrieving their output.

reproc consists out of two libraries: reproc and reproc++. reproc is a C99
library that contains the actual code for working with external programs.
reproc++ depends on reproc and adapts its API to an idiomatic C++11 API. It
also adds a few extras that simplify working with external programs from C++.

%package        devel
Summary:        Development files for %{name}
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

%cmake -DREPROC++=ON -DREPROC_TEST=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n reproc-devel -f %{oreon_filedir}/reproc-devel.list

%changelog

%autochangelog
