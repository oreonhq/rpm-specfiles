%global source0_hash af3662023058e2cebebc14056f7e03e57d42017935b542fded7752931a720b64

%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_includedir}/httpd/.mmn || echo missinghttpddevel)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}

Name:           mod_auth_openid
Version:        0.8
Release:        27%{?dist}
Summary:        OpenID authentication for apache

License:        MIT
URL:            http://findingscience.com/mod_auth_openid/
Source0:        https://github.com/downloads/bmuller/mod_auth_openid/mod_auth_openid-0.8.tar.gz
Source1:        10-mod_auth_openid.conf

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  tidy-devel
BuildRequires:  libopkele-devel
BuildRequires:  sqlite-devel
BuildRequires:  pcre-devel
BuildRequires:  libcurl-devel
BuildRequires:  httpd-devel
BuildRequires:  autoconf
BuildRequires:  libtool
Requires:       httpd
Requires:       httpd-mmn = %{_httpd_mmn}

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
# The install target of the Makefile isn't used because that uses apxs
# which tries to enable the module in the build host httpd instead of in
# the build root.
mkdir -p %{buildroot}%{_httpd_confdir}
mkdir -p %{buildroot}%{_libdir}/httpd/modules
install -m 700 -d %{buildroot}%{_localstatedir}/lib/%{name}

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
# 2.4-style
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}/10-mod_auth_openid.conf
%else
# 2.2-style
install -d -m0755 %{buildroot}%{_httpd_confdir}
install -Dp -m644 %{SOURCE1} > %{buildroot}%{_httpd_confdir}/mod_auth_openid.conf
%endif
install -m 755 src/.libs/mod_auth_openid.so %{buildroot}%{_httpd_moddir}

%files
%doc AUTHORS COPYING README NEWS UPGRADE
%{_httpd_moddir}/mod_auth_openid.so

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%config(noreplace) %{_httpd_modconfdir}/*.conf
%else
%config(noreplace) %{_httpd_confdir}/*.conf
%endif

%attr(700,apache,root) %dir %{_localstatedir}/lib/%{name}

%changelog
%autochangelog
