%global source0_hash 338e1cc1ceb8e0bdb2cb113936966b89ef2f24557502c61fe14e535fae14f7cd
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}
%{!?_httpd_moddir: %{expand: %%global _httpd_moddir %%{_libdir}/httpd/modules}}
%{!?_httpd_confdir: %{expand: %%global _httpd_confdir %{_sysconfdir}/httpd/conf.d}}
%{!?_with_hiredis: %{!?_without_hiredis: %global _without_hiredis --without-hiredis}}
%{?_with_hiredis: %{?_without_hiredis: %{error: both _with_hiredis and _without_hiredis}}}
%{!?_with_hiredis: %{!?_without_hiredis: %{error: neither _with_hiredis nor _without_hiredis}}}
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%global httpd_pkg_cache_dir /var/cache/httpd/mod_auth_openidc
Name:		mod_auth_openidc
Version:	2.4.20.3
Release:        1%{?dist}
Summary:        OpenID Connect auth module for Apache HTTP Server
License:	Apache-2.0
URL:		https://github.com/OpenIDC/mod_auth_openidc
Source0:        https://github.com/OpenIDC/mod_auth_openidc/releases/download/v%{version}/mod_auth_openidc-%{version}.tar.gz
%{?_with_hiredis:BuildRequires: hiredis-devel}
Requires:	httpd-mmn
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cjose-devel
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  jansson-devel
BuildRequires:  jq-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
# /oreon:deps
%description
This module enables an Apache 2.x web server to operate as
an OpenID Connect Relying Party and/or OAuth 2.0 Resource Server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

export MODULES_DIR=%{_httpd_moddir}
export APXS2_OPTS='-S LIBEXECDIR=${MODULES_DIR}'
autoreconf -vfi
%configure \
  --with-jq=/usr/lib64/ \
  %{?_with_hiredis} \
  %{?_without_hiredis} \
  --with-apxs2=%{_httpd_apxs}
%{make_build}
%check

export MODULES_DIR=%{_httpd_moddir}
export APXS2_OPTS='-S LIBEXECDIR=${MODULES_DIR}'
%{make_build} test
%install
mkdir -p $RPM_BUILD_ROOT%{_httpd_moddir}
make install DESTDIR=$RPM_BUILD_ROOT MODULES_DIR=$RPM_BUILD_ROOT%{_httpd_moddir}
install -m 755 -d $RPM_BUILD_ROOT%{_httpd_modconfdir}
echo 'LoadModule auth_openidc_module modules/mod_auth_openidc.so' > \
	$RPM_BUILD_ROOT%{_httpd_modconfdir}/10-auth_openidc.conf
install -m 755 -d $RPM_BUILD_ROOT%{_httpd_confdir}
install -m 644 auth_openidc.conf $RPM_BUILD_ROOT%{_httpd_confdir}
sed -i 's!/var/cache/apache2/!/var/cache/httpd/!' $RPM_BUILD_ROOT%{_httpd_confdir}/auth_openidc.conf
install -m 700 -d $RPM_BUILD_ROOT%{httpd_pkg_cache_dir}
install -m 700 -d $RPM_BUILD_ROOT%{httpd_pkg_cache_dir}/metadata
install -m 700 -d $RPM_BUILD_ROOT%{httpd_pkg_cache_dir}/cache
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
