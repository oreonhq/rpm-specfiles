%global source0_hash 21795bdcc6d671368871c9202ae64c729efca8a0055a7482a26a06f2e7131eff

%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}

%global modsuffix authnz_external
%global conffile %{modsuffix}.conf
%global conffile2 10-%{modsuffix}.conf

Summary: An Apache module used for authentication
Name: mod_%{modsuffix}
Version: 3.3.3
Release: 14%{?dist}
License: Apache-1.0
URL: https://github.com/phokz/mod-auth-external/
Source: https://github.com/phokz/mod-auth-external/archive/%{name}-%{version}.tar.gz
Source1: %{conffile}
Source2: %{conffile2}
Requires: pwauth, httpd-mmn = %{_httpd_mmn}
BuildRequires: gcc
BuildRequires: httpd-devel

%description
Mod_Auth_External can be used to quickly construct secure, reliable
authentication systems.  It can also be misused to quickly open gaping
holes in your security.  Read the documentation, and use with extreme
caution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mod-auth-external-%{name}-%{version}

%build
%{_httpd_apxs} -c -I . %{name}.c

%install
mkdir -p %{buildroot}%{_httpd_moddir} %{buildroot}%{_httpd_confdir} \
         %{buildroot}%{_httpd_modconfdir}
apxs -i -S LIBEXECDIR=%{buildroot}%{_httpd_moddir} -n %{name} %{name}.la
install -p -m 644 -t %{buildroot}%{_httpd_confdir}/ %{SOURCE1}
install -p -m 644 -t %{buildroot}%{_httpd_modconfdir}/ %{SOURCE2}

%files
%{_httpd_moddir}/%{name}.so
%config(noreplace) %lang(en) %{_httpd_confdir}/%{conffile}
%config(noreplace) %lang(en) %{_httpd_modconfdir}/%{conffile2}
%doc AUTHENTICATORS CHANGES README TODO UPGRADE

%changelog
%autochangelog
