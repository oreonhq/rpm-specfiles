%global source0_hash 260107caf318650a57a8caa593550e39bca6943e93f970c80d6c17e59d62cd92

Name: usrsctp
Version: 0.9.5.0
Release: 12%{?dist}
Epoch: 1

License: BSD-3-Clause
Summary: Portable SCTP userland stack
URL: https://github.com/sctplab/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: gcc

%description
SCTP is a message oriented, reliable transport protocol with direct support
for multihoming that runs on top of IP or UDP, and supports both v4 and v6
versions.

Like TCP, SCTP provides reliable, connection oriented data delivery with
congestion control. Unlike TCP, SCTP also provides message boundary
preservation, ordered and unordered message delivery, multi-streaming and
multi-homing. Detection of data corruption, loss of data and duplication
of data is achieved by using checksums and sequence numbers. A selective
retransmission mechanism is applied to correct loss or corruption of data.

In this manual the socket API for the SCTP User-land implementation will be
described. It is based on RFC 6458. The main focus of this document is on
pointing out the differences to the SCTP Sockets API. For all aspects of the
sockets API that are not mentioned in this document, please refer to RFC
6458. Questions about SCTP itself can hopefully be answered by RFC 4960.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson \
    -Dwerror=false \
    -Dsctp_debug=false \
    -Dsctp_inet=true \
    -Dsctp_inet6=true \
    -Dsctp_build_programs=false
%meson_build

%check
%meson_test

%install
%meson_install

%files
%doc README.md Manual.md
%license LICENSE.md
%{_libdir}/lib%{name}.so.2*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
