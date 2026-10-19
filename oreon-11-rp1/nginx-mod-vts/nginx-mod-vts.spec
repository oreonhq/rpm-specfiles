%global source0_hash 0003bfa57da2106367fdc3f87760910c046e7df5545db73c880fc2b80350b14c
%global nginx_modname vts
%global origname nginx-module-%{nginx_modname}
Name:           nginx-mod-vts
Version:        0.2.7
Release:        1%{?dist}
Summary:        Nginx virtual host traffic status module
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/vozlt/nginx-module-vts
Source0:        https://github.com/vozlt/%{origname}/archive/v%{version}/%{origname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  nginx-mod-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
