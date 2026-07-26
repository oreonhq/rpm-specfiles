%global source0_hash 86677b4aef54b32bcdc11bb48d63f0a30ee520c8aa60e1f0f51d6cd671ee4010

Name:		globus-ftp-control
%global _name %(tr - _ <<< %{name})
Version:	9.10
Release:	10%{?dist}
Summary:	Grid Community Toolkit - GridFTP Control Library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gss-assist-devel >= 11
BuildRequires:	globus-gssapi-gsi-devel >= 13
BuildRequires:	globus-io-devel >= 11
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-gssapi-error-devel >= 4
BuildRequires:	globus-xio-gsi-driver-devel >= 4
BuildRequires:	doxygen
#		Additional requirements for make check
BuildRequires:	openssl

Requires:	globus-gss-assist%{?_isa} >= 11
Requires:	globus-gssapi-gsi%{?_isa} >= 13
Requires:	globus-io%{?_isa} >= 11
Requires:	globus-xio-gsi-driver%{?_isa} >= 4

%package devel
Summary:	Grid Community Toolkit - GridFTP Control Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - GridFTP Control Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GridFTP Control Library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GridFTP Control Library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
GridFTP Control Library Documentation Files

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

%check
GLOBUS_HOSTNAME=localhost %make_build check

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_ftp_control.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_ftp_control.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
%autochangelog
