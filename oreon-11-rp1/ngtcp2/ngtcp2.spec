%global source0_hash 2a34d2484ba17847a5d11965704e9dd0fac4c6d8efc75ffe1ec7de66d8c6b6fb
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: ngtcp2
Version: 1.25.0
Release: 1%{?dist}
Summary: QUIC protocol library
License: MIT
URL: https://github.com/ngtcp2/ngtcp2
Source0: https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz
Source1: ngtcp2-%{version}.tar.xz.asc
Source2: ngtcp2-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: patchelf
BuildRequires: pkgconf
BuildRequires: openssl-devel
BuildRequires: gnutls-devel
%endif

%description
ngtcp2 implements the QUIC protocol (RFC 9000). This build ships the
library and the OpenSSL and GnuTLS crypto helper libraries.

%package devel
Summary: Development files for ngtcp2
Requires: ngtcp2%{?_isa} = %{version}-%{release}
Provides: pkgconfig(ngtcp2)

%description devel
Headers and libraries for developing against ngtcp2.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n ngtcp2-%{version} -p1

%build
%oreon_configure --disable-static --enable-lib-only --with-openssl --with-gnutls
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
