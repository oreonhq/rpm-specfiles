%global source0_hash 19686927abd3fe93f12b15e7799d777b557834c5a20522543942a3cb291055f3

Name:		globus-gram-job-manager-scripts
%global _name %(tr - _ <<< %{name})
Version:	7.3
Release:	15%{?dist}
Summary:	Grid Community Toolkit - GRAM Job ManagerScripts

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
BuildArch:	noarch

BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter

%package doc
Summary:	Grid Community Toolkit - GRAM Job ManagerScripts Documentation Files

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GRAM Job ManagerScripts

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
GRAM Job ManagerScripts Documentation Files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib}

%make_build

%install
%make_install

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

# Remove libdir reference from noarch package
sed '/$libdir =/d' \
    -i $RPM_BUILD_ROOT%{_datadir}/globus/globus-job-manager-script.pl

%files
%{_sbindir}/globus-gatekeeper-admin
%dir %{_datadir}/globus
%{_datadir}/globus/globus-job-manager-script.pl
%dir %{perl_vendorlib}/Globus
%dir %{perl_vendorlib}/Globus/GRAM
%{perl_vendorlib}/Globus/GRAM/JobDescription.pm
%{perl_vendorlib}/Globus/GRAM/JobManager.pm
%{perl_vendorlib}/Globus/GRAM/StdioMerger.pm
%doc %{_mandir}/man8/globus-gatekeeper-admin.8*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/perl
%dir %{_pkgdocdir}/perl/Globus
%dir %{_pkgdocdir}/perl/Globus/GRAM
%doc %{_pkgdocdir}/perl/Globus/GRAM/*.html
%license GLOBUS_LICENSE

%changelog
%autochangelog
