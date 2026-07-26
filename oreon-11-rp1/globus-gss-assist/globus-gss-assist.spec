%global source0_hash 5184e0f1a09a64651472f19b79101fc6d966056fd9e1ee29512e41f694eae759

Name:		globus-gss-assist
%global _name %(tr - _ <<< %{name})
Version:	12.7
Release:	10%{?dist}
Summary:	Grid Community Toolkit - GSSAPI Assist library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gsi-sysconfig-devel >= 7
BuildRequires:	globus-gsi-cert-utils-devel >= 8
BuildRequires:	globus-gssapi-gsi-devel >= 13
BuildRequires:	globus-callout-devel >= 2
BuildRequires:	globus-gsi-credential-devel >= 6
BuildRequires:	doxygen
BuildRequires:	perl-generators
#		Additional requirements for make check
BuildRequires:	openssl
BuildRequires:	perl-interpreter
BuildRequires:	perl(English)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(warnings)

Requires:	globus-gsi-sysconfig%{?_isa} >= 7
Requires:	globus-gssapi-gsi%{?_isa} >= 13

%package progs
Summary:	Grid Community Toolkit - GSSAPI Assist library Programs
BuildArch:	noarch

%package devel
Summary:	Grid Community Toolkit - GSSAPI Assist library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - GSSAPI Assist library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GSSAPI Assist library

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
GSSAPI Assist library Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GSSAPI Assist library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
GSSAPI Assist library Documentation Files

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
%{_libdir}/libglobus_gss_assist.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_sbindir}/grid-mapfile-add-entry
%{_sbindir}/grid-mapfile-check-consistency
%{_sbindir}/grid-mapfile-delete-entry
%doc %{_mandir}/man8/grid-mapfile-add-entry.8*
%doc %{_mandir}/man8/grid-mapfile-check-consistency.8*
%doc %{_mandir}/man8/grid-mapfile-delete-entry.8*
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gss_assist.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
%autochangelog
