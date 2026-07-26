%global source0_hash b833b88b38a1f24eef96d8264dd2b2c1d3f868007d49cc58670ab477be1a5e7a

%global _hardened_build 1

# To build without checks:
# rpmbuild --without checks
# fedpkg local --without checks
# fedpkg mockbuild --without checks
%bcond check 0s

Name:           myproxy
Version:        6.2.20
Release:        2%{?dist}
Summary:        Manage X.509 Public Key Infrastructure (PKI) security credentials

License:        NCSA AND BSD-4-Clause AND BSD-2-Clause AND Apache-2.0
URL:            http://grid.ncsa.illinois.edu/myproxy/
Source:         https://repo.gridcf.org/gct6/sources/%{name}-%{version}.tar.gz
Source1:        myproxy-server-systemd-sysusers.conf
Source8:        README

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  globus-common-devel >= 15
BuildRequires:  globus-gssapi-gsi-devel >= 9
BuildRequires:  globus-gss-assist-devel >= 8
BuildRequires:  globus-gsi-sysconfig-devel >= 5
BuildRequires:  globus-gsi-cert-utils-devel >= 8
BuildRequires:  globus-gsi-proxy-core-devel >= 6
BuildRequires:  globus-gsi-credential-devel >= 5
BuildRequires:  globus-gsi-callback-devel >= 4
BuildRequires:  cyrus-sasl-devel
BuildRequires:  krb5-devel
BuildRequires:  openssl-devel
%if %{?fedora}%{!?fedora:0} >= 41
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  openldap-devel >= 2.3
BuildRequires:  pam-devel
BuildRequires:  perl-generators
BuildRequires:  voms-devel >= 1.9.12.1
BuildRequires:  systemd-rpm-macros
%if %{with checks}
BuildRequires:  globus-proxy-utils
BuildRequires:  globus-gsi-cert-utils-progs
BuildRequires:  openssl
BuildRequires:  perl-interpreter
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Socket)
BuildRequires:  voms-clients
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       %{name}-client = %{version}-%{release}

%description
MyProxy is open source software for managing X.509 Public Key Infrastructure
(PKI) security credentials (certificates and private keys). MyProxy
combines an online credential repository with an online certificate
authority to allow users to securely obtain credentials when and where needed.
Users run myproxy-logon to authenticate and obtain credentials, including
trusted CA certificates and Certificate Revocation Lists (CRLs).

%package libs
Summary:        Manage X.509 Public Key Infrastructure (PKI) security credentials
Requires:       globus-proxy-utils

%description libs
MyProxy is open source software for managing X.509 Public Key Infrastructure
(PKI) security credentials (certificates and private keys). MyProxy
combines an online credential repository with an online certificate
authority to allow users to securely obtain credentials when and where needed.
Users run myproxy-logon to authenticate and obtain credentials, including
trusted CA certificates and Certificate Revocation Lists (CRLs).

Package %{name}-libs contains runtime libs for MyProxy.

%package devel
Summary:        Develop X.509 Public Key Infrastructure (PKI) security credentials
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
MyProxy is open source software for managing X.509 Public Key Infrastructure
(PKI) security credentials (certificates and private keys). MyProxy
combines an online credential repository with an online certificate
authority to allow users to securely obtain credentials when and where needed.
Users run myproxy-logon to authenticate and obtain credentials, including
trusted CA certificates and Certificate Revocation Lists (CRLs).

Package %{name}-devel contains development files for MyProxy.

%package server
Summary:        Server for X.509 Public Key Infrastructure (PKI) security credentials
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%{?sysusers_requires_compat}
%{?systemd_requires}

%description server
MyProxy is open source software for managing X.509 Public Key Infrastructure
(PKI) security credentials (certificates and private keys). MyProxy
combines an online credential repository with an online certificate
authority to allow users to securely obtain credentials when and where needed.
Users run myproxy-logon to authenticate and obtain credentials, including
trusted CA certificates and Certificate Revocation Lists (CRLs).

Package %{name}-server contains the MyProxy server.

%package admin
# Create a separate admin clients package since they are not needed for normal
# operation and pull in a load of perl dependencies.
Summary:        Server for X.509 Public Key Infrastructure (PKI) security credentials
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-server = %{version}-%{release}
Requires:       globus-gsi-cert-utils-progs

%description admin
MyProxy is open source software for managing X.509 Public Key Infrastructure
(PKI) security credentials (certificates and private keys). MyProxy
combines an online credential repository with an online certificate
authority to allow users to securely obtain credentials when and where needed.
Users run myproxy-logon to authenticate and obtain credentials, including
trusted CA certificates and Certificate Revocation Lists (CRLs).

Package %{name}-admin contains the MyProxy server admin commands.

%package voms
Summary:        Manage X.509 Public Key Infrastructure (PKI) security credentials
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-libs < 6.1.6
Requires:       voms-clients

%description voms
MyProxy is open source software for managing X.509 Public Key Infrastructure
(PKI) security credentials (certificates and private keys). MyProxy
combines an online credential repository with an online certificate
authority to allow users to securely obtain credentials when and where needed.
Users run myproxy-logon to authenticate and obtain credentials, including
trusted CA certificates and Certificate Revocation Lists (CRLs).

Package %{name}-voms contains runtime libs for MyProxy to use VOMS.

%package doc
Summary:        Documentation for X.509 Public Key Infrastructure (PKI) security credentials
BuildArch:      noarch

%description doc
MyProxy is open source software for managing X.509 Public Key Infrastructure
(PKI) security credentials (certificates and private keys). MyProxy
combines an online credential repository with an online certificate
authority to allow users to securely obtain credentials when and where needed.
Users run myproxy-logon to authenticate and obtain credentials, including
trusted CA certificates and Certificate Revocation Lists (CRLs).

Package %{name}-doc contains the MyProxy documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%configure --disable-static \
           --includedir=%{_includedir}/globus \
           --with-openldap=%{_prefix} \
           --with-voms=%{_prefix} \
           --with-kerberos5=%{_prefix} \
           --with-sasl2=%{_prefix}

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Put documentation in Fedora default location
mkdir -p %{buildroot}%{_pkgdocdir}/extras
for FILE in login.html myproxy-accepted-credentials-mapapp \
            myproxy-cert-checker myproxy-certificate-mapapp \
            myproxy-certreq-checker myproxy-crl.cron myproxy.cron \
            myproxy-get-delegation.cgi myproxy-get-trustroots.cron \
            myproxy-passphrase-policy myproxy-revoke ; do
   mv %{buildroot}%{_datadir}/%{name}/$FILE %{buildroot}%{_pkgdocdir}/extras
done

mkdir -p %{buildroot}%{_pkgdocdir}
for FILE in PROTOCOL README.sasl REPOSITORY VERSION ; do
   mv %{buildroot}%{_datadir}/%{name}/$FILE %{buildroot}%{_pkgdocdir}
done

# Remove irrelevant example configuration files
for FILE in etc.inetd.conf.modifications etc.init.d.myproxy.nonroot \
            etc.services.modifications etc.xinetd.myproxy etc.init.d.myproxy \
            myproxy-server.service myproxy-server.conf LICENSE* ; do
   rm %{buildroot}%{_datadir}/%{name}/$FILE
done

# Move example configuration file into place
mkdir -p %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_datadir}/%{name}/myproxy-server.config \
   %{buildroot}%{_sysconfdir}

mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -p -m 644 systemd/myproxy-server.service %{buildroot}%{_unitdir}
install -p -m 644 systemd/myproxy-server.conf %{buildroot}%{_tmpfilesdir}

mkdir -p %{buildroot}%{_sysusersdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/myproxy-server.conf

mkdir -p %{buildroot}%{_localstatedir}/lib/myproxy

# Create a directory to hold myproxy owned host certificates
mkdir -p %{buildroot}%{_sysconfdir}/grid-security/myproxy

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove myproxy-server-setup rhbz#671561
rm %{buildroot}%{_sbindir}/myproxy-server-setup

%check
%if %{with checks}
%make_build check
%endif

%pre server
%sysusers_create_compat %{SOURCE1}

%post server
%tmpfiles_create myproxy-server.conf
%systemd_post myproxy-server.service

%preun server
%systemd_preun myproxy-server.service

%postun server
%systemd_postun_with_restart myproxy-server.service

%files
%{_bindir}/myproxy-change-pass-phrase
%{_bindir}/myproxy-destroy
%{_bindir}/myproxy-get-delegation
%{_bindir}/myproxy-get-trustroots
%{_bindir}/myproxy-info
%{_bindir}/myproxy-init
%{_bindir}/myproxy-logon
%{_bindir}/myproxy-retrieve
%{_bindir}/myproxy-store
%{_mandir}/man1/myproxy-change-pass-phrase.1*
%{_mandir}/man1/myproxy-destroy.1*
%{_mandir}/man1/myproxy-get-delegation.1*
%{_mandir}/man1/myproxy-get-trustroots.1*
%{_mandir}/man1/myproxy-info.1*
%{_mandir}/man1/myproxy-init.1*
%{_mandir}/man1/myproxy-logon.1*
%{_mandir}/man1/myproxy-retrieve.1*
%{_mandir}/man1/myproxy-store.1*

%files libs
%{_libdir}/libmyproxy.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/PROTOCOL
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/README.sasl
%doc %{_pkgdocdir}/REPOSITORY
%doc %{_pkgdocdir}/VERSION
%license LICENSE*

%files devel
%{_includedir}/globus/*
%{_libdir}/libmyproxy.so
%{_libdir}/pkgconfig/myproxy.pc

%files server
%{_sbindir}/myproxy-server
%{_unitdir}/myproxy-server.service
%{_tmpfilesdir}/myproxy-server.conf
%{_sysusersdir}/myproxy-server.conf
%config(noreplace) %{_sysconfdir}/myproxy-server.config
# myproxy-server wants exactly 700 permission on its data
# which is just fine.
%attr(0700,myproxy,myproxy) %dir %{_localstatedir}/lib/myproxy
%dir %{_sysconfdir}/grid-security/myproxy
%{_mandir}/man8/myproxy-server.8*
%{_mandir}/man5/myproxy-server.config.5*
%doc README.Fedora

%files admin
%{_sbindir}/myproxy-admin-addservice
%{_sbindir}/myproxy-admin-adduser
%{_sbindir}/myproxy-admin-change-pass
%{_sbindir}/myproxy-admin-load-credential
%{_sbindir}/myproxy-admin-query
%{_sbindir}/myproxy-replicate
%{_sbindir}/myproxy-test
%{_sbindir}/myproxy-test-replicate
%{_mandir}/man8/myproxy-admin-addservice.8*
%{_mandir}/man8/myproxy-admin-adduser.8*
%{_mandir}/man8/myproxy-admin-change-pass.8*
%{_mandir}/man8/myproxy-admin-load-credential.8*
%{_mandir}/man8/myproxy-admin-query.8*
%{_mandir}/man8/myproxy-replicate.8*

%files voms
%{_libdir}/libmyproxy_voms.so

%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/extras
%license LICENSE*

%changelog
%autochangelog
