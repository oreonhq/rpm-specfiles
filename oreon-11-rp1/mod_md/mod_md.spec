%global source0_hash 674117771ec8bae121513876e8cadb1cef354d8867576373c7994224c925d770
%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}
%{!?_httpd_statedir: %global _httpd_statedir %{_localstatedir}/lib/httpd}
Name:           mod_md
Version:        2.6.7
Release:        1%{?dist}
Summary:        Certificate provisioning using ACME for the Apache HTTP Server
License:        Apache-2.0
URL:            https://icing.github.io/mod_md/
Source0:        https://github.com/icing/mod_md/releases/download/v%{version}/mod_md-%{version}.tar.gz
Patch1:         mod_md-2.0.8-state_dir.patch
Requires:       httpd-mmn, mod_ssl >= 1:2.4.41
Conflicts:      httpd < 2.4.39-7
Epoch:          1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  jansson-devel
BuildRequires:  libcurl-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  xmlto
# /oreon:deps
%description
This module manages common properties of domains for one or more
virtual hosts. Specifically it can use the ACME protocol to automate
certificate provisioning.  Certificates will be configured for managed
domains and their virtual hosts automatically, including at renewal.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --with-apxs=%{_httpd_apxs}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build V=1
%check

%make_build check
%install
%make_install
rm -rf %{buildroot}/etc/httpd/share/doc/
rm -f %{buildroot}%{_httpd_moddir}/mod_md.so
mv %{buildroot}%{_httpd_moddir}/mod_md.so.0.0.0 %{buildroot}%{_httpd_moddir}/mod_md.so
mkdir -p %{buildroot}%{_httpd_modconfdir} %{buildroot}%{_httpd_statedir}/md
echo "LoadModule md_module modules/mod_md.so" > %{buildroot}%{_httpd_modconfdir}/01-md.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.7-1
- Prepare for Oreon 11 (RP1)
