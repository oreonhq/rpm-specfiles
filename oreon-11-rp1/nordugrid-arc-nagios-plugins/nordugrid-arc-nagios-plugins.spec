%global source0_hash 2edac4af0560d9e55be9f4eec253f0f706c2613afb419b3544dcaa00daf7a3d2

# Disable debuginfo since there are no binaries
%global debug_package %{nil}

%global enable_doc 1

%global nagios_bindir %{_libdir}/nagios/plugins
%global arc_spooldir %{_localstatedir}/spool/arc
%global pkg_spooldir %{arc_spooldir}/nagios
%global pkg_sysconfdir %{_sysconfdir}/arc/nagios

Name:		nordugrid-arc-nagios-plugins
Version:	3.2.3
Release:	3%{?dist}
Summary:	Nagios plugins for ARC

License:	Apache-2.0
URL:		https://www.nordugrid.org
Source0:	https://download.nordugrid.org/packages/%{name}/releases/%{version}/src/%{name}-%{version}.tar.gz

Requires:	nordugrid-arc-client
Requires:	(nordugrid-arc-plugins-arcrest >= 6.5.0 or nordugrid-arc-plugins-needed >= 7.0.0)
Requires:	nagios-common

%if %{?rhel}%{!?rhel:0} == 8
Requires:	python38-cryptography
Requires:	python38-jinja2
Requires:	python38-ldap
BuildRequires:	python38-devel
BuildRequires:	python38-setuptools
%else
Requires:	python3-cryptography
Requires:	python3-jinja2
Requires:	python3-ldap
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif

%if %{enable_doc}
BuildRequires:	make
BuildRequires:	/usr/bin/sphinx-build
%endif

%description
This package provides the Nagios plugins for testing ARC computing elements.

%if %{enable_doc}
%package doc
Summary:	HTML documentation for the ARC Nagios plugins
BuildArch:	noarch

%description doc
This package provides HTML documentation for the ARC Nagios plugins.
%endif

%package egi
Summary:	EGI configuration and dependencies for the ARC Nagios plugins
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
Requires:	nordugrid-arc-plugins-gridftp >= 6.5.0

%description egi
This package provides EGI configuration and dependencies for the ARC Nagios
plugins.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%py3_build
%if %{enable_doc}
make -C doc html
rm -f doc/_build/html/.buildinfo
%endif

%install
%py3_install

install -m755 -d %{buildroot}%{pkg_spooldir}

%files
%dir %{pkg_sysconfdir}
%dir %{pkg_sysconfdir}/20-dist.d
%config(noreplace) %{pkg_sysconfdir}/20-dist.ini
%config(noreplace) %{pkg_sysconfdir}/20-dist.d/default.xrsl.j2
%{nagios_bindir}/check_arcce_clean
%{nagios_bindir}/check_arcce_monitor
%{nagios_bindir}/check_arcce_submit
%{nagios_bindir}/check_arcrest_info
%{nagios_bindir}/check_arcservice
%{nagios_bindir}/check_gridstorage
%{python3_sitelib}/arcnagios
%{python3_sitelib}/nordugrid_arc_nagios_plugins-*.egg-info
%dir %{arc_spooldir}
%attr(-,nagios,nagios) %{pkg_spooldir}
%license LICENSE NOTICE
%doc AUTHORS README.rst
%doc doc/arcnagios.ini.example
%doc doc/services.cfg.example

%if %{enable_doc}
%files doc
%doc doc/_build/html
%license LICENSE NOTICE
%endif

%files egi
%dir %{pkg_sysconfdir}/60-egi.d
%config(noreplace) %{pkg_sysconfdir}/60-egi.ini
%config(noreplace) %{pkg_sysconfdir}/60-egi.d/arcce_igtf.py

%changelog
%autochangelog
