%global source0_hash e5b9f1f3389bd087c8a7a9866d7035cc677698ddbf9e4f79f4bdbb56ae37d0d1

%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}

Summary: PAM authorization checker and PAM Basic Authentication provider
Name: mod_authnz_pam
Version: 1.2.3
Release: 12%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://www.adelton.com/apache/mod_authnz_pam/
Source0: https://www.adelton.com/apache/mod_authnz_pam/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: httpd-devel
BuildRequires: pam-devel
BuildRequires: pkgconfig
Requires: httpd-mmn = %{_httpd_mmn}
Requires: pam

# Suppres auto-provides for module DSO per
# 
%{?filter_provides_in: %filter_provides_in %{_libdir}/httpd/modules/.*\.so$}
%{?filter_setup}

%description
mod_authnz_pam is a PAM authorization module, supplementing
authentication done by other modules, for example mod_auth_kerb; it
can also be used as full Basic Authentication provider which runs the
[login, password] authentication through the PAM stack.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}

%build
%{_httpd_apxs} -c -Wc,"%{optflags} -Wall -pedantic -std=c99" -lpam mod_authnz_pam.c
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
echo > authnz_pam.confx
echo "# Load the module in %{_httpd_modconfdir}/55-authnz_pam.conf" >> authnz_pam.confx
cat authnz_pam.conf >> authnz_pam.confx
%else
cat authnz_pam.module > authnz_pam.confx
cat authnz_pam.conf >> authnz_pam.confx
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 755 .libs/mod_authnz_pam.so $RPM_BUILD_ROOT%{_httpd_moddir}/mod_authnz_pam.so

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
# httpd >= 2.4.x
install -Dp -m 0644 authnz_pam.module $RPM_BUILD_ROOT%{_httpd_modconfdir}/55-authnz_pam.conf
%endif
install -Dp -m 0644 authnz_pam.confx $RPM_BUILD_ROOT%{_httpd_confdir}/authnz_pam.conf

%files
%doc README LICENSE
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%config(noreplace) %{_httpd_modconfdir}/55-authnz_pam.conf
%endif
%config(noreplace) %{_httpd_confdir}/authnz_pam.conf
%{_httpd_moddir}/*.so

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.3-12
- Import
