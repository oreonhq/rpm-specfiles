%global source0_hash 52db8a663e6b5d5a23e677d0a902c26333a0b4f9f73377ccb24efe5515be1c29

%global _hardened_build 1

Name:		globus-gatekeeper
%global _name %(tr - _ <<< %{name})
Version:	11.4
Release:	11%{?dist}
Summary:	Grid Community Toolkit - Globus Gatekeeper

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source1:	%{name}.service
Source3:	%{name}.README
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gss-assist-devel >= 8
BuildRequires:	globus-gssapi-gsi-devel >= 9
BuildRequires:	openssl-devel
BuildRequires:	systemd-rpm-macros

Requires:	logrotate
%{?systemd_requires}

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus Gatekeeper

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

# Remove start-up script
rm -rf %{buildroot}%{_sysconfdir}/init.d

# Install start-up script
mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p %{SOURCE1} %{buildroot}%{_unitdir}

# Install post installation instructions
install -m 644 -p %{SOURCE3} %{buildroot}%{_pkgdocdir}/README.Fedora

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

mkdir -p %{buildroot}%{_sysconfdir}/grid-services
mkdir -p %{buildroot}%{_sysconfdir}/grid-services/available

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_sbindir}/globus-gatekeeper
%{_sbindir}/globus-k5
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/grid-services
%dir %{_sysconfdir}/grid-services/available
%doc %{_mandir}/man8/globus-gatekeeper.8*
%doc %{_mandir}/man8/globus-k5.8*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/README.Fedora
%license GLOBUS_LICENSE

%changelog
%autochangelog
