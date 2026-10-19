%global source0_hash 7ead7a89e7aaa059d20e34042c58a198c2981cad729550d1388ddfc9036d3983
Name:                   nuttcp
Version:                8.2.2
Release:        1%{?dist}
Source0:        http://nuttcp.net/nuttcp/%{name}-%{version}.tar.bz2
URL:                    http://nuttcp.net/
Summary:        Tool for testing TCP connections
License:                GPL-2.0-or-later
Requires(post):         systemd-units
Requires(preun):        systemd-units
Requires(postun):       systemd-units
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
nuttcp is a network performance measurement tool intended for use by
network and system managers.  Its most basic usage is to determine the
raw TCP (or UDP) network layer throughput by transferring memory buffers
from a source system across an interconnecting network to a destination
system, either transferring data for a specified time interval, or
alternatively transferring a specified number of buffers.  In addition
to reporting the achieved network throughput in Mbps, nuttcp also
provides additional useful information related to the data transfer
such as user, system, and wall-clock time, transmitter and receiver
CPU utilization, and loss percentage (for UDP transfers).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build CFLAGS="$RPM_OPT_FLAGS"
%install
mkdir -p %{buildroot}{%{_mandir}/man8,%{_bindir},%{_sysconfdir}/xinetd.d}
install -m755 %{name}-%{version} %{buildroot}%{_bindir}/%{name}
install -pm644 %{name}.8 %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_unitdir}
install -m644 systemd/* %{buildroot}%{_unitdir}
%oreon_autofiles main

%post

%systemd_post %{name}@.service
%preun

%systemd_preun %{name}@.service
%postun

%systemd_postun_with_restart %{name}@.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
