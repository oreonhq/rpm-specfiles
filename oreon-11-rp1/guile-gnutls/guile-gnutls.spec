%global source0_hash de2bfcd4fd93d669e85f83c48a53470390fed60987158e9a14c9ff8e0beeb651

%global guile_ver 3.0

Name:    guile-gnutls
Version: 3.7.14
Release: %{?autorelease}%{!?autorelease:1%{?dist}}
Summary: Guile bindings for the GNUTLS library

License: GPL-3.0-or-later AND LGPL-2.1-or-later
URL:     https://gitlab.com/gnutls/guile
Source0: https://ftpmirror.gnu.org/gnutls/%{name}-%{version}.tar.gz
Source1: https://ftpmirror.gnu.org/gnutls/%{name}-%{version}.tar.gz.sig
Source2: https://ftp.gnu.org/gnu/gnu-keyring.gpg

Requires:      guile30
BuildRequires: gcc make
BuildRequires: gnupg2
BuildRequires: gnutls-devel
BuildRequires: guile30-devel

Provides:  gnutls-guile = %{version}-%{release}
Obsoletes: gnutls-guile <= 3.7.8-4

%description
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS
protocols and technologies around them. It provides a simple C language
application programming interface (API) to access the secure communications
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and
other required structures.
This package contains Guile bindings for the library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
guile_snarf=%{_bindir}/guile-snarf%{guile_ver}
GUILD=%{_bindir}/guild%{guile_ver}
export guile_snarf GUILD

%configure \
    --with-guile-extension-dir=%{_libdir}/guile/%{guile_ver}

%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_infodir}/gnutls*
rm -f $RPM_BUILD_ROOT%{_libdir}/guile/%{guile_ver}/guile-gnutls*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/guile/%{guile_ver}/guile-gnutls*.la

%check
#make check

%files
%license COPYING
%doc README ChangeLog AUTHORS NEWS
%{_libdir}/guile/%{guile_ver}/guile-gnutls*.so*
%{_libdir}/guile/%{guile_ver}/site-ccache/gnutls.go
%dir %{_libdir}/guile/%{guile_ver}/site-ccache/gnutls/
%{_libdir}/guile/%{guile_ver}/site-ccache/gnutls/extra.go
%{_datadir}/guile/site/%{guile_ver}/gnutls.scm
%dir %{_datadir}/guile/site/%{guile_ver}/gnutls/
%{_datadir}/guile/site/%{guile_ver}/gnutls/extra.scm

%changelog
%autochangelog
