%global source0_hash 8f19ca024cc7f5729737a3c731d4d37cd3b24047a19a11e31dd115c360120937
%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:     %{expand: %%global _httpd_moddir %%{_libdir}/httpd/modules}}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:          mod_cluster
Version:       2.1.0.Final
Release:        1%{?dist}
Summary:        Apache HTTP Server dynamic load balancer with Wildfly and Tomcat libraries
License:       LGPL-3.0-only
URL:           http://modcluster.io/
Source0:        https://github.com/modcluster/%{name}/archive/%{version}%{namedreltag}/%{name}-%{version}%{namedreltag}.tar.gz
Source1:       mod_cluster.conf
Source2:       README.fedora
Requires:      httpd >= 2.4.49
Requires:      httpd-mmn = %{_httpd_mmn}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  make
# /oreon:deps
%description
Mod_cluster is an httpd-based load balancer. Like mod_jk and mod_proxy,
mod_cluster uses a communication channel to forward requests from httpd to one
of a set of application server nodes. Unlike mod_jk and mod_proxy, mod_cluster
leverages an additional connection between the application server nodes and
httpd. The application server nodes use this connection to transmit server-side
load balance factors and lifecycle events back to httpd via a custom set of
HTTP methods, affectionately called the Mod-Cluster Management Protocol (MCMP).
This additional feedback channel allows mod_cluster to offer a level of
intelligence and granularity not found in other load balancing solutions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mod_cluster-%{namedversion}

%build

CFLAGS="$RPM_OPT_FLAGS"
export CFLAGS
module_dirs=( advertise mod_manager mod_proxy_cluster mod_cluster_slotmem )
for dir in ${module_dirs[@]} ; do
    pushd native/${dir}
        sh buildconf
        %configure --libdir=%{_libdir} --with-apxs=%{_httpd_apxs}
        make %{?_smp_mflags}
    popd
done
%install
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/httpd/modules
install -d -m 755 $RPM_BUILD_ROOT%{_httpd_confdir}
module_dirs=( advertise mod_manager mod_proxy_cluster mod_cluster_slotmem )
for dir in ${module_dirs[@]} ; do
    pushd native/${dir}
        cp ./*.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules
    popd
done
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_confdir}/
install -pm 0644 %{SOURCE2} README
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
