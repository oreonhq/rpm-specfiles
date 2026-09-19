%global source0_hash c22e7690546e24d46210ca92dd808f17c3102e1344cd2f9a370136a96d22319d

Name:       libsignal-protocol-c
Version:    2.3.3
Release:    17%{?dist}

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:    GPL-3.0-only
Summary:    Signal Protocol C library
URL:        https://github.com/signalapp/libsignal-protocol-c
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# CVE-2022-48468: https://bugzilla.redhat.com/show_bug.cgi?id=2186673
# Upstream is gone, so sadly we must carry this patch downstream.
Patch0:     0001-CVE-2022-48468-unsigned-integer-overflow.patch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: openssl-devel

# https://github.com/signalapp/libsignal-protocol-c/issues/103
Provides: bundled(protobuf-c) = 1.1.1

%description
This is a ratcheting forward secrecy protocol that works in synchronous
and asynchronous messaging environments.

%package devel
Summary:    Development files for libsignal-protocol-c

Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libsignal-protocol-c.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Debug .
%cmake_build

%install
%cmake_install

%check
ctest -V %{?_smp_mflags}

%files
%license LICENSE
%doc README.md
%{_libdir}/libsignal-protocol-c.so.2*

%files devel
%{_includedir}/signal
%{_libdir}/libsignal-protocol-c.so
%{_libdir}/pkgconfig/libsignal-protocol-c.pc

%changelog
%autochangelog
