%global source0_hash 3fb73364a5a30efe615046d07e6db9d09fd2b41c763c5f7d3bfb121cd5c5ac5a
%undefine __cmake_in_source_build
%global _vpath_builddir build
Name: yajl
Version: 2.1.0
Release:        1%{?dist}
Summary:        Yet Another JSON Library (YAJL)
License: ISC
URL: http://lloyd.github.com/yajl/
Source0:        https://codeload.github.com/lloyd/yajl/tar.gz/refs/tags/%{version}#/yajl-%{version}.tar.gz
Patch: 0001-pkg-config-file-should-be-in-lib-dir-not-shared-data.patch
Patch: 0002-pkg-config-include-dir-should-not-have-the-yajl-suff.patch
Patch: 0003-fix-patch-to-test-files-to-take-account-of-vpath.patch
Patch: 0004-drop-bogus-_s-suffix-from-yajl-dynamic-library.patch
Patch: 0005-Fix-for-CVE-2017-16516.patch
Patch: 0006-Fix-CVE-2022-24795.patch
Patch: 0007-yajl-fix-memory-leak-problem.patch
Patch: 0008-fix-memory-leaks.patch
Patch: 0009-Allow-cmake-4.0.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git
# /oreon:deps
%package devel
Summary: Libraries, includes, etc to develop with YAJL
Requires: %{name} = %{version}-%{release}
%description
Yet Another JSON Library. YAJL is a small event-driven
(SAX-style) JSON parser written in ANSI C, and a small
validating JSON generator.

%description devel
Yet Another JSON Library. YAJL is a small event-driven
(SAX-style) JSON parser written in ANSI C, and a small
validating JSON generator.

This sub-package provides the libraries and includes
necessary for developing against the YAJL library

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
   %if "%{?_lib}" == "lib64"
     %{?_cmake_lib_suffix64}
   %endif
%cmake_build
%install
%cmake_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libyajl_s.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd test
(cd parsing && ./run_tests.sh)
(cd api && ./run_tests.sh)
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n yajl-devel -f %{oreon_filedir}/yajl-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.0-1
- Import
