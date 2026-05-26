Name:		libsrtp
Version:	2.6.0
Release:	4%{?dist}
Summary:	An implementation of the Secure Real-time Transport Protocol (SRTP)
License:	BSD-3-Clause
URL:		https://github.com/cisco/libsrtp
Source0:	https://github.com/cisco/libsrtp/archive/v%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 bf641aa654861be10570bfc137d1441283822418e9757dc71ebb69a6cf84ea6b
%global source0_file v2.6.0.tar.gz
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v2.6.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bf641aa654861be10570bfc137d1441283822418e9757dc71ebb69a6cf84ea6b" || { echo "oreon: Source0 SHA256 mismatch for v2.6.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
