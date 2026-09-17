%global source0_hash 4ddcb849b175a71c57bf4030dea0dc9556f0b58a74ea50d88f12e89195c61727

%global nginx_modname vts
%global origname nginx-module-%{nginx_modname}

Name:           nginx-mod-vts
Version:        0.2.4
Release:        6%{?dist}
Summary:        Nginx virtual host traffic status module

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/vozlt/nginx-module-vts
Source0:        %{url}/archive/v%{version}/%{origname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  nginx-mod-devel

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{origname}-%{version}

%build
%nginx_modconfigure
%nginx_modbuild

%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_vhost_traffic_status_module.so %{buildroot}%{nginx_moddir}
install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/ngx_http_vhost_traffic_status_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-vhost-traffic-status.conf
popd

%files
%license LICENSE
%doc README.md
%{nginx_moddir}/ngx_http_vhost_traffic_status_module.so
%{nginx_modconfdir}/mod-vhost-traffic-status.conf

%changelog
%autochangelog
