%global source0_hash 2c565850f05b71dd3876fa0dfcab71ec45488ec9d949a7460070930e016c378d

Summary: Client and protocol library for the Couchbase project
Name: libcouchbase
Version: 3.3.18
Release: 3%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
BuildRequires: gcc, gcc-c++
BuildRequires: cmake >= 3.5.1
BuildRequires: pkgconfig(libevent) >= 2
BuildRequires: pkgconfig(libuv) >= 1
BuildRequires: libev-devel >= 3
BuildRequires: openssl-devel
BuildRequires: make
URL: https://docs.couchbase.com/c-sdk/current/project-docs/sdk-release-notes.html
Source: https://packages.couchbase.com/clients/c/%{name}-%{version}.tar.gz
%if ! (0%{?rhel} && 0%{?rhel} <= 7)
Recommends: %{name}-libevent%{_isa} = %{version}-%{release}
Suggests: %{name}-libev%{_isa} = %{version}-%{release}
Suggests: %{name}-tools%{_isa} = %{version}-%{release}
%endif

Patch0: %{name}-0001-enforce-system-crypto-policies.patch

# exclude from "Provides" private IO plugins
%{?filter_provides_in: %filter_provides_in %{name}/%{name}.*\.so$}
%{?filter_setup}

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
# TODO: Please submit an issue to upstream (rhbz#2380712)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

%check
export CTEST_OUTPUT_ON_FAILURE=1
%cmake_build --target alltests
%ctest

%ldconfig_scriptlets

%files
%{_libdir}/%{name}.so.*
%doc README.markdown RELEASE_NOTES.markdown
%license LICENSE
%dir %{_libdir}/%{name}

%files libevent
%{_libdir}/%{name}/%{name}_libevent.so

%files libev
%{_libdir}/%{name}/%{name}_libev.so

%files libuv
%{_libdir}/%{name}/%{name}_libuv.so

%files tools
%{_bindir}/cbc*
%{_mandir}/man1/cbc*.1*
%{_mandir}/man4/cbcrc*.4*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
