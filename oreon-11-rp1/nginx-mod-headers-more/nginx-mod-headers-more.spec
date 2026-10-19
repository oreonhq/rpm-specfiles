%global source0_hash c14cb5e6c998590c209efbf77bd7637ce2cab02332e4192756a8af5b26ba4284
%global nginx_modname headers-more
%global origname %{nginx_modname}-nginx-module
Name:           nginx-mod-headers-more
Version:        0.40
Release:        1%{?dist}
Summary:        This module allows adding, setting, or clearing specified input/output headers
License:        BSD-2-Clause
URL:            https://github.com/openresty/headers-more-nginx-module
Source0:        https://github.com/openresty/%{origname}/archive/v%{version}/%{origname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  nginx-mod-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
