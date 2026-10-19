%global source0_hash dd12cbff378deaf192ec60b8b003aa409994fda46c9acbc5e2b757e5eefc1e61
%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}
Name:		mod_http2
Version:	2.0.37
Release:        1%{?dist}
Summary:        module implementing HTTP/2 for Apache 2
License:	Apache-2.0
URL:		https://icing.github.io/mod_h2/
Source0:        https://github.com/icing/mod_h2/releases/download/v%{version}/mod_http2-%{version}.tar.gz
Requires:       httpd-mmn
Conflicts:      httpd < 2.4.48
Conflicts:      libnghttp2 < 1.50.0-1
# oreon:deps
BuildRequires:  /usr/bin/hostname
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
# /oreon:deps
%description
The mod_h2 Apache httpd module implements the HTTP2 protocol (h2+h2c) on
top of libnghttp2 for httpd 2.4 servers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
%configure --with-apxs=%{_httpd_apxs}
%make_build
%install
%make_install
rm -rf %{buildroot}/etc/httpd/share/doc/
mkdir -p %{buildroot}%{_httpd_modconfdir}
echo "LoadModule http2_module modules/mod_http2.so" > %{buildroot}%{_httpd_modconfdir}/10-h2.conf
echo "LoadModule proxy_http2_module modules/mod_proxy_http2.so" > %{buildroot}%{_httpd_modconfdir}/10-proxy_h2.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.37-1
- Prepare for Oreon 11 (RP1)
