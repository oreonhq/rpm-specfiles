%global source0_hash 2edac4af0560d9e55be9f4eec253f0f706c2613afb419b3544dcaa00daf7a3d2
%global debug_package %{nil}
%global enable_doc 1
%global nagios_bindir %{_libdir}/nagios/plugins
%global arc_spooldir %{_localstatedir}/spool/arc
%global pkg_spooldir %{arc_spooldir}/nagios
%global pkg_sysconfdir %{_sysconfdir}/arc/nagios
Name:		nordugrid-arc-nagios-plugins
Version:	3.2.3
Release:        1%{?dist}
Summary:        Nagios plugins for ARC
License:	Apache-2.0
URL:		https://www.nordugrid.org
Source0:        https://download.nordugrid.org/packages/%{name}/releases/%{version}/src/%{name}-%{version}.tar.gz
Requires:	nordugrid-arc-client
Requires:	(nordugrid-arc-plugins-arcrest >= 6.5.0 or nordugrid-arc-plugins-needed >= 7.0.0)
Requires:	nagios-common
Requires:	python3-cryptography
Requires:	python3-jinja2
Requires:	python3-ldap
# oreon:deps
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
This package provides the Nagios plugins for testing ARC computing elements.

%package doc
Summary:	HTML documentation for the ARC Nagios plugins
BuildArch:	noarch
%description doc
This package provides HTML documentation for the ARC Nagios plugins.

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
make -C doc html
rm -f doc/_build/html/.buildinfo
%install
%py3_install
install -m755 -d %{buildroot}%{pkg_spooldir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n nordugrid-arc-nagios-plugins-doc -f %{oreon_filedir}/nordugrid-arc-nagios-plugins-doc.list
%files -n nordugrid-arc-nagios-plugins-egi -f %{oreon_filedir}/nordugrid-arc-nagios-plugins-egi.list

%changelog

%autochangelog
