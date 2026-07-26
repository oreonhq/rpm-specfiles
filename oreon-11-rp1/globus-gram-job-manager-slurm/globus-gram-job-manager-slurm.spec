%global source0_hash 9217811d3389b5a631dfbe60970b2e90139de899248b0d2eb77997de99e9d36b

Name:		globus-gram-job-manager-slurm
%global _name %(tr - _ <<< %{name})
Version:	3.0
Release:	23%{?dist}
Summary:	Grid Community Toolkit - SLURM Job Manager Support

#		The slurm.pm file is BSD, the rest is Apache-2.0
License:	Apache-2.0 AND BSD-2-Clause
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
Provides:	%{name}-setup-poll = %{version}-%{release}

Requires(preun):	globus-gram-job-manager-scripts >= 4

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
SLURM Job Manager Support

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
export MPIRUN=no
export SRUN=%{_bindir}/srun
export SBATCH=%{_bindir}/sbatch
export SALLOC=%{_bindir}/salloc
export SCANCEL=%{_bindir}/scancel
export SCONTROL=%{_bindir}/scontrol
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib}

%make_build

%install
%make_install

# Remove jobmanager-slurm from install dir - leave it for admin configuration
rm %{buildroot}%{_sysconfdir}/grid-services/jobmanager-slurm

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license files from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE
rm %{buildroot}%{_pkgdocdir}/LICENSE*

%preun
if [ $1 -eq 0 ]; then
    globus-gatekeeper-admin -d jobmanager-slurm-poll > /dev/null 2>&1 || :
fi

%files
%{_datadir}/globus/globus_gram_job_manager/slurm.rvf
%dir %{perl_vendorlib}/Globus
%dir %{perl_vendorlib}/Globus/GRAM
%dir %{perl_vendorlib}/Globus/GRAM/JobManager
%{perl_vendorlib}/Globus/GRAM/JobManager/slurm.pm
%config(noreplace) %{_sysconfdir}/globus/globus-slurm.conf
%config(noreplace) %{_sysconfdir}/grid-services/available/jobmanager-slurm-poll
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE LICENSE*

%changelog
%autochangelog
