%global source0_hash 38719dfe90ebbb63cb2c88c5848d1e6fa0445d45050ecf71320ccff9101afa91

Name:		globus-gram-job-manager
%global _name %(tr - _ <<< %{name})
Version:	15.10
Release:	2%{?dist}
Summary:	Grid Community Toolkit - GRAM Jobmanager

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gsi-credential-devel >= 5
BuildRequires:	globus-gass-cache-devel >= 8
BuildRequires:	globus-gass-transfer-devel >= 7
BuildRequires:	globus-gram-protocol-devel >= 11
BuildRequires:	globus-gssapi-gsi-devel >= 10
BuildRequires:	globus-gss-assist-devel >= 8
BuildRequires:	globus-gsi-sysconfig-devel >= 5
BuildRequires:	globus-callout-devel >= 2
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-xio-popen-driver-devel >= 2
BuildRequires:	globus-rsl-devel >= 9
BuildRequires:	globus-gram-job-manager-callout-error-devel >= 2
BuildRequires:	globus-scheduler-event-generator-devel >= 4
BuildRequires:	openssl-devel
BuildRequires:	libxml2-devel
BuildRequires:	perl-interpreter
#		Additional requirements for make check
BuildRequires:	globus-io-devel >= 9
BuildRequires:	globus-gram-client-devel >= 3
BuildRequires:	globus-gass-server-ez-devel >= 2
BuildRequires:	globus-common-progs >= 15
BuildRequires:	globus-gatekeeper >= 9
BuildRequires:	globus-gram-client-tools >= 10
BuildRequires:	globus-gass-copy-progs >= 8
BuildRequires:	globus-gass-cache-program >= 5
BuildRequires:	globus-gram-job-manager-scripts >= 6
BuildRequires:	globus-proxy-utils >= 5
BuildRequires:	globus-gsi-cert-utils-progs
BuildRequires:	globus-gram-job-manager-fork-setup-poll
BuildRequires:	openssl
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Compare)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Globus::Core::Paths)
BuildRequires:	perl(Globus::GRAM::Error)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IPC::Open2)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

Requires:	globus-xio-popen-driver%{?_isa} >= 2
Requires:	globus-common-progs >= 15
Requires:	globus-gatekeeper >= 9
Requires:	globus-gram-client-tools >= 10
Requires:	globus-gass-copy-progs >= 8
Requires:	globus-gass-cache-program >= 5
Requires:	globus-gram-job-manager-scripts >= 6
Requires:	globus-proxy-utils >= 5
Requires:	globus-gsi-cert-utils-progs
Requires:	globus-seg-job-manager%{?_isa} = %{version}-%{release}
Requires:	logrotate

%package -n globus-seg-job-manager
Summary:	Grid Community Toolkit - Scheduler Event Generator Job Manager
Requires:	%{name} = %{version}-%{release}

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GRAM Jobmanager

%description -n globus-seg-job-manager
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The globus-seg-job-manager package contains:
Scheduler Event Generator Job Manager

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

export GLOBUS_VERSION=6.2
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

%if %{?rhel}%{!?rhel:0} == 6
# Remove su option from logrotate file in EPEL 6 (not supported)
sed '/ su /d' -i %{buildroot}%{_sysconfdir}/logrotate.d/globus-job-manager
%endif

%check
GLOBUS_HOSTNAME=localhost %make_build check

%ldconfig_scriptlets -n globus-seg-job-manager

%files
%{_bindir}/globus-personal-gatekeeper
%{_sbindir}/globus-gram-streamer
%{_sbindir}/globus-job-manager
%{_sbindir}/globus-job-manager-lock-test
%{_sbindir}/globus-rvf-check
%{_sbindir}/globus-rvf-edit
%dir %{_datadir}/globus
%dir %{_datadir}/globus/%{_name}
%{_datadir}/globus/%{_name}/globus-gram-job-manager.rvf
%config(noreplace) %{_sysconfdir}/logrotate.d/globus-job-manager
%dir %{_localstatedir}/lib/globus
%dir %{_localstatedir}/lib/globus/gram_job_state
%dir %{_localstatedir}/log/globus
%dir %{_sysconfdir}/globus
%config(noreplace) %{_sysconfdir}/globus/globus-gram-job-manager.conf
%doc %{_mandir}/man1/globus-personal-gatekeeper.1*
%doc %{_mandir}/man5/rsl.5*
%doc %{_mandir}/man8/globus-job-manager.8*
%doc %{_mandir}/man8/globus-rvf-check.8*
%doc %{_mandir}/man8/globus-rvf-edit.8*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files -n globus-seg-job-manager
# This is a loadable module (plugin)
%{_libdir}/libglobus_seg_job_manager.so

%changelog
%autochangelog
