%global source0_hash e5920fdd09cae155b89eb21a94a21c029ebfdb056c284130221525be54044aae

%global shortname naxsi

Name:           nginx-mod-naxsi
Version:        1.6
Release:        14%{?dist}
Summary:        nginx web application firewall module
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only

URL:            https://github.com/wargio/naxsi
Source0:        %{url}/archive/%{version}/%{shortname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  nginx-mod-devel
BuildRequires:  pkgconfig(libinjection)

%description
naxsi is an nginx module that provides score based Web Application Firewall
(WAF) abilities in a highly granular fashion.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{shortname}-%{version} -p1

%build
pushd naxsi_src
%nginx_modconfigure
%nginx_modbuild
popd

%install
pushd naxsi_src/%{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm0755 ngx_http_naxsi_module.so %{buildroot}%{nginx_moddir}
popd

install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/ngx_http_naxsi_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-naxsi-web-app-firewall.conf

install -dm 0755 %{buildroot}%{_datadir}/nginx/naxsi
install -m0755 naxsi_rules/naxsi_core.rules %{buildroot}%{_datadir}/nginx/naxsi/

%files
%license LICENSE
%doc README.md
%doc naxsi_rules/
%{nginx_moddir}/ngx_http_naxsi_module.so
%{nginx_modconfdir}/mod-naxsi-web-app-firewall.conf
%{_datadir}/nginx/naxsi/

%changelog
%autochangelog
