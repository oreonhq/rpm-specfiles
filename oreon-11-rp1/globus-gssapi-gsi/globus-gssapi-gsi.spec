%global source0_hash 2ba4e905f1dbbbee8ade01a6d0d59a9b5e816620fe5b080de0524b5331614236

Name:		globus-gssapi-gsi
%global _name %(tr - _ <<< %{name})
Version:	14.20
Release:	10%{?dist}
Summary:	Grid Community Toolkit - GSSAPI library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-openssl-module-devel >= 3
BuildRequires:	globus-gsi-openssl-error-devel >= 2
BuildRequires:	globus-gsi-cert-utils-devel >= 8
BuildRequires:	globus-gsi-credential-devel >= 5
BuildRequires:	globus-gsi-callback-devel >= 4
BuildRequires:	globus-gsi-proxy-core-devel >= 8
BuildRequires:	globus-gsi-sysconfig-devel >= 8
BuildRequires:	openssl-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	doxygen
#		Additional requirements for make check
BuildRequires:	openssl
BuildRequires:	perl-interpreter
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)

Requires:	globus-gsi-sysconfig%{?_isa} >= 8
%if %{?rhel}%{!?rhel:0} == 7
Requires:	openssl-libs >= 1.0.2
%endif

%package devel
Summary:	Grid Community Toolkit - GSSAPI library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - GSSAPI library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GSSAPI library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GSSAPI library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
GSSAPI library Documentation Files

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
%make_build check

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_gssapi_gsi.so.*
%config(noreplace) %{_sysconfdir}/grid-security/gsi.conf
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gssapi_gsi.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
%autochangelog
