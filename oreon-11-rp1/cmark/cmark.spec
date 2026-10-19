%global source0_hash f9bc5ca38bcb0b727f0056100fac4d743e768872e3bacec7746de28f5700d697
%bcond tests 0
Name:           cmark
Version:        0.31.2
Release:        1%{?dist}
Summary:        CommonMark parsing and rendering
License:        BSD-2-Clause AND MIT
URL:            https://github.com/jgm/cmark
Source0:        https://github.com/jgm/cmark/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
`cmark` is the C reference implementation of CommonMark,
a rationalized version of Markdown syntax with a spec.

It provides a shared library (`libcmark`) with functions for parsing
CommonMark documents to an abstract syntax tree (AST), manipulating
the AST, and rendering the document to HTML, groff man, LaTeX,
CommonMark, or an XML representation of the AST.  It also provides a
command-line program (`cmark`) for parsing and rendering CommonMark
documents.

%package devel
Summary:        Development files for cmark
Requires:       cmark-lib%{?_isa} = %{version}-%{release}
Requires:       cmark%{?_isa} = %{version}-%{release}
%description devel
This package provides the development files for cmark.

%package lib
Summary:        CommonMark parsing and rendering library
%description lib
This package provides the cmark library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake %{?_without_tests:-DBUILD_TESTING=OFF}
%cmake_build
%install
%cmake_install
%oreon_autofiles cmark-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cmark-lib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cmake_build --target test
%endif
%ldconfig_scriptlets lib
%files -f %{oreon_filedir}/main.list
%files -n cmark-devel -f %{oreon_filedir}/cmark-devel.list
%files -n cmark-lib -f %{oreon_filedir}/cmark-lib.list

%changelog

%autochangelog
