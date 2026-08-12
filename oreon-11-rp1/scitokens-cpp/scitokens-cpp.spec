%global source0_hash 08b9a31375c338001694f07d0945064900734074bb86e2300eacec9421360a5a

%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

Name: scitokens-cpp
Version: 1.4.1
Release:        2%{?dist}
Summary: C++ Implementation of the SciTokens Library
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/scitokens/scitokens-cpp

# Directions to generate a proper release:
# git archive --prefix "scitokens-cpp-0.3.3/" -o "scitokens-cpp-0.3.3.tar" v0.3.3
# git submodule update --init
# git submodule foreach --recursive "git archive --prefix=scitokens-cpp-0.3.3/\$path/ --output=\$sha1.tar HEAD && tar --concatenate --file=$(pwd)/scitokens-cpp-0.3.3.tar \$sha1.tar && rm \$sha1.tar"
# gzip "scitokens-cpp-0.3.3.tar"
Source0: https://github.com/scitokens/scitokens-cpp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix build failure with GCC10.1 and Werror (upstream pull request)
# https://github.com/kazuho/picojson/pull/131
#Patch0: %{name}-paren.patch

# Scitokens-cpp bundles jwt-cpp, a header only dependency
# Since it doesn't create a library that can be used by others, it seems
# inappropriate to include a "Provides", as jwt-cpp is not provided
# by this package.

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake
BuildRequires: sqlite-devel
BuildRequires: openssl-devel
BuildRequires: libcurl-devel
BuildRequires: libuuid-devel

%if 0%{?el7}
# needed for ldconfig_scriptlets
BuildRequires: epel-rpm-macros
BuildRequires: cmake3
%endif

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

# Run the ldconfig
%ldconfig_scriptlets

%files
%{_libdir}/libSciTokens.so.0*
%{_bindir}/scitokens-*
%license LICENSE
%doc README.md

%files devel
%{_libdir}/libSciTokens.so
%{_includedir}/scitokens/scitokens.h
%dir %{_includedir}/scitokens

%changelog
%autochangelog
