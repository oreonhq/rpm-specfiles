%global source0_hash b7c764a78cebe8de06eddbfb3a5e5f9e3330054a9052d36d9c599b673dac3a1c

%global _hardened_build 1

Name:		globus-scheduler-event-generator
%global _name %(tr - _ <<< %{name})
Version:	6.6
Release:	2%{?dist}
Summary:	Grid Community Toolkit - Scheduler Event Generator

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source1:	%{name}@.service
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-gram-protocol-devel >= 11
BuildRequires:	globus-xio-gsi-driver-devel >= 2
BuildRequires:	libtool-ltdl-devel
BuildRequires:	doxygen
BuildRequires:	systemd-rpm-macros
#		Additional requirements for make check
BuildRequires:	perl-interpreter
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Compare)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More)

Requires:	globus-xio-gsi-driver%{?_isa} >= 2

%package progs
Summary:	Grid Community Toolkit - Scheduler Event Generator Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%package devel
Summary:	Grid Community Toolkit - Scheduler Event Generator Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Scheduler Event Generator Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Scheduler Event Generator

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
Scheduler Event Generator Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Scheduler Event Generator Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Scheduler Event Generator Documentation Files

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
	   --with-initscript-config-path=%{_sysconfdir}/sysconfig/%{name} \
	   --with-lockfile-path=/run/lock/subsys/%{name}

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Remove start-up scripts
rm -rf %{buildroot}%{_sysconfdir}/init.d

# Install start-up scripts
mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p %{SOURCE1} %{buildroot}%{_unitdir}

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%check
%make_build check

%ldconfig_scriptlets

%post progs
if [ $1 -eq 1 ] ; then
    systemctl daemon-reload > /dev/null 2>&1 || :
fi

%preun progs
if [ $1 -eq 0 ] ; then
    for INSTANCE in `systemctl | grep %{name}@ | awk '{print $1;}'`; do
	systemctl --no-reload disable $INSTANCE > /dev/null 2>&1 || :
	systemctl stop $INSTANCE > /dev/null 2>&1 || :
    done
fi

%postun progs
if [ $1 -ge 1 ] ; then
    systemctl daemon-reload > /dev/null 2>&1 || :
    for INSTANCE in `systemctl | grep %{name}@ | awk '{print $1;}'`; do
	systemctl try-restart $INSTANCE > /dev/null 2>&1 || :
    done
fi

%files
%{_libdir}/libglobus_scheduler_event_generator.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_sbindir}/globus-scheduler-event-generator
%{_sbindir}/globus-scheduler-event-generator-admin
%{_mandir}/man8/globus-scheduler-event-generator.8*
%{_mandir}/man8/globus-scheduler-event-generator-admin.8*
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}@.service
%dir %{_sysconfdir}/globus
%dir %{_sysconfdir}/globus/scheduler-event-generator
%dir %{_sysconfdir}/globus/scheduler-event-generator/available

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_scheduler_event_generator.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
%autochangelog
