%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}

Summary: Apache module to retrieve additional information about the authenticated user
Name: mod_lookup_identity
Version: 1.0.0
Release: 25%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: http://www.adelton.com/apache/mod_lookup_identity/
Source0: http://www.adelton.com/apache/mod_lookup_identity/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: httpd-devel
BuildRequires: dbus-devel
BuildRequires: pkgconfig
Requires: httpd-mmn = %{_httpd_mmn}
%if 0%{?fedora} || 0%{?rhel} >= 8 || 0%{?oreon}
Recommends: sssd-dbus
%endif

# Suppres auto-provides for module DSO per
# 
%{?filter_provides_in: %filter_provides_in %{_libdir}/httpd/modules/.*\.so$}
%{?filter_setup}

%description
mod_lookup_identity can retrieve additional pieces of information
about user authenticated in Apache httpd server and store these values
in notes/environment variables to be consumed by web applications.
Use of REMOTE_USER_* environment variables is recommended.

%prep
%setup -q -n %{name}-%{version}

%build
%{_httpd_apxs} -c -Wc,"%{optflags} -Wall -pedantic -std=c99 $(pkg-config --cflags dbus-1)" $(pkg-config --libs dbus-1) mod_lookup_identity.c
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
echo > lookup_identity.confx
echo "# Load the module in %{_httpd_modconfdir}/55-lookup_identity.conf" >> lookup_identity.confx
cat lookup_identity.conf >> lookup_identity.confx
%else
cat lookup_identity.module > lookup_identity.confx
cat lookup_identity.conf >> lookup_identity.confx
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 755 .libs/mod_lookup_identity.so $RPM_BUILD_ROOT%{_httpd_moddir}/mod_lookup_identity.so

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
# httpd >= 2.4.x
install -Dp -m 0644 lookup_identity.module $RPM_BUILD_ROOT%{_httpd_modconfdir}/55-lookup_identity.conf
%endif
install -Dp -m 0644 lookup_identity.confx $RPM_BUILD_ROOT%{_httpd_confdir}/lookup_identity.conf

%files
%doc README LICENSE
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%config(noreplace) %{_httpd_modconfdir}/55-lookup_identity.conf
%endif
%config(noreplace) %{_httpd_confdir}/lookup_identity.conf
%{_httpd_moddir}/*.so

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-25
- Import
