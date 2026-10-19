%global source0_hash 2d8a3d1a67e012cc562aa7cf6105def8e23a01930bc92459c43c119a13b3ebc8
Summary:        Client and protocol library for the Couchbase project
Name: libcouchbase
Version: 3.3.19
Release:        1%{?dist}
License: Apache-2.0
URL: https://docs.couchbase.com/c-sdk/current/project-docs/sdk-release-notes.html
Source0:        https://packages.couchbase.com/clients/c/%{name}-%{version}.tar.gz
Patch0: %{name}-0001-enforce-system-crypto-policies.patch
%{?filter_provides_in: %filter_provides_in %{name}/%{name}.*\.so$}
%{?filter_setup}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libev-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libuv)
# /oreon:deps
%description
This package provides the core for libcouchbase. It contains an IO
implementation based on select(2). If preferred, you can install one
of the available back-ends (libcouchbase-libevent or libcouchbase-libev).
libcouchbase will automatically use the installed back-end. It is also
possible to integrate another IO back-end or write your own.

%package libevent
Summary: Couchbase client library - libevent IO back-end
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libevent
This package provides libevent back-end for libcouchbase.

%package libev
Summary: Couchbase client library - libev IO back-end
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libev
This package provides libev back-end for libcouchbase.

%package libuv
Summary: Couchbase client library - libuv IO back-end
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libuv
This package provides libuv back-end for libcouchbase.

%package tools
Summary: Couchbase client tools
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libevent%{?_isa} = %{version}-%{release}
%description tools
This is the CLI tools Couchbase project.

%package devel
Summary: Couchbase client library - Header files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for the Couchbase client Library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%cmake -DLCB_NO_MOCK=1 -DLCB_BUILD_DTRACE=0

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export CTEST_OUTPUT_ON_FAILURE=1
%cmake_build --target alltests
%ctest
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libcouchbase-libevent -f %{oreon_filedir}/libcouchbase-libevent.list
%files -n libcouchbase-libev -f %{oreon_filedir}/libcouchbase-libev.list
%files -n libcouchbase-libuv -f %{oreon_filedir}/libcouchbase-libuv.list
%files -n libcouchbase-tools -f %{oreon_filedir}/libcouchbase-tools.list
%files -n libcouchbase-devel -f %{oreon_filedir}/libcouchbase-devel.list

%changelog

%autochangelog
