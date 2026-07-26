%global source0_hash 04763bee423e32fcad53880f1a9b4eae505112cca08bba5e789d64290bb9f3bf

%global commit be1e01ea173defc9837bd1b90dc72ed63c8131e7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mod_auth_cas
Version:        1.2
Release:        12%{?dist}
Summary:        Apache CAS Authentication Module for the JASIG/Apereo CAS Server

License:        Apache-2.0
URL:            https://github.com/apereo/mod_auth_cas
Source0:        https://github.com/apereo/mod_auth_cas/archive/%{commit}/%{name}-v%{version}.tar.gz
Source1:        auth_cas_mod.conf
Source2:        auth_cas_httpd.conf

BuildRequires:  openssl-devel
BuildRequires:  httpd-devel
BuildRequires:  m4, readline-devel, autoconf, automake
BuildRequires:  libcurl-devel
BuildRequires:  libtool
# Created issue with upstream https://github.com/apereo/mod_auth_cas/issues/208
BuildRequires:  pcre2-devel
BuildRequires:  gcc

Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       mod_ssl

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

%files
%doc README
%{_libdir}/httpd/modules/mod_auth_cas.so
%config(noreplace) %{_httpd_confdir}/auth_cas.conf
%config(noreplace) %{_httpd_modconfdir}/10-auth_cas.conf

%dir %attr(-,apache,apache) %{_localstatedir}/cache/httpd/%{name}

%changelog
%autochangelog
