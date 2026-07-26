%global source0_hash 4b0d14e5bfe77ce419affd253366e861968ae6ef2c35ae293727c1415bd145c8

# https://bugzilla.redhat.com/show_bug.cgi?id=2394765
%global _lto_cflags %nil
%undefine __cmake_in_source_build
%define major 2
%define minor 10
Name:           cpprest
Version:        2.10.19
Release:        11%{?dist}
Summary:        C++ REST library
License:        MIT
Url:            https://github.com/Microsoft/cpprestsdk
Source0:        https://github.com/Microsoft/cpprestsdk/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Disable outside, failing and sometimes failing tests
Patch1:         cpprest-2.10.17-disable-outside-and-failing-tests.patch
# Disable tests with long timeouts
Patch2:         cpprest-2.10.9-disable-tests-long-timeouts.patch
# Disable test extract_floating_point, which fails on ppc64le and aarch64
Patch3:         cpprest-2.10.9-disable-test-extract_floating_point.patch
# Revert "libcpprestsdk: fix building as a static library (#1344)"
# https://github.com/microsoft/cpprestsdk/pull/1401
Patch4:         cpprest-2.10.16-revert_commit_cb7ca74.patch
# Fix Boost asio errors
# Patch modified from:
# https://github.com/microsoft/vcpkg/pull/42678
# https://raw.githubusercontent.com/microsoft/vcpkg/566f949/ports/cpprestsdk/fix-asio-error.patch
# Additionally fixed: Release/tests/functional/pplx/pplx_test/pplx_op_test.cpp
Patch5:         cpprest-2.10.19-fix-boost-asio-errors.patch

BuildRequires:  boost-devel >= 1.55
# The lowest version in currently supported Fedora was tested under F27: brotli-devel 0.6.0
BuildRequires:  pkgconfig(libbrotlidec) >= 0.6.0
BuildRequires:  pkgconfig(libbrotlienc) >= 0.6.0
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(openssl) >= 1.0
BuildRequires:  openssl-devel-engine
BuildRequires:  websocketpp-devel >= 0.5.1
BuildRequires:  pkgconfig(zlib)

%description
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

Also known as Casablanca.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       pkgconfig(openssl)

%description devel
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

Development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cpprestsdk-%{version} -p1
# Remove bundled sources of websocketpp
rm -r Release/libs
# Remove file ThirdPartyNotices.txt, which is associated to websocketpp
rm ThirdPartyNotices.txt

%build
cd Release
# https://fedoraproject.org/wiki/Common_Rpmlint_issues#unused-direct-shlib-dependency
# -Wl,--as-needed
export CXXFLAGS="%{optflags} -Wl,--as-needed"
# Not needed anymore since v2.10.15 (new default): -DCPPREST_EXPORT_DIR=cmake/cpprestsdk
%cmake -DCMAKE_BUILD_TYPE=Release -DWERROR=OFF -DCPPREST_EXCLUDE_BROTLI=OFF
%cmake_build

%install
cd Release
%cmake_install

%check
%ifarch ppc64 s390x
# Do not run tests for ppc64 and s390x, because of many failing, even crashing tests
# See https://koji.fedoraproject.org/koji/taskinfo?taskID=20183925
%else
# Run tests for the other buildArchs like x86_64, ppc64le, aarch64, i686, armv7hl
cd Release/%{_vpath_builddir}/Binaries
./test_runner *_test.so ||:
%endif

%ldconfig_scriptlets

%files
%doc CONTRIBUTORS.txt
%license license.txt
%{_libdir}/libcpprest.so.%{major}.%{minor}

%files devel
%doc CONTRIBUTORS.txt
%{_includedir}/%{name}
%{_includedir}/pplx
%{_libdir}/libcpprest.so
%{_libdir}/cmake/cpprestsdk

%changelog
%autochangelog
