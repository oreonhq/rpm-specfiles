%global source0_hash dde68d3fa2a9fc7f52e436d2edc53c6d703dcd911283965d889102d3a877c778

%global nginx_modname headers-more
%global origname %{nginx_modname}-nginx-module

Name:           nginx-mod-headers-more
Version:        0.39
Release:        6%{?dist}
Summary:        This module allows adding, setting, or clearing specified input/output headers

License:        BSD-2-Clause
URL:            https://github.com/openresty/headers-more-nginx-module
Source0:        %{url}/archive/v%{version}/%{origname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  nginx-mod-devel

%description
%{summary}.

This is an enhanced version of the standard headers module because it provides
more utilities like resetting or clearing "builtin headers" like Content-Type,
Content-Length, and Server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{origname}-%{version}

%build
%nginx_modconfigure
%nginx_modbuild

%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_headers_more_filter_module.so %{buildroot}%{nginx_moddir}
install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/ngx_http_headers_more_filter_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-headers-more.conf
popd

%files
%doc README.markdown
%license LICENSE
%{nginx_moddir}/ngx_http_headers_more_filter_module.so
%{nginx_modconfdir}/mod-headers-more.conf

%changelog
%autochangelog
