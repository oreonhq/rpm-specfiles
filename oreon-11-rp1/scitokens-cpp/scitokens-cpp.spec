%global source0_hash 08b9a31375c338001694f07d0945064900734074bb86e2300eacec9421360a5a
%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build
Name: scitokens-cpp
Version: 1.4.1
Release:        1%{?dist}
Summary:        C++ Implementation of the SciTokens Library
License: Apache-2.0
URL: https://github.com/scitokens/scitokens-cpp
Source0:        https://github.com/scitokens/scitokens-cpp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if 0%{?el7}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
%{summary}

%package devel
Summary: Header files for the scitokens-cpp public interfaces
Requires: %{name}%{?_isa} = %{version}
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#sed 's/ -Werror//' -i CMakeLists.txt

%build

%cmake
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n scitokens-cpp-devel -f %{oreon_filedir}/scitokens-cpp-devel.list

%changelog

%autochangelog
