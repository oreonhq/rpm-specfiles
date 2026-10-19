%global source0_hash c85cdcfd76703c95aa4204ee4c2e619aa5b075cac18f428202f65552104add3b
%global baseversion 1.0.0
%global prerel rc
%global upstream_tag %{baseversion}%{?prerel}
Name:           nginx-mod-brotli
Version:        %{baseversion}%{?prerel:~%{prerel}}
Release:        1%{?dist}
Summary:        NGINX module for Brotli compression
License:        BSD-2-Clause
URL:            https://github.com/google/ngx_brotli
Source0:        https://github.com/google/ngx_brotli/a%{prerel}hive/v%{baseversion}%{prerel}/ngx_brotli-%{baseversion}%{prerel}.tar.gz
Patch:          https://patch-diff.githubusercontent.com/raw/google/ngx_brotli/pull/150.patch
Patch:          https://patch-diff.githubusercontent.com/raw/google/ngx_brotli/pull/172.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  nginx-mod-devel
BuildRequires:  pkgconfig(libbrotlienc)
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ngx_brotli-%{upstream_tag} -p1

%build

%nginx_modconfigure
%nginx_modbuild
%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_brotli_filter_module.so %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_brotli_static_module.so %{buildroot}%{nginx_moddir}
install -dm 0755 %{buildroot}%{nginx_modconfdir}
cat <<EOF > %{buildroot}%{nginx_modconfdir}/mod-brotli.conf
load_module "%{nginx_moddir}/ngx_http_brotli_filter_module.so";
load_module "%{nginx_moddir}/ngx_http_brotli_static_module.so";
EOF
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
