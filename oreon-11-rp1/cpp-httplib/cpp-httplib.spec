%global source0_hash 31932ce8b33f2905472a987dc1984b9d8a7d338083a066021349587cc5f1cfea
%global forgeurl https://github.com/yhirose/cpp-httplib
%undefine __cmake_in_source_build
%bcond_without tests
%bcond_with    online
%bcond_with compile
%if %{without compile}
%undefine __cmake_in_source_build
%global debug_package %{nil}
%endif
Name:           cpp-httplib
Version:        0.58.0
%global tag v%{version}
%forgemeta
Release:        1%{?dist}
Summary:        A C++11 single-file header-only cross platform HTTP/HTTPS library
License:        MIT
URL:            https://github.com/yhirose/cpp-httplib
VCS:            git:%{forgeurl}
Source0:        %{forgeurl}/archive/%{tag}/%{name}-%{version}.tar.gz
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  brotli-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libcurl-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  redhat-rpm-config
BuildRequires:  zlib-devel
# /oreon:deps
%description
A C++11 single-file header-only cross platform HTTP/HTTPS library.

It's extremely easy to setup. Just include the httplib.h file in your code!

%package devel
Summary:        A C++11 single-file header-only cross platform HTTP/HTTPS library
Recommends:     cmake
Requires:       cmake-filesystem%{?_isa}
Requires:       openssl-devel%{?_isa} zlib-devel%{?_isa} brotli-devel%{?_isa}
%if %{with compile}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%else
Provides:       %{name}-static = %{version}-%{release}
%endif
%description devel
A C++11 single-file header-only cross platform HTTP/HTTPS library.

It's extremely easy to setup. Just include the httplib.h file in your code!

NOTE: This is a multi-threaded 'blocking' HTTP library.
If you are looking for a 'non-blocking' library, this is not the one that you want.

Development files only.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake \
%if %{with compile}
    -DBUILD_SHARED_LIBS=ON -DHTTPLIB_COMPILE=ON \
%endif
%if %{with tests}
    -DHTTPLIB_TEST=ON \
%endif
%cmake_build
%install
%cmake_install
rm -r $RPM_BUILD_ROOT%{_docdir}/httplib
rm -r $RPM_BUILD_ROOT%{_licensedir}/httplib
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{with tests}
%if %{with online}
  %ctest --parallel 1
%else
  %ifnarch %{ix86}
    %ctest --parallel 1 --exclude-regex '^MaxTimeoutTest.ContentStream|_Online$'
  %else
    %ctest --parallel 1 --exclude-regex '^ETagTest.LastModifiedAndIfModifiedSince|^ETagTest.IfRangeWithDate|^WebSocketIntegrationTest.LargeMessage|^WebSocketIntegrationTest.MaxPayloadAtLimit|^MaxTimeoutTest.ContentStream|_Online$'
  %endif
%endif
%endif
%if %{with compile}
%files -f %{oreon_filedir}/main.list
%files -n cpp-httplib-devel -f %{oreon_filedir}/cpp-httplib-devel.list

%changelog

%autochangelog
%endif
