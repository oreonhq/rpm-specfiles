%global source0_hash b60be61a8b0a944a66e3b719704b4c03c1bc2c22f32d5d21e99e434c82a9d769

Name: thc-ipv6
Version: 3.8
Release: 9%{?dist}
Summary: Toolkit for attacking the IPv6 protocol suite

# Automatically converted from old format: AGPLv3 with exceptions - review is highly recommended.
License: LicenseRef-Callaway-AGPLv3-with-exceptions
URL: https://github.com/vanhauser-thc/thc-ipv6
Source0: https://github.com/vanhauser-thc/thc-ipv6/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: https://github.com/vanhauser-thc/thc-ipv6/commit/5dea4ce77dbff19c53c027229365fd5aad4570d3.patch#/thc-ipv6-3.8-socket.patch
Patch1: https://github.com/vanhauser-thc/thc-ipv6/commit/c9617d5638196bd88336225a6abdfd45c3df0bcf.patch#/thc-ipv6-3.8-c23.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: libpcap-devel
BuildRequires: openssl-devel
BuildRequires: libnetfilter_queue-devel
BuildRequires: perl-generators

%description
A complete tool set to attack the inherent protocol weaknesses of IPv6
and ICMPv6, including an easy to use packet factory library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build \
  CFLAGS="%{optflags} -D_HAVE_SSL" \
  LDFLAGS="%{?__global_ldflags} -lpcap -lssl -lcrypto"

%install
%make_install \
  PREFIX=%{_prefix} \
  STRIP=%{_bindir}/true

%files
%license LICENSE LICENSE.OPENSSL
%doc CHANGES HOWTO-INJECT README
%{_bindir}/*
%{_mandir}/man8/*

%changelog
%autochangelog
