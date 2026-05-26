# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7276bcf214f31051188b2e44f11029e57303f37e54126e517000c1b2123a6d4e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name: ipvsadm
Summary: Utility to administer the Linux Virtual Server
Version: 1.31
Release: 17%{?dist}
License: GPL-2.0-or-later
URL: https://kernel.org/pub/linux/utils/kernel/ipvsadm/

Source0: https://kernel.org/pub/linux/utils/kernel/ipvsadm/%{name}-%{version}.tar.gz
Source1: ipvsadm.service
Source2: ipvsadm-config

Patch0: 0003-ipvsadm-use-CFLAGS-and-LDFLAGS-environment-variables.patch

BuildRequires: gcc
Buildrequires: libnl3-devel
Buildrequires: popt-devel
BuildRequires: systemd
BuildRequires: make

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
ipvsadm is used to setup, maintain, and inspect the virtual server
table in the Linux kernel. The Linux Virtual Server can be used to
build scalable network services based on a cluster of two or more
nodes. The active node of the cluster redirects service requests to a
collection of server hosts that will actually perform the
services. Supported Features include:
  - two transport layer (layer-4) protocols (TCP and UDP)
  - three packet-forwarding methods (NAT, tunneling, and direct routing)
  - eight load balancing algorithms (round robin, weighted round robin,
    least-connection, weighted least-connection, locality-based
    least-connection, locality-based least-connection with
    replication, destination-hashing, and source-hashing)

%prep
%oreon_verify_sources
%setup -q
%patch -P0 -p1

%build
%set_build_flags
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/rc.d/init.d
%{__make} install BUILD_ROOT=%{buildroot}%{_prefix} SBIN=%{buildroot}%{_sbindir} MANDIR=%{buildroot}%{_mandir} MAN=%{buildroot}%{_mandir}/man8 INIT=%{buildroot}%{_sysconfdir}/rc.d/init.d

%{__rm} -f %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -p -D -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-config

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc MAINTAINERS README
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-config
%{_sbindir}/%{name}
%{_sbindir}/%{name}-restore
%{_sbindir}/%{name}-save
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}-restore.8*
%{_mandir}/man8/%{name}-save.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.31-17
- Prepare for Oreon 11 (RP1)
