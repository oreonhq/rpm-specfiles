# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash aad782c23d3f01bd4bb52c8bac7a553b631ef8115fd1612703df6183449fef19

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global abi_ver 9

Name:           nghttp3
Version:        1.18.0
Release:        1%{?dist}
Summary:        HTTP/3 library written in C

License:        MIT
URL:            https://github.com/ngtcp2/nghttp3
Source0:        https://github.com/ngtcp2/nghttp3/releases/download/v%{version}/nghttp3-%{version}.tar.xz
Source1:        nghttp3-1.18.0.tar.xz.asc
Source2:        tatsuhiro-t.asc

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gpgverify
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  oreon-rpm-macros

%global _description %{expand:
nghttp3 is an implementation of RFC 9114 HTTP/3 mapping over QUIC
and RFC 9204 QPACK in C.
It does not depend on any particular QUIC transport implementation.}

%description %{_description}


%package -n     libnghttp3
Summary:        HTTP/3 library written in C

%description -n libnghttp3 %{_description}


%package -n     libnghttp3-devel
Summary:        Development files for libnghttp3
Requires:       libnghttp3%{?_isa} = %{version}-%{release}

%description -n libnghttp3-devel %{_description}

The libnghttp3-devel package contains libraries and header files for
developing applications that use libnghttp3.


%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1


%build
autoreconf -fiv
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
# will be installed via %%doc
rm -f %{buildroot}%{_docdir}/nghttp3/README.rst


%check
%make_build check


%files -n libnghttp3
%license COPYING
%doc README.rst
%{_libdir}/libnghttp3.so.%{abi_ver}{,.*}

%files -n libnghttp3-devel
%{_includedir}/nghttp3
%{_libdir}/libnghttp3.so
%{_libdir}/pkgconfig/libnghttp3.pc


