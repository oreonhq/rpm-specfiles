%global source0_hash 25748224202586f6eedbdd8f8fc8f7d7647367e50fdadb780839efc65b2cb8b4

%global _hardened_build 1

Name:		voms
Version:	2.1.3
Release:	3%{?dist}
Summary:	Virtual Organization Membership Service

License:	Apache-2.0
URL:		https://italiangrid.github.io/voms/
Source0:	https://github.com/italiangrid/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
#		Post-install setup instructions:
Source1:	%{name}.INSTALL
#		System user creation config
Source2:	%{name}-sysusers.conf

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	openssl-devel
BuildRequires:	expat-devel
BuildRequires:	gsoap-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	libxslt
BuildRequires:	docbook-style-xsl
BuildRequires:	doxygen
BuildRequires:	systemd-rpm-macros

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides libraries that applications using the VOMS functionality
will bind to.

%package devel
Summary:	Virtual Organization Membership Service Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	openssl-devel%{?_isa}

%description devel
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides header files for programming with the VOMS libraries.

%package doc
Summary:	Virtual Organization Membership Service Documentation
BuildArch:	noarch

%description doc
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides documentation for the Virtual Organization Membership
Service.

%package clients-cpp
Summary:	Virtual Organization Membership Service Clients
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	voms-clients = %{version}-%{release}
Obsoletes:	voms-clients < 2.0.12-3

Requires(post):		%{_sbindir}/update-alternatives
Requires(preun):	%{_sbindir}/update-alternatives

%description clients-cpp
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides command line applications to access the VOMS
services.

%package server
Summary:	Virtual Organization Membership Service Server
Requires:	%{name}%{?_isa} = %{version}-%{release}
%{?sysusers_requires_compat}
%{?systemd_requires}

%description server
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides the VOMS service.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

./autogen.sh

install -m 644 -p %{SOURCE1} README.Fedora

%build
%configure --disable-static --enable-docs --disable-parser-gen

%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/*.la

mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p systemd/%{name}@.service %{buildroot}%{_unitdir}
rm %{buildroot}%{_initrddir}/%{name}
rm %{buildroot}%{_sysconfdir}/sysconfig/%{name}

mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 -p %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}.conf

mkdir -p %{buildroot}%{_pkgdocdir}/VOMS_C_API
cp -pr doc/apidoc/api/VOMS_C_API/html %{buildroot}%{_pkgdocdir}/VOMS_C_API
rm -f %{buildroot}%{_pkgdocdir}/VOMS_C_API/html/installdox

mkdir -p %{buildroot}%{_pkgdocdir}/VOMS_CC_API
cp -pr doc/apidoc/api/VOMS_CC_API/html %{buildroot}%{_pkgdocdir}/VOMS_CC_API
rm -f %{buildroot}%{_pkgdocdir}/VOMS_CC_API/html/installdox

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for b in voms-proxy-init voms-proxy-info voms-proxy-destroy; do
  ## Rename client binaries
  mv %{buildroot}%{_bindir}/${b} %{buildroot}%{_bindir}/${b}2
  ln -s %{_bindir}/${b}2 %{buildroot}%{_sysconfdir}/alternatives/${b}
  ln -s %{_sysconfdir}/alternatives/${b} %{buildroot}%{_bindir}/${b}
  ## and man pages
  mv %{buildroot}%{_mandir}/man1/${b}.1 %{buildroot}%{_mandir}/man1/${b}2.1
  ln -s %{_mandir}/man1/${b}2.1.gz %{buildroot}%{_sysconfdir}/alternatives/${b}.1.gz
  ln -s %{_sysconfdir}/alternatives/${b}.1.gz %{buildroot}%{_mandir}/man1/${b}.1.gz
done

%posttrans
# Recover /etc/vomses...
if [ -r %{_sysconfdir}/vomses.rpmsave -a ! -r %{_sysconfdir}/vomses ] ; then
   mv %{_sysconfdir}/vomses.rpmsave %{_sysconfdir}/vomses
fi

%pre server
%sysusers_create_compat %{SOURCE2}

%post server
if [ $1 -eq 1 ] ; then
    systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun server
if [ $1 -eq 0 ] ; then
    for INSTANCE in `systemctl | grep %{name}@ | awk '{print $1;}'`; do
	systemctl --no-reload disable $INSTANCE > /dev/null 2>&1 || :
	systemctl stop $INSTANCE > /dev/null 2>&1 || :
    done
fi

%postun server
if [ $1 -ge 1 ] ; then
    systemctl daemon-reload >/dev/null 2>&1 || :
    for INSTANCE in `systemctl | grep %{name}@ | awk '{print $1;}'`; do
	systemctl try-restart $INSTANCE >/dev/null 2>&1 || :
    done
fi

%pre clients-cpp
if [ $1 -gt 1 ]; then
  for c in voms-proxy-init voms-proxy-info voms-proxy-destroy; do
    if [ -r %{_bindir}/$c -a ! -h %{_bindir}/$c ]; then
      rm -f %{_bindir}/$c
    fi
    if [ -r %{_mandir}/man1/$c.1.gz -a ! -h %{_mandir}/man1/$c.1.gz ]; then
      rm -f %{_mandir}/man1/$c.1.gz
    fi
  done
fi

%post clients-cpp
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-init \
    voms-proxy-init %{_bindir}/voms-proxy-init2 50 \
    --slave %{_mandir}/man1/voms-proxy-init.1.gz voms-proxy-init-man \
    %{_mandir}/man1/voms-proxy-init2.1.gz
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-info \
    voms-proxy-info %{_bindir}/voms-proxy-info2 50 \
    --slave %{_mandir}/man1/voms-proxy-info.1.gz voms-proxy-info-man \
    %{_mandir}/man1/voms-proxy-info2.1.gz
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-destroy \
    voms-proxy-destroy %{_bindir}/voms-proxy-destroy2 50 \
    --slave %{_mandir}/man1/voms-proxy-destroy.1.gz voms-proxy-destroy-man \
    %{_mandir}/man1/voms-proxy-destroy2.1.gz

%preun clients-cpp
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove voms-proxy-init \
    %{_bindir}/voms-proxy-init2
    %{_sbindir}/update-alternatives --remove voms-proxy-info \
    %{_bindir}/voms-proxy-info2
    %{_sbindir}/update-alternatives --remove voms-proxy-destroy \
    %{_bindir}/voms-proxy-destroy2
fi

%triggerpostun clients-cpp -- voms-clients
# Uninstalling the old voms-clients package will remove the alternatives
# for voms-clients-cpp - put them back in this triggerpostun script
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-init \
    voms-proxy-init %{_bindir}/voms-proxy-init2 50 \
    --slave %{_mandir}/man1/voms-proxy-init.1.gz voms-proxy-init-man \
    %{_mandir}/man1/voms-proxy-init2.1.gz
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-info \
    voms-proxy-info %{_bindir}/voms-proxy-info2 50 \
    --slave %{_mandir}/man1/voms-proxy-info.1.gz voms-proxy-info-man \
    %{_mandir}/man1/voms-proxy-info2.1.gz
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-destroy \
    voms-proxy-destroy %{_bindir}/voms-proxy-destroy2 50 \
    --slave %{_mandir}/man1/voms-proxy-destroy.1.gz voms-proxy-destroy-man \
    %{_mandir}/man1/voms-proxy-destroy2.1.gz

%files
%{_libdir}/libvomsapi.so.1*
%dir %{_sysconfdir}/grid-security
%dir %{_sysconfdir}/grid-security/vomsdir
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/vomses.template
%doc AUTHORS
%doc README.md
%license LICENSE

%files devel
%{_libdir}/libvomsapi.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}-2.0.pc
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man3/*

%files doc
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/VOMS_C_API
%doc %{_pkgdocdir}/VOMS_CC_API
%doc AUTHORS
%license LICENSE

%files clients-cpp
%{_bindir}/voms-proxy-destroy2
%{_bindir}/voms-proxy-info2
%{_bindir}/voms-proxy-init2
%{_bindir}/voms-proxy-fake
%{_bindir}/voms-proxy-list
%{_bindir}/voms-verify
%ghost %{_bindir}/voms-proxy-destroy
%ghost %{_bindir}/voms-proxy-info
%ghost %{_bindir}/voms-proxy-init
%ghost %{_sysconfdir}/alternatives/voms-proxy-destroy
%ghost %{_sysconfdir}/alternatives/voms-proxy-info
%ghost %{_sysconfdir}/alternatives/voms-proxy-init
%{_mandir}/man1/voms-proxy-destroy2.1*
%{_mandir}/man1/voms-proxy-info2.1*
%{_mandir}/man1/voms-proxy-init2.1*
%{_mandir}/man1/voms-proxy-fake.1*
%{_mandir}/man1/voms-proxy-list.1*
%ghost %{_mandir}/man1/voms-proxy-destroy.1*
%ghost %{_mandir}/man1/voms-proxy-info.1*
%ghost %{_mandir}/man1/voms-proxy-init.1*
%ghost %{_sysconfdir}/alternatives/voms-proxy-destroy.1*
%ghost %{_sysconfdir}/alternatives/voms-proxy-info.1*
%ghost %{_sysconfdir}/alternatives/voms-proxy-init.1*

%files server
%{_sbindir}/%{name}
%{_unitdir}/%{name}@.service
%attr(-,voms,voms) %dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/grid-security/%{name}
%attr(-,voms,voms) %dir %{_localstatedir}/log/%{name}
%{_datadir}/%{name}/mysql2oracle
%{_datadir}/%{name}/upgrade1to2
%{_datadir}/%{name}/voms.data
%{_datadir}/%{name}/voms_install_db
%{_datadir}/%{name}/voms-ping
%{_datadir}/%{name}/voms_replica_master_setup.sh
%{_datadir}/%{name}/voms_replica_slave_setup.sh
%{_mandir}/man8/voms.8*
%{_sysusersdir}/%{name}.conf
%doc README.Fedora

%changelog
%autochangelog
