%global source0_hash a4bb89a2704b2a9461fbc9c0397f326b092c358d9d12b6311c2aa63d161f0530
Name:           mod_auth_gssapi
Version:        1.6.5
Release:        1%{?dist}
Summary:        A GSSAPI Authentication module for Apache
License:        MIT
URL:            https://github.com/gssapi/mod_auth_gssapi
Source0:        https://github.com/gssapi/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires:       httpd-mmn
Requires:       krb5-libs >= 1.11.5
%if 0%{?rhel} || (0%{?oreon} >= 11)
%else
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  git
BuildRequires:  gssntlmssp-devel
BuildRequires:  httpd-devel
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
The mod_auth_gssapi module is an authentication service that implements the
SPNEGO based HTTP Authentication protocol defined in RFC4559.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export APXS=%{_httpd_apxs}
autoreconf -fi
%configure
make %{?_smp_mflags}
%install
mkdir -p %{buildroot}%{_httpd_moddir}
install -m 755 src/.libs/%{name}.so %{buildroot}%{_httpd_moddir}
echo "LoadModule auth_gssapi_module modules/mod_auth_gssapi.so" > 10-auth_gssapi.conf
mkdir -p %{buildroot}%{_httpd_modconfdir}
install -m 644 10-auth_gssapi.conf %{buildroot}%{_httpd_modconfdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.5-1
- Import
