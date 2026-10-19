%global source0_hash 04763bee423e32fcad53880f1a9b4eae505112cca08bba5e789d64290bb9f3bf
%global commit be1e01ea173defc9837bd1b90dc72ed63c8131e7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           mod_auth_cas
Version:        1.3
Release:        1%{?dist}
Summary:        Apache CAS Authentication Module for the JASIG/Apereo CAS Server
License:        Apache-2.0
URL:            https://github.com/apereo/mod_auth_cas
Source0:        https://github.com/apereo/%{name}/archive/%{commit}/%{name}-v%{version}.tar.gz
Source1:        auth_cas_mod.conf
Source2:        auth_cas_httpd.conf
Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       mod_ssl
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
The purpose of this module is to allow an Apache web server to interact
with an authentication server that conforms to the CAS version 1 or 2
protocol or SAML protocol as used by the JASIG/Apereo CAS Server

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mod_auth_cas-%{commit}

%build

autoreconf -vif #BZ926155 - support aarch64
%configure --with-apxs=%{_httpd_apxs}
%make_build
%install
%make_install
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}/10-auth_cas.conf
install -Dp -m 644 %{SOURCE2} %{buildroot}%{_httpd_confdir}/auth_cas.conf
mkdir -p %{buildroot}%{_localstatedir}/cache/httpd/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
