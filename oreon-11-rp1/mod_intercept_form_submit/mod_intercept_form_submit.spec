%global source0_hash 578ef277ef85b64c692a25f3f61d798d9f27b14ccb0961ae096d2e7252ff3966
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn 0-0}}
%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}
Summary:        Apache module to intercept login form submission and run PAM authentication
Name: mod_intercept_form_submit
Version: 1.2.0
Release:        1%{?dist}
License: Apache-2.0
URL: https://www.adelton.com/apache/mod_intercept_form_submit/
Source0:        https://www.adelton.com/apache/mod_intercept_form_submit/%{name}-%{version}.tar.gz
Requires: httpd-mmn
Requires: mod_authnz_pam >= 0.7
%{?filter_provides_in: %filter_provides_in %{_libdir}/httpd/modules/.*\.so$}
%{?filter_setup}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  pkgconfig
# /oreon:deps
%description
mod_intercept_form_submit can intercept submission of application login
forms. It retrieves the login and password information from the POST
HTTP request, runs PAM authentication with those credentials, and sets
the REMOTE_USER environment variable if the authentication passes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
install -Dp -m 0644 intercept_form_submit.module $RPM_BUILD_ROOT%{_httpd_modconfdir}/55-intercept_form_submit.conf
%endif
install -Dp -m 0644 intercept_form_submit.confx $RPM_BUILD_ROOT%{_httpd_confdir}/intercept_form_submit.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-11
- Import
