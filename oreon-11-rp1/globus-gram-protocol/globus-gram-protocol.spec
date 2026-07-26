%global source0_hash 6558d8ab99bf3d65e5e56435069a107db5dbf71dd8edc203b8a689837eb1befb

Name:		globus-gram-protocol
%global _name %(tr - _ <<< %{name})
Version:	13.6
Release:	11%{?dist}
Summary:	Grid Community Toolkit - GRAM Protocol Library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-io-devel >= 8
BuildRequires:	globus-gssapi-gsi-devel >= 10
BuildRequires:	globus-gss-assist-devel >= 8
BuildRequires:	doxygen
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
#		Additional requirements for make check
BuildRequires:	openssl

%package devel
Summary:	Grid Community Toolkit - GRAM Protocol Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - GRAM Protocol Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GRAM Protocol Library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GRAM Protocol Library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
GRAM Protocol Library Documentation Files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib}

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
%{_libdir}/libglobus_gram_protocol.so.*
%dir %{perl_vendorlib}/Globus
%dir %{perl_vendorlib}/Globus/GRAM
%{perl_vendorlib}/Globus/GRAM/Error.pm
%{perl_vendorlib}/Globus/GRAM/JobSignal.pm
%{perl_vendorlib}/Globus/GRAM/JobState.pm
%dir %{_datadir}/globus
%{_datadir}/globus/globus-gram-protocol-constants.sh
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gram_protocol.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%dir %{_pkgdocdir}/perl
%dir %{_pkgdocdir}/perl/Globus
%dir %{_pkgdocdir}/perl/Globus/GRAM
%doc %{_pkgdocdir}/perl/Globus/GRAM/*.html
%license GLOBUS_LICENSE

%changelog
%autochangelog
