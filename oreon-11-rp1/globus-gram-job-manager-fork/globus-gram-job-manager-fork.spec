%global source0_hash 5a35fec504a032dbe4a1f33fe879b6d08708a60dc4fff78bc0f557324cdd9296

Name:		globus-gram-job-manager-fork
%global _name %(tr - _ <<< %{name})
Version:	3.4
Release:	2%{?dist}
Summary:	Grid Community Toolkit - Fork Job Manager Support

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-scheduler-event-generator-devel >= 4
BuildRequires:	globus-gram-protocol-devel >= 11
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	systemd-rpm-macros

#		A requirement on globus-gram-job-manager would make sense.
#		However, that would create a circular build dependency when
#		building the globus-gram-job-manager package, since the test
#		suite for that package requires globus-gram-job-manager-fork
#		to run.
# Requires:	globus-gram-job-manager >= 13
Requires:	globus-gram-job-manager-scripts >= 4
Requires:	globus-gass-cache-program >= 5
Requires:	globus-gatekeeper >= 9
Requires:	%{name}-setup = %{version}-%{release}

%package setup-poll
Summary:	Grid Community Toolkit - Fork Job Manager Support using polling
BuildArch:	noarch
Provides:	%{name}-setup = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

Requires(preun):	globus-gram-job-manager-scripts >= 4

%package setup-seg
Summary:	Grid Community Toolkit - Fork Job Manager Support using SEG
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
Fork Job Manager Support

%description setup-poll
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-setup-poll package contains:
Fork Job Manager Support using polling to monitor job state

%description setup-seg
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-setup-seg package contains:
Fork Job Manager Support using the scheduler event generator to monitor job
state

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

export MPIEXEC=no
export MPIRUN=no
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib} \
	   --with-globus-state-dir=%{_localstatedir}/log/globus

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Remove jobmanager-fork from install dir - leave it for admin configuration
rm %{buildroot}%{_sysconfdir}/grid-services/jobmanager-fork

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%preun setup-poll
if [ $1 -eq 0 ]; then
    globus-gatekeeper-admin -d jobmanager-fork-poll > /dev/null 2>&1 || :
fi

%preun setup-seg
if [ $1 -eq 0 ]; then
    globus-gatekeeper-admin -d jobmanager-fork-seg > /dev/null 2>&1 || :
    systemctl --no-reload disable globus-scheduler-event-generator@fork > /dev/null 2>&1 || :
    systemctl stop globus-scheduler-event-generator@fork > /dev/null 2>&1 || :
    globus-scheduler-event-generator-admin -d fork > /dev/null 2>&1 || :
fi

%ldconfig_post setup-seg

%postun setup-seg
%{?ldconfig}
if [ $1 -ge 1 ]; then
    systemctl try-restart globus-scheduler-event-generator@fork > /dev/null 2>&1 || :
fi

%files
%dir %{perl_vendorlib}/Globus
%dir %{perl_vendorlib}/Globus/GRAM
%dir %{perl_vendorlib}/Globus/GRAM/JobManager
%{perl_vendorlib}/Globus/GRAM/JobManager/fork.pm
%dir %{_sysconfdir}/globus
%config(noreplace) %{_sysconfdir}/globus/globus-fork.conf
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files setup-poll
%config(noreplace) %{_sysconfdir}/grid-services/available/jobmanager-fork-poll

%files setup-seg
# This is a loadable module (plugin)
%{_libdir}/libglobus_seg_fork.so
%{_sbindir}/globus-fork-starter
%doc %{_mandir}/man8/globus-fork-starter.8*
%config(noreplace) %{_sysconfdir}/grid-services/available/jobmanager-fork-seg
%config(noreplace) %{_sysconfdir}/globus/scheduler-event-generator/available/fork

%changelog
%autochangelog
