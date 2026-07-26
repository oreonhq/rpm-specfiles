%global source0_hash 0ef2d71173b8bc3af705d1626f52007173bda5719b7270a4d80740779439f23a

%global _hardened_build 1

Name:		globus-gass-server-ez
%global _name %(tr - _ <<< %{name})
Version:	6.2
Release:	10%{?dist}
Summary:	Grid Community Toolkit - Globus Gass Server_ez

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gass-transfer-devel >= 7
BuildRequires:	globus-gssapi-gsi-devel >= 10
BuildRequires:	globus-gss-assist-devel >= 8

%package progs
Summary:	Grid Community Toolkit - Globus Gass Server_ez Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package devel
Summary:	Grid Community Toolkit - Globus Gass Server_ez Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus Gass Server_ez

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
Globus Gass Server_ez Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus Gass Server_ez Development Files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

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

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_gass_server_ez.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_bindir}/globus-gass-server
%{_bindir}/globus-gass-server-shutdown

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gass_server_ez.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
