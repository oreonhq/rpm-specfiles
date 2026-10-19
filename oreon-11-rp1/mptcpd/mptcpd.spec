%global source0_hash 34810a09d167370c64b5766687b2eb4f6d3f7a1ab33ee71d821cdac819552be1
%bcond check 0
Summary:        Multipath TCP daemon
Name: mptcpd
Version: 0.14
Release:        1%{?dist}
License: GPL-2.0-or-later AND BSD-3-Clause
URL: https://multipath-tcp.org
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Source0:        https://github.com/multipath-tcp/mptcpd/archive/v%{version}/%{name}-%{version}.tar.gz#/mptcpd-0.14.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-g++
BuildRequires:  libell-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-units
# /oreon:deps
%description
The Multipath TCP Daemon is a daemon for Linux based operating systems that
performs multipath TCP path management related operations in user space. It
interacts with the Linux kernel through a generic netlink connection to track
per-connection information (e.g. available remote addresses), available network
interfaces, request new MPTCP subflows, handle requests for subflows, etc.

%package devel
Summary: MPTCP path manager header files
Group: Development/Libraries
Requires: pkgconfig
Requires: %{name}%{?_isa} = %{version}-%{release}
License: BSD-3-Clause
%description devel
Header files for adding MPTCP path manager support to applications

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf --install --symlink --force
%configure --enable-debug=info
%make_build V=1
%check

%if %{with check}
make check
%endif
%install
install -d %{buildroot}/%{_libexecdir}
install -d %{buildroot}/%{_mandir}/man8
install -d %{buildroot}/%{_sysconfdir}/%{name}
install -d %{buildroot}/%{_unitdir}
install -d %{buildroot}/%{_libdir}/%{name}
install -d %{buildroot}/%{_includedir}/%{name}
%make_install
sed -i '/^# addr-flags=subflow/s/^# //g' %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf
sed -i '/^# notify-flags=existing,skip_link_local,skip_loopback/s/^# //g' %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%systemd_postun mptcp.service
%files -f %{oreon_filedir}/main.list
%files -n mptcpd-devel -f %{oreon_filedir}/mptcpd-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14-1
- Import
