%global source0_hash eb87b4c2c1137959025b355296fa556b4d5a09c480e75918ee4b13c354eae29d
Name:		gssntlmssp
Version:	1.3.1
Release:        1%{?dist}
Summary:        GSSAPI NTLMSSP Mechanism
License:	LGPL-3.0-or-later
URL:		https://github.com/gssapi/gss-ntlmssp
Source0:        https://github.com/gssapi/gss-ntlmssp/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires: krb5-libs%{?_isa} >= 1.19
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gettext-devel
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wbclient)
BuildRequires:  zlib-devel
# /oreon:deps
%description
A GSSAPI Mechanism that implements NTLMSSP

%package devel
Summary: Development header for GSSAPI NTLMSSP
License: LGPL-3.0-or-later
%description devel
Adds a header file with definition for custom GSSAPI extensions for NTLMSSP

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

autoreconf -fiv
%configure \
    --with-wbclient \
    --disable-static \
    --disable-rpath
make %{?_smp_mflags} all
%install
%make_install
rm -f %{buildroot}%{_libdir}/gssntlmssp/gssntlmssp.la
mkdir -p %{buildroot}%{_sysconfdir}/gss/mech.d
install -pm644 examples/mech.ntlmssp %{buildroot}%{_sysconfdir}/gss/mech.d/ntlmssp.conf
%{find_lang} %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test_gssntlmssp
%files -f %{oreon_filedir}/main.list
%files -n gssntlmssp-devel -f %{oreon_filedir}/gssntlmssp-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-1
- Prepare for Oreon 11 (RP1)
