%global source0_hash e986a69e36fe2029b8813458187f5ac467dd98ce11b64b5453f1ada7c6251ec7

Name:		globus-net-manager
%global _name %(tr - _ <<< %{name})
Version:	1.7
Release:	14%{?dist}
Summary:	Grid Community Toolkit - Network Manager Library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15.27
BuildRequires:	globus-xio-devel >= 5
%if %{?fedora}%{!?fedora:0} >= 30 || %{?rhel}%{!?rhel:0} >= 8
BuildRequires:	python3-devel
%else
BuildRequires:	python2-devel
%endif
BuildRequires:	doxygen
BuildRequires:	perl-interpreter
BuildRequires:	perl(strict)

Requires:	globus-common%{?_isa} >= 15.27

%package devel
Summary:	Grid Community Toolkit - Network Manager Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package -n globus-xio-net-manager-driver
Summary:	Grid Community Toolkit - Globus XIO Network Manager Driver
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	globus-xio%{?_isa} >= 5

%package -n globus-xio-net-manager-driver-devel
Summary:	Grid Community Toolkit - Globus XIO Network Manager Driver Development Files
Requires:	globus-xio-net-manager-driver%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Network Manager Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Network Manager Library

The Globus Neteork Manager Library is a plug-in point for network management
tasks, such as:
 - selectively open ports in a firewall and allow these ports to be closed
   when transfers are complete
 - configure a virtual circuit based on a site policy and route traffic
   over this circuit
 - route network traffic related to a task over a particular network

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Network Manager Library Development Files

%description -n globus-xio-net-manager-driver
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The globus-xio-net-manager-driver package contains:
Globus XIO Network Manager Driver

%description -n globus-xio-net-manager-driver-devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The globus-xio-net-manager-driver-devel package contains:
Globus XIO Network Manager Driver Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Network Manager Library Documentation Files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%if %{?fedora}%{!?fedora:0} >= 30 || %{?rhel}%{!?rhel:0} >= 8
export PYTHON_CONFIG=%{__python3}-config
%else
export PYTHON_CONFIG=%{__python2}-config
%endif

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --enable-python

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%check
GLOBUS_HOSTNAME=localhost PYTHONDONTWRITEBYTECODE=1 %make_build check

%ldconfig_scriptlets

%ldconfig_scriptlets -n globus-xio-net-manager-driver

%files
%{_libdir}/libglobus_net_manager.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/globus_net_manager.h
%{_includedir}/globus/globus_net_manager_attr.h
%{_libdir}/libglobus_net_manager.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n globus-xio-net-manager-driver
# This is a loadable module (plugin)
%{_libdir}/libglobus_xio_net_manager_driver.so

%files -n globus-xio-net-manager-driver-devel
%{_includedir}/globus/globus_xio_net_manager_driver.h
%{_libdir}/pkgconfig/globus-xio-net-manager-driver.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
%autochangelog
