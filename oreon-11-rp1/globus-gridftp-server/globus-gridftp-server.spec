%global source0_hash 98be8b9af9a9682bbad3bbff83309f454a7de2e822bb667d188b86df8b76b615

%global _hardened_build 1

Name:		globus-gridftp-server
%global _name %(tr - _ <<< %{name})
Version:	13.28
Release:	2%{?dist}
Summary:	Grid Community Toolkit - Globus GridFTP Server

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source1:	%{name}.service
Source2:	globus-gridftp-sshftp.service
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 17
BuildRequires:	globus-xio-devel >= 5
BuildRequires:	globus-xio-gsi-driver-devel >= 2
BuildRequires:	globus-gfork-devel >= 3
BuildRequires:	globus-gridftp-server-control-devel >= 9
BuildRequires:	globus-ftp-control-devel >= 7
BuildRequires:	globus-authz-devel >= 2
BuildRequires:	globus-gssapi-gsi-devel >= 10
BuildRequires:	globus-gss-assist-devel >= 9
BuildRequires:	globus-gsi-credential-devel >= 6
BuildRequires:	globus-gsi-sysconfig-devel >= 5
BuildRequires:	globus-io-devel >= 9
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	perl-generators
BuildRequires:	systemd-rpm-macros
#		Additional requirements for make check
BuildRequires:	openssl
#		Optional test dependency
BuildRequires:	fakeroot

Requires:	globus-xio-gsi-driver%{?_isa} >= 2
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 8
Recommends:	globus-xio-udt-driver%{?_isa} >= 1
%else
Requires:	globus-xio-udt-driver%{?_isa} >= 1
%endif
Requires:	globus-common%{?_isa} >= 17
Requires:	globus-xio%{?_isa} >= 5
Requires:	globus-gridftp-server-control%{?_isa} >= 9
Requires:	globus-ftp-control%{?_isa} >= 7

%package progs
Summary:	Grid Community Toolkit - Globus GridFTP Server Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%package devel
Summary:	Grid Community Toolkit - Globus GridFTP Server Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus GridFTP Server

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
Globus GridFTP Server Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus GridFTP Server Development Files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

export GRIDMAP=%{_sysconfdir}/grid-security/grid-mapfile
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

mv %{buildroot}%{_sysconfdir}/gridftp.conf.default \
   %{buildroot}%{_sysconfdir}/gridftp.conf
mkdir -p %{buildroot}%{_sysconfdir}/xinetd.d
mv %{buildroot}%{_sysconfdir}/gridftp.xinetd.default \
   %{buildroot}%{_sysconfdir}/xinetd.d/gridftp
mv %{buildroot}%{_sysconfdir}/gridftp.gfork.default \
   %{buildroot}%{_sysconfdir}/gridftp.gfork

# No need for environment in conf files
sed '/ env /d' -i %{buildroot}%{_sysconfdir}/gridftp.gfork
sed '/^env /d' -i %{buildroot}%{_sysconfdir}/xinetd.d/gridftp

# Remove start-up scripts
rm -rf %{buildroot}%{_sysconfdir}/init.d

# Install start-up scripts
mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p %{SOURCE1} %{SOURCE2} %{buildroot}%{_unitdir}

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%check
%make_build check

%ldconfig_scriptlets

%post progs
%systemd_post %{name}.service globus-gridftp-sshftp.service

%preun progs
%systemd_preun %{name}.service globus-gridftp-sshftp.service

%postun progs
%systemd_postun_with_restart %{name}.service globus-gridftp-sshftp.service

%files
%{_libdir}/libglobus_gridftp_server.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_sbindir}/gfs-dynbe-client
%{_sbindir}/gfs-gfork-master
%{_sbindir}/globus-gridftp-password
%{_sbindir}/globus-gridftp-server
%{_sbindir}/globus-gridftp-server-enable-sshftp
%{_sbindir}/globus-gridftp-server-setup-chroot
%config(noreplace) %{_sysconfdir}/gridftp.conf
%config(noreplace) %{_sysconfdir}/gridftp.gfork
%config(noreplace) %{_sysconfdir}/xinetd.d/gridftp
%{_unitdir}/%{name}.service
%{_unitdir}/globus-gridftp-sshftp.service
%doc %{_mandir}/man8/globus-gridftp-password.8*
%doc %{_mandir}/man8/globus-gridftp-server.8*
%doc %{_mandir}/man8/globus-gridftp-server-setup-chroot.8*

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gridftp_server.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
