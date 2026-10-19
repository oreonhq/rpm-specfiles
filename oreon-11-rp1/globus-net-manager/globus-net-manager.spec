%global source0_hash e986a69e36fe2029b8813458187f5ac467dd98ce11b64b5453f1ada7c6251ec7
Name:		globus-net-manager
%global _name %(tr - _ <<< %{name})
Version:	6.2.20251212
Release:        1%{?dist}
Summary:        Grid Community Toolkit - Network Manager Library
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
Requires:	globus-common%{?_isa} >= 15.27
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-xio-devel
BuildRequires:  make
BuildRequires:  perl(strict)
BuildRequires:  perl-interpreter
BuildRequires:  python2-devel
# /oreon:deps
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

export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"
export PYTHON_CONFIG=%{__python2}-config
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --enable-python
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE
%oreon_autofiles globus-xio-net-manager-driver usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles globus-xio-net-manager-driver-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

GLOBUS_HOSTNAME=localhost PYTHONDONTWRITEBYTECODE=1 %make_build check
%ldconfig_scriptlets
%ldconfig_scriptlets -n globus-xio-net-manager-driver
%files -f %{oreon_filedir}/main.list
%files -n globus-net-manager-devel -f %{oreon_filedir}/globus-net-manager-devel.list
%files -n globus-xio-net-manager-driver -f %{oreon_filedir}/globus-xio-net-manager-driver.list
%files -n globus-xio-net-manager-driver-devel -f %{oreon_filedir}/globus-xio-net-manager-driver-devel.list
%files -n globus-net-manager-doc -f %{oreon_filedir}/globus-net-manager-doc.list

%changelog

%autochangelog
