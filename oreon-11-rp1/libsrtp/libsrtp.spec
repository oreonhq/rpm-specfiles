%global source0_hash bf641aa654861be10570bfc137d1441283822418e9757dc71ebb69a6cf84ea6b

Name:		libsrtp
Version:	2.6.0
Release:	4%{?dist}
Summary:	An implementation of the Secure Real-time Transport Protocol (SRTP)
License:	BSD-3-Clause
URL:		https://github.com/cisco/libsrtp
Source0:        https://github.com/cisco/libsrtp/archive/refs/tags/v2.6.0.tar.gz

BuildRequires:	gcc
BuildRequires:	doxygen
BuildRequires:	meson
BuildRequires:	procps-ng
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libpcap)
Provides:	libsrtp-tools = %{version}-%{release}
Obsoletes:	libsrtp-tools < 2.6.0-1

%description
This package provides an implementation of the Secure Real-time
Transport Protocol (SRTP), the Universal Security Transform (UST), and
a supporting cryptographic kernel.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}

%build
%meson -Dcrypto-library=openssl -Dcrypto-library-kdf=disabled
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc CHANGES README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/srtp2/
%{_libdir}/pkgconfig/libsrtp2.pc
%{_libdir}/*.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.0-4
- Prepare for Oreon 11 (RP1)
