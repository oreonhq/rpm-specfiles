%global source0_hash 5da8b2ddb3cb03edd6c046e1475d9bdf3b34f5d3398b79fbabe32ebc98f0fd50

Name:		globus-gram-job-manager-condor
%global _name %(tr - _ <<< %{name})
Version:	3.0
Release:	23%{?dist}
Summary:	Grid Community Toolkit - Condor Job Manager Support

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
BuildArch:	noarch

BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter

Requires:	globus-gram-job-manager >= 13
Requires:	globus-gram-job-manager-scripts >= 4
Requires:	globus-gass-cache-program >= 5
Requires:	globus-gatekeeper >= 9

Requires(preun):	globus-gram-job-manager-scripts >= 4

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Condor Job Manager Support

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
export CONDOR_RM=%{_bindir}/condor_rm
export CONDOR_SUBMIT=%{_bindir}/condor_submit
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib} \
	   --with-condor-os=LINUX \
	   --with-condor-arch=""

%make_build

%install
%make_install

# Remove jobmanager-condor from install dir - leave it for admin configuration
rm %{buildroot}%{_sysconfdir}/grid-services/jobmanager-condor

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%preun
if [ $1 -eq 0 ]; then
    globus-gatekeeper-admin -d jobmanager-condor > /dev/null 2>&1 || :
fi

%files
%{_datadir}/globus/globus_gram_job_manager/condor.rvf
%dir %{perl_vendorlib}/Globus
%dir %{perl_vendorlib}/Globus/GRAM
%dir %{perl_vendorlib}/Globus/GRAM/JobManager
%{perl_vendorlib}/Globus/GRAM/JobManager/condor.pm
%config(noreplace) %{_sysconfdir}/globus/globus-condor.conf
%config(noreplace) %{_sysconfdir}/grid-services/available/jobmanager-condor
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%changelog
%autochangelog
