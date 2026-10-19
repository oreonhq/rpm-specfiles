%global source0_hash 7aadc253a41a39de03f6855ac5c75ee16249403ff1dd4b7531915d6bb7adb72e
%global snapdate 20241211
%global commit 47dd9c5432da760e3b780a50ae339ae385b16b7c
%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
%global snaprel %%{?snapdate:.git%%{snapdate}.%%{shortcommit}}
%global baserelease 0.2
Name:       ipsilon
Version:    3.1.1
Release:        1%{?dist}
Summary:        An Identity Provider Server
License:    GPL-3.0-or-later
URL:        https://pagure.io/ipsilon
%if %{defined snaprel}
Source0:        https://pagure.io/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
%endif
BuildArch:  noarch
Requires:       python3-setuptools
Requires:       python3-requests
Requires:       python3-filetype
Requires:       %{name}-base = %{version}-%{release}
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-lasso
BuildRequires:  python3-openid
BuildRequires:  python3-openid-cla
BuildRequires:  python3-openid-teams
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Ipsilon is a multi-protocol Identity Provider service. Its function is to
bridge authentication providers and applications to achieve Single Sign On
and Federation.

%package base
Summary:        Ipsilon base IDP server
License:        GPL-3.0-or-later
Requires:       httpd
Requires:       mod_ssl
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       %{name}-provider = %{version}-%{release}
Requires:       python3-mod_wsgi
Requires:       python3-cherrypy
Requires:       python3-jinja2
Requires:       python3-lxml
Requires:       python3-sqlalchemy
Requires:       open-sans-fonts
Requires:       font(fontawesome)
Requires:       pam
%description base
The Ipsilon IdP server without installer

%package filesystem
Summary:        Package providing files required by Ipsilon
License:        GPL-3.0-or-later
%description filesystem
Package providing basic directory structure required
for all Ipsilon parts

%package client
Summary:        Tools for configuring Ipsilon clients
License:        GPL-3.0-or-later
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       %{name}-saml2-base = %{version}-%{release}
Requires:       mod_auth_mellon
Requires:       mod_auth_openidc
Requires:       mod_ssl
Requires:       python3-requests
BuildArch:      noarch
%description client
Client install tools

%package tools-ipa
summary:        IPA helpers
License:        GPL-3.0-or-later
Requires:       %{name}-authgssapi = %{version}-%{release}
Requires:       %{name}-authform = %{version}-%{release}
Requires:       %{name}-infosssd = %{version}-%{release}
Requires:       freeipa-client
Requires:       freeipa-admintools
BuildArch:      noarch
%description tools-ipa
Convenience client install tools for IPA support in the Ipsilon identity Provider

%package saml2-base
Summary:        SAML2 base
License:        GPL-3.0-or-later
Requires:       openssl
Requires:       python3-lasso
Requires:       python3-lxml
BuildArch:      noarch
%description saml2-base
Provides core SAML2 utilities

%package saml2
Summary:        SAML2 provider plugin
License:        GPL-3.0-or-later
Provides:       ipsilon-provider = %{version}-%{release}
Requires:       %{name}-base = %{version}-%{release}
Requires:       %{name}-saml2-base = %{version}-%{release}
BuildArch:      noarch
%description saml2
Provides a SAML2 provider plugin for the Ipsilon identity Provider

%package openid
Summary:        Openid provider plugin
License:        GPL-3.0-or-later
Provides:       ipsilon-provider = %{version}-%{release}
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-openid
Requires:       python3-openid-cla
Requires:       python3-openid-teams
BuildArch:      noarch
%description openid
Provides an OpenId provider plugin for the Ipsilon identity Provider

%package openidc
Summary:        OpenID Connect provider plugin
License:        GPL-3.0-or-later
Provides:       ipsilon-provider = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       python3-jwcrypto
BuildArch:      noarch
%description openidc
Provides an OpenID Connect and OAuth2 provider plugin for the Ipsilon
identity Provider

%package authform
Summary:        mod_intercept_form_submit login plugin
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       mod_intercept_form_submit
BuildArch:      noarch
%description authform
Provides a login plugin to authenticate with mod_intercept_form_submit

%package authpam
Summary:        PAM based login plugin
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-pam
BuildArch:      noarch
%description authpam
Provides a login plugin to authenticate against the local PAM stack

%package authgssapi
Summary:        mod_auth_gssapi based login plugin
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       mod_auth_gssapi
BuildArch:      noarch
%description authgssapi
Provides a login plugin to allow authentication via the mod_auth_gssapi
Apache module.

%package authldap
Summary:        LDAP info and login plugin
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-ldap
BuildArch:      noarch
%description authldap
Provides a login plugin to allow authentication and info retrieval via LDAP.

%package infofas
Summary:        Fedora Authentication System login plugin
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       %{name}-infosssd = %{version}-%{release}
BuildArch:      noarch
%description infofas
Provides an info plugin to retrieve info from the Fedora Authentication System

%package infosssd
Summary:        SSSD based identity plugin
License:        GPL-3.0-or-later
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-sssdconfig
Requires:       sssd >= 1.12.4
BuildArch:      noarch
%description infosssd
Provides an info plugin to allow retrieval via SSSD.

%package theme-Fedora
Summary:        Fedora Account System theme
Requires:       %{name}-base = %{version}-%{release}
BuildArch:      noarch
%description theme-Fedora
Provides a theme for Ipsilon used for the Fedora Account System.

%package theme-openSUSE
Summary:        openSUSE Accounts theme
Requires:       %{name}-base = %{version}-%{release}
BuildArch:      noarch
%description theme-openSUSE
Provides a theme for Ipsilon used for openSUSE Accounts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{defined snaprel}
%autosetup -n %{name}-%{commit} -p1
%else
%autosetup -p1
%endif

# Create a sysusers.d config file
cat >ipsilon.sysusers.conf <<EOF
u ipsilon - 'Ipsilon Server' %{_sharedstatedir}/ipsilon -
EOF

%build

%py3_build
%install
%py3_install
mkdir -p %{buildroot}%{_libexecdir}/ipsilon
mkdir -p %{buildroot}%{_defaultdocdir}
mkdir -p %{buildroot}%{_localstatedir}/cache/ipsilon
install -d -m 0700 %{buildroot}%{_sharedstatedir}/ipsilon
install -d -m 0700 %{buildroot}%{_sysconfdir}/ipsilon
mv %{buildroot}/%{_bindir}/ipsilon %{buildroot}/%{_libexecdir}/ipsilon/ipsilon
mv %{buildroot}%{_defaultdocdir}/%{name} %{buildroot}%{_defaultdocdir}/%{name}-%{version}
rm -fr %{buildroot}%{python3_sitelib}/tests
ln -s %{_datadir}/fonts %{buildroot}%{_datadir}/ipsilon/ui/fonts
mkdir -p  %{buildroot}%{_sysconfdir}/pam.d
cp %{buildroot}%{_datadir}/ipsilon/templates/install/pam/ipsilon.pamd %{buildroot}%{_sysconfdir}/pam.d/ipsilon
install -m0644 -D ipsilon.sysusers.conf %{buildroot}%{_sysusersdir}/ipsilon.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ipsilon-base -f %{oreon_filedir}/ipsilon-base.list
%files -n ipsilon-filesystem -f %{oreon_filedir}/ipsilon-filesystem.list
%files -n ipsilon-client -f %{oreon_filedir}/ipsilon-client.list
%files -n ipsilon-tools-ipa -f %{oreon_filedir}/ipsilon-tools-ipa.list
%files -n ipsilon-saml2-base -f %{oreon_filedir}/ipsilon-saml2-base.list
%files -n ipsilon-saml2 -f %{oreon_filedir}/ipsilon-saml2.list
%files -n ipsilon-openid -f %{oreon_filedir}/ipsilon-openid.list
%files -n ipsilon-openidc -f %{oreon_filedir}/ipsilon-openidc.list
%files -n ipsilon-authform -f %{oreon_filedir}/ipsilon-authform.list
%files -n ipsilon-authpam -f %{oreon_filedir}/ipsilon-authpam.list
%files -n ipsilon-authgssapi -f %{oreon_filedir}/ipsilon-authgssapi.list
%files -n ipsilon-authldap -f %{oreon_filedir}/ipsilon-authldap.list
%files -n ipsilon-infofas -f %{oreon_filedir}/ipsilon-infofas.list
%files -n ipsilon-infosssd -f %{oreon_filedir}/ipsilon-infosssd.list
%files -n ipsilon-theme-Fedora -f %{oreon_filedir}/ipsilon-theme-Fedora.list
%files -n ipsilon-theme-openSUSE -f %{oreon_filedir}/ipsilon-theme-openSUSE.list

%changelog

%autochangelog
