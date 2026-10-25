%global source0_hash ffed8ec1bf09c2426d4f14aae377de4753b53e537d685e604e99a8b16ca9c97e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gnutls
Version: 3.8.13
Release: 1%{?dist}
Summary: TLS library
License: LGPL-2.1-or-later
URL: https://www.gnutls.org/
Source0: https://www.gnupg.org/ftp/gcrypt/gnutls/v3.8/gnutls-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: gmp-devel
BuildRequires: nettle-devel
BuildRequires: libtasn1-devel
BuildRequires: p11-kit-devel
BuildRequires: libidn2-devel
BuildRequires: libunistring-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
BuildRequires: pkgconf
%endif

%description
TLS library

%package devel
Summary: TLS library
Requires: gnutls%{?_isa} = %{version}-%{release}

%description devel
TLS library

%prep
%oreon_sha256
%autosetup -n gnutls-3.8.13 -p1

%build
%oreon_configure --disable-static --disable-guile --without-tpm2 --with-zstd
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING.LESSERv2

%files devel -f %{_builddir}/%{name}-devel.files
