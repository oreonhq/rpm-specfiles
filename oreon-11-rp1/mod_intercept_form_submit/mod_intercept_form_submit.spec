# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 578ef277ef85b64c692a25f3f61d798d9f27b14ccb0961ae096d2e7252ff3966
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}

Summary: Apache module to intercept login form submission and run PAM authentication
Name: mod_intercept_form_submit
Version: 1.2.0
Release: 11%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://www.adelton.com/apache/mod_intercept_form_submit/
Source0: https://www.adelton.com/apache/mod_intercept_form_submit/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: httpd-devel
BuildRequires: pkgconfig
Requires: httpd-mmn = %{_httpd_mmn}
Requires: mod_authnz_pam >= 0.7

# Suppres auto-provides for module DSO per
# 
%{?filter_provides_in: %filter_provides_in %{_libdir}/httpd/modules/.*\.so$}
%{?filter_setup}

%description
mod_intercept_form_submit can intercept submission of application login
forms. It retrieves the login and password information from the POST
HTTP request, runs PAM authentication with those credentials, and sets
the REMOTE_USER environment variable if the authentication passes.

%prep
%oreon_verify_sources
%setup -q -n %{name}-%{version}

%build
%{_httpd_apxs} -c -Wc,"%{optflags} -Wall -pedantic -std=c99" mod_intercept_form_submit.c
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
echo > intercept_form_submit.confx
echo "# Load the module in %{_httpd_modconfdir}/55-intercept_form_submit.conf" >> intercept_form_submit.confx
cat intercept_form_submit.conf >> intercept_form_submit.confx
%else
cat intercept_form_submit.module > intercept_form_submit.confx
cat intercept_form_submit.conf >> intercept_form_submit.confx
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 755 .libs/mod_intercept_form_submit.so $RPM_BUILD_ROOT%{_httpd_moddir}/mod_intercept_form_submit.so

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
# httpd >= 2.4.x
install -Dp -m 0644 intercept_form_submit.module $RPM_BUILD_ROOT%{_httpd_modconfdir}/55-intercept_form_submit.conf
%endif
install -Dp -m 0644 intercept_form_submit.confx $RPM_BUILD_ROOT%{_httpd_confdir}/intercept_form_submit.conf

%files
%doc README LICENSE docs/*
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%config(noreplace) %{_httpd_modconfdir}/55-intercept_form_submit.conf
%endif
%config(noreplace) %{_httpd_confdir}/intercept_form_submit.conf
%{_httpd_moddir}/*.so

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-11
- Import
