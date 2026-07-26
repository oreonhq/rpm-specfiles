%global source0_hash dcb8309c034c8b485f86ce9756549320fca2d10e01b32d6cb3b3c0df00c7415f

Name:		globus-gram-job-manager-pbs
%global _name %(tr - _ <<< %{name})
Version:	3.1
Release:	21%{?dist}
Summary:	Grid Community Toolkit - PBS Job Manager Support

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-scheduler-event-generator-devel >= 4
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	systemd-rpm-macros

Requires:	globus-gram-job-manager >= 13
Requires:	globus-gram-job-manager-scripts >= 4
Requires:	globus-gass-cache-program >= 5
Requires:	globus-gatekeeper >= 9
Requires:	%{name}-setup = %{version}-%{release}

%package setup-poll
Summary:	Grid Community Toolkit - PBS Job Manager Support using polling
BuildArch:	noarch
Provides:	%{name}-setup = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

Requires(preun):	globus-gram-job-manager-scripts >= 4

%package setup-seg
Summary:	Grid Community Toolkit - PBS Job Manager Support using SEG
Provides:	%{name}-setup = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	globus-scheduler-event-generator-progs >= 4

Requires(preun):	globus-gram-job-manager-scripts >= 4
Requires(preun):	globus-scheduler-event-generator-progs >= 4
Requires(postun):	globus-scheduler-event-generator-progs >= 4
%{?systemd_requires}

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
PBS Job Manager Support

%description setup-poll
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-setup-poll package contains:
PBS Job Manager Support using polling to monitor job state

%description setup-seg
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-setup-seg package contains:
PBS Job Manager Support using the scheduler event generator to monitor job
state

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

export MPIEXEC=no
export MPIRUN=no
export QDEL=%{_bindir}/qdel-torque
export QSTAT=%{_bindir}/qstat-torque
export QSUB=%{_bindir}/qsub-torque
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib} \
	   --with-globus-state-dir=%{_localstatedir}/log/globus \
	   --with-log-path=%{_localstatedir}/log/torque/server_logs

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Remove jobmanager-pbs from install dir - leave it for admin configuration
rm %{buildroot}%{_sysconfdir}/grid-services/jobmanager-pbs

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%preun setup-poll
if [ $1 -eq 0 ]; then
    globus-gatekeeper-admin -d jobmanager-pbs-poll > /dev/null 2>&1 || :
fi

%preun setup-seg
if [ $1 -eq 0 ]; then
    globus-gatekeeper-admin -d jobmanager-pbs-seg > /dev/null 2>&1 || :
    systemctl --no-reload disable globus-scheduler-event-generator@pbs > /dev/null 2>&1 || :
    systemctl stop globus-scheduler-event-generator@pbs > /dev/null 2>&1 || :
    globus-scheduler-event-generator-admin -d pbs > /dev/null 2>&1 || :
fi

%ldconfig_post setup-seg

%postun setup-seg
%{?ldconfig}
if [ $1 -ge 1 ]; then
    systemctl try-restart globus-scheduler-event-generator@pbs > /dev/null 2>&1 || :
fi

%files
%{_datadir}/globus/globus_gram_job_manager/pbs.rvf
%dir %{perl_vendorlib}/Globus
%dir %{perl_vendorlib}/Globus/GRAM
%dir %{perl_vendorlib}/Globus/GRAM/JobManager
%{perl_vendorlib}/Globus/GRAM/JobManager/pbs.pm
%config(noreplace) %{_sysconfdir}/globus/globus-pbs.conf
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files setup-poll
%config(noreplace) %{_sysconfdir}/grid-services/available/jobmanager-pbs-poll

%files setup-seg
# This is a loadable module (plugin)
%{_libdir}/libglobus_seg_pbs.so
%config(noreplace) %{_sysconfdir}/grid-services/available/jobmanager-pbs-seg
%config(noreplace) %{_sysconfdir}/globus/scheduler-event-generator/available/pbs

%changelog
%autochangelog
