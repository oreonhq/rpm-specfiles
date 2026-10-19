%global source0_hash 38719dfe90ebbb63cb2c88c5848d1e6fa0445d45050ecf71320ccff9101afa91
Name:		globus-gram-job-manager
%global _name %(tr - _ <<< %{name})
Version:	15.10
Release:        2%{?dist}
Summary:        Grid Community Toolkit - GRAM Jobmanager
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
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
# oreon:deps
BuildRequires:  gcc
BuildRequires:  globus-callout-devel
BuildRequires:  globus-common-devel
BuildRequires:  globus-common-progs
BuildRequires:  globus-gass-cache-devel
BuildRequires:  globus-gass-cache-program
BuildRequires:  globus-gass-copy-progs
BuildRequires:  globus-gass-server-ez-devel
BuildRequires:  globus-gass-transfer-devel
BuildRequires:  globus-gatekeeper
BuildRequires:  globus-gram-client-devel
BuildRequires:  globus-gram-client-tools
BuildRequires:  globus-gram-job-manager-callout-error-devel
BuildRequires:  globus-gram-job-manager-fork-setup-poll
BuildRequires:  globus-gram-job-manager-scripts
BuildRequires:  globus-gram-protocol-devel
BuildRequires:  globus-gsi-cert-utils-progs
BuildRequires:  globus-gsi-credential-devel
BuildRequires:  globus-gsi-sysconfig-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  globus-io-devel
BuildRequires:  globus-proxy-utils
BuildRequires:  globus-rsl-devel
BuildRequires:  globus-scheduler-event-generator-devel
BuildRequires:  globus-xio-devel
BuildRequires:  globus-xio-popen-driver-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Globus::Core::Paths)
BuildRequires:  perl(Globus::GRAM::Error)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl-interpreter
# /oreon:deps
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

export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"
export GLOBUS_VERSION=6.2
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE
%oreon_autofiles globus-seg-job-manager usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

GLOBUS_HOSTNAME=localhost %make_build check
%ldconfig_scriptlets -n globus-seg-job-manager
%files -f %{oreon_filedir}/main.list
%files -n globus-seg-job-manager -f %{oreon_filedir}/globus-seg-job-manager.list

%changelog

%autochangelog
