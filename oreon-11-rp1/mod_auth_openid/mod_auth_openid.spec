%global source0_hash af3662023058e2cebebc14056f7e03e57d42017935b542fded7752931a720b64
%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_includedir}/httpd/.mmn || echo missinghttpddevel)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}
Name:           mod_auth_openid
Version:        0.8
Release:        1%{?dist}
Summary:        OpenID authentication for apache
License:        MIT
URL:            http://findingscience.com/mod_auth_openid/
Source0:        https://github.com/downloads/bmuller/mod_auth_openid/mod_auth_openid-0.8.tar.gz
Source1:        10-mod_auth_openid.conf
Requires:       httpd
Requires:       httpd-mmn = %{_httpd_mmn}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  httpd-devel
BuildRequires:  libcurl-devel
BuildRequires:  libopkele-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pcre-devel
BuildRequires:  sqlite-devel
BuildRequires:  tidy-devel
# /oreon:deps
%description
mod_auth_openid is an authentication module for the Apache 2 webserver.
OpenID 2.0 relying party for apache webserver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

./autogen.sh
%configure --with-apxs=%{_httpd_apxs}
make %{?_smp_mflags}
%install
mkdir -p %{buildroot}%{_httpd_confdir}
mkdir -p %{buildroot}%{_libdir}/httpd/modules
install -m 700 -d %{buildroot}%{_localstatedir}/lib/%{name}
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}/10-mod_auth_openid.conf
%else
install -d -m0755 %{buildroot}%{_httpd_confdir}
install -Dp -m644 %{SOURCE1} > %{buildroot}%{_httpd_confdir}/mod_auth_openid.conf
%endif
install -m 755 src/.libs/mod_auth_openid.so %{buildroot}%{_httpd_moddir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
