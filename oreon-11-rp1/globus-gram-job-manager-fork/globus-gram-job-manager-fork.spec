%global source0_hash 5a35fec504a032dbe4a1f33fe879b6d08708a60dc4fff78bc0f557324cdd9296
Name:		globus-gram-job-manager-fork
%global _name %(tr - _ <<< %{name})
Version:	6.2.20251212
Release:        1%{?dist}
Summary:        Grid Community Toolkit - Fork Job Manager Support
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
Requires:	globus-gram-job-manager-scripts >= 4
Requires:	globus-gass-cache-program >= 5
Requires:	globus-gatekeeper >= 9
Requires:	%{name}-setup = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-gram-protocol-devel
BuildRequires:  globus-scheduler-event-generator-devel
BuildRequires:  globus-xio-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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

export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"
export MPIEXEC=no
export MPIRUN=no
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-perlmoduledir=%{perl_vendorlib} \
	   --with-globus-state-dir=%{_localstatedir}/log/globus
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_sysconfdir}/grid-services/jobmanager-fork
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n globus-gram-job-manager-fork-setup-poll -f %{oreon_filedir}/globus-gram-job-manager-fork-setup-poll.list
%files -n globus-gram-job-manager-fork-setup-seg -f %{oreon_filedir}/globus-gram-job-manager-fork-setup-seg.list

%changelog

%autochangelog
