%global source0_hash 855fa5400d90fc177e97266320181c8fe205bdef7b24cd435990052f82979071
%bcond check 1
%global goipath         github.com/fido-device-onboard/go-fdo-server
%global with_debug 1
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif
Version:        1.0.1
%gometa -L -f
Name:           go-fdo-server
Release:        1%{?dist}
Summary:        A Go implementation of the FIDO Device Onboard Specification
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-fdo-server-group.conf
Source3:        go-fdo-server-manufacturer-user.conf
Source4:        go-fdo-server-rendezvous-user.conf
Source5:        go-fdo-server-owner-user.conf
%{?sysusers_requires_compat}
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This package provides a server-side implementation of the FIDO Device Onboard
(FDO) specification, written in Go. FDO is an open standard for the late
binding of device credentials, allowing for automated and secure on-boarding of
devices when they are first powered on in their final location.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
#%%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export GOEXPERIMENT="nodwarf5"
export GO_LDFLAGS="-X %{goipath}/internal/version.VERSION=%{version}"
%gobuild -o %{gobuilddir}/bin/go-fdo-server %{goipath}
%install
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}
install -m 0750 -vd %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -vp configs/manufacturing.yaml %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -vp configs/owner.yaml %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -vp configs/rendezvous.yaml %{buildroot}%{_sysconfdir}/%{name}
install -m 0750 -vd %{buildroot}%{_sysconfdir}/pki/%{name}
install -m 0644 -vp -D %{SOURCE2} %{buildroot}/%{_sysusersdir}/go-fdo-server.conf
install -m 0644 -vp -D %{SOURCE3} %{buildroot}/%{_sysusersdir}/go-fdo-server-manufacturer.conf
install -m 0644 -vp -D %{SOURCE4} %{buildroot}/%{_sysusersdir}/go-fdo-server-rendezvous.conf
install -m 0644 -vp -D %{SOURCE5} %{buildroot}/%{_sysusersdir}/go-fdo-server-owner.conf
install -m 0755 -vd %{buildroot}%{_unitdir}
install -m 0644 -vp -D init/systemd/* %{buildroot}%{_unitdir}
install -m 0755 -vd %{buildroot}%{_libexecdir}/%{name}
install -m 0755 -vp scripts/cert-utils.sh %{buildroot}%{_libexecdir}/%{name}
install -m 0755 -vp scripts/generate-go-fdo-server-certs.sh %{buildroot}%{_libexecdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with check}
%gotest ./...
%endif
%pre

%sysusers_create_compat %{SOURCE2}
%package manufacturer
Requires: go-fdo-server
Requires: group(go-fdo-server)
Requires: openssl
Summary: A Go implementation of the FDO manufacturer server
BuildArch: noarch
%description manufacturer
This package provides the manufacturer server component of the FDO stack.
The manufacturer server is responsible for creating ownership vouchers and
preparing devices for the on-boarding process during the manufacturing phase.

%pre manufacturer

%sysusers_create_compat %{SOURCE3}
%post manufacturer

%systemd_post go-fdo-server-manufacturer.service
%preun manufacturer

%systemd_preun go-fdo-server-manufacturer.service
%postun manufacturer

%systemd_postun_with_restart go-fdo-server-manufacturer.service
%package rendezvous
Requires: go-fdo-server
Requires: group(go-fdo-server)
Summary: A Go implementation of the FDO rendezvous server
BuildArch: noarch
%description rendezvous
This package provides the rendezvous server component of the FDO stack.
The rendezvous server acts as a trusted intermediary, redirecting devices
to their designated owner's on-boarding service based on their ownership
voucher.

%pre rendezvous

%sysusers_create_compat %{SOURCE4}
%post rendezvous

%systemd_post go-fdo-server-rendezvous.service
%preun rendezvous

%systemd_preun go-fdo-server-rendezvous.service
%postun rendezvous

%systemd_postun_with_restart go-fdo-server-rendezvous.service
%package owner
Requires: go-fdo-server
Requires: group(go-fdo-server)
Summary: A Go implementation of the FDO owner server
BuildArch: noarch
%description owner
This package provides the owner server component of the FDO stack. The owner
server is the final destination for a device during on-boarding. It verifies
the device's authenticity, establishes ownership, and provisions it with the
necessary credentials and configuration for operation.

%pre owner

%sysusers_create_compat %{SOURCE5}
%post owner

%systemd_post go-fdo-server-owner.service
%preun owner

%systemd_preun go-fdo-server-owner.service
%postun owner

%systemd_postun_with_restart go-fdo-server-owner.service
%files -f %{oreon_filedir}/main.list
%files -n go-fdo-server-manufacturer -f %{oreon_filedir}/go-fdo-server-manufacturer.list
%files -n go-fdo-server-rendezvous -f %{oreon_filedir}/go-fdo-server-rendezvous.list
%files -n go-fdo-server-owner -f %{oreon_filedir}/go-fdo-server-owner.list

%changelog

%autochangelog
