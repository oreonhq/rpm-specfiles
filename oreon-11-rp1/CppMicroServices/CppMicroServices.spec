%global source0_hash 882158dea81c4ee6246239b840ec301aef0fbf0a1ae4b032b717f6e5542791cc
%global _lto_cflags %nil
%ifarch %{ix86}
%global with_tests 0
%else
%global with_tests 1
%endif
Name: CppMicroServices
Version: 3.8.9
Release:        1%{?dist}
Summary:        C++ components for building service-oriented applications
Url: http://cppmicroservices.org/
License: %{shrink:
  Apache-2.0 AND
  %dnl third_party/tinyscheme
  BSD-3-Clause AND
  %dnl framework/include/cppmicroservices/Any.h
  %dnl webconsole/include/cppmicroservices/webconsole/mustache.hpp
  BSL-1.0 AND
  %dnl webconsole/resources/res/*.{jss,css}
  %dnl third_party/{rapidjson,optionparser,miniz}
  MIT
}
Source0:        https://github.com/CppMicroServices/CppMicroServices/archive/refs/tags/v%{version}.tar.gz#/CppMicroServices-%{version}.tar.gz
Patch: 0001-Fully-use-system-boost.patch
Patch: 0002-Use-system-jsoncpp-library.patch
Patch: 0003-Use-system-spdlog-package.patch
Patch: 0004-Replace-use-of-removed-htmlescape-function-from-sphi.patch
Patch: 0005-Remove-broken-docs-python-monkeypatching.patch
Patch: 0006-Fix-for-system-libraries-for-gmock-google-benchmark.patch
Patch: 0007-Fix-inconsistent-public-private-class-name-usage.patch
Patch: 0008-Disable-JSON-comment-test.patch
Patch: 0009-Disable-use-of-Werror.patch
Patch: 0010-Remove-use-of-docutils.error_reporting.patch
Provides: bundled(rapidjson) = 091de040edb3355dcf2f4a18c425aec51b906f08
Provides: bundled(miniz) = 3.0.2
Provides: bundled(optionparser) = 1.7
Provides: bundled(tinyscheme) = 1.41
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  gtest-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  lsof
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  rapidjson-devel
BuildRequires:  spdlog-devel
# /oreon:deps
%description
The C++ Micro Services project is a collection of components for
building modular and dynamic service-oriented applications. It
is based on OSGi, but tailored to support native cross-platform
solutions.

%package devel
Summary: Development files for CppMicroServices
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The C++ Micro Services project is a collection of components for
building modular and dynamic service-oriented applications. It
is based on OSGi, but tailored to support native cross-platform
solutions.

This provides the development headers and libraries.

%package docs
Summary: Development files for CppMicroServices
Requires: %{name}%{?_isa} = %{version}-%{release}
%description docs
The C++ Micro Services project is a collection of components for
building modular and dynamic service-oriented applications. It
is based on OSGi, but tailored to support native cross-platform
solutions.

This provides the library documentation

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Patched to use Fedora package
rm -rf third_party/benchmark

# Patched to use Fedora package
rm -rf third_party/boost

# Not really third party code AFAICT, so not
# applicable to unbundle
#rm -rf third_party/cppmicroservices_pe.h

# Not applicable to Linux build
rm -rf third_party/dirent_win32.h

# Patched to use Fedora package
rm -rf third_party/googletest

# Patched to use Fedora package
rm -rf third_party/json
rm -rf third_party/jsoncpp.cpp

# Has local modifications adding features that are not
# in upstream so can't use standard Fedora package
#rm -rf third_party/miniz*

# Not in Fedora and has local modifications adding
# features that are not in upstream so undesirable
# to add a Fedora package
#rm -rf third_party/optionparser.h

# Needs git master. Upstream is dead and won't be making
# any more releases:
#
#    https://github.com/Tencent/rapidjson/issues/1006
#
# Fedora has 1.1.0 and is resisting shipping git snapshots:
#
#    https://lists.fedorahosted.org/archives/list/devel@lists.fedoraproject.org/message/RKNCGOALWVIEYMIB5ZRPTVSH5EDG4NGU/
#rm -rf third_party/rapidjson

# Patched to use Fedora package
rm -rf third_party/spdlog

# Not in Fedora, and has build time settings for controlling
# available features that are intended to be set to match
# the application's required usage.
#rm -rf third_party/tinyscheme

%build

%cmake \
  -DUS_USE_SYSTEM_BOOST:BOOL=ON \
  -DUS_USE_SYSTEM_GTEST:BOOL=ON \
  -DUS_BUILD_TESTING:BOOL=ON \
  -DUS_MEMCHECK_COMMAND:PATH=/bin/true \
  -DUS_BUILD_DOC_HTML:BOOL=ON \
  -DUS_BUILD_DOC_MAN:BOOL=ON \
  -DLIBRARY_INSTALL_DIR=%{_libdir} \
  -DTOOLS_INSTALL_DIR=%{_bindir} \
  -DRUNTIME_INSTALL_DIR=%{_bindir} \
  -DARCHIVE_INSTALL_DIR=%{_libdir} \
  -DHEADER_INSTALL_DIR=%{_includedir}/cppmicroservices3 \
  -DAUXILIARY_INSTALL_DIR=%{_datadir}/cppmicroservices3 \
  -DDOC_INSTALL_DIR=%{_datadir}/doc/cppmicroservices3 \
  -DMAN_INSTALL_DIR=%{_mandir}
%cmake_build
%install
%cmake_install
rm -f %{buildroot}/%{_bindir}/change_namespace
%oreon_autofiles CppMicroServices-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles CppMicroServices-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%cmake_build -t test || (
  echo "==================== TEST LOGS ===================="
  cat %{__cmake_builddir}/Testing/Temporary/LastTest.log;
  exit 1
)
%files -f %{oreon_filedir}/main.list
%files -n CppMicroServices-devel -f %{oreon_filedir}/CppMicroServices-devel.list
%files -n CppMicroServices-docs -f %{oreon_filedir}/CppMicroServices-docs.list

%changelog

%autochangelog
