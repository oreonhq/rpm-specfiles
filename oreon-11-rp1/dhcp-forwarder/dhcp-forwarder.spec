%global source0_hash 72dc290ac1d228b450ddab0a61c308b8ebeff806f00e6b1c0828da3a8e97aa6e

Summary: DHCP relay agent
Name: dhcp-forwarder
Version: 0.11
Release: 27%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL: http://www.nongnu.org/dhcp-fwd/
Source0: http://savannah.nongnu.org/download/dhcp-fwd/%name-%version.tar.xz
Source1: http://savannah.nongnu.org/download/dhcp-fwd/%name-%version.tar.xz.asc
Source2: dhcp-forwarder.service

BuildRequires:  gcc
BuildRequires: systemd-units
BuildRequires: make
Requires(post): coreutils bash systemd
Requires(preun): systemd
Requires(postun): systemd

# required to update the old packages which had init system sub packages
Obsoletes: dhcp-forwarder-systemd

%description
dhcp-fwd forwards DHCP messages between subnets with different sublayer
broadcast domains. It is similar to the DHCP relay agent dhcrelay of
ISC's DHCP, but has the following important features:

* Runs as non-root in a chroot-environment
* Uses AF_INET sockets which makes it possible to filter incoming
  messages with packetfilters
* The DHCP agent IDs can be defined freely
* Has a small memory footprint when using dietlibc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Create a sysusers.d config file
cat >dhcp-forwarder.sysusers.conf <<EOF
u dhcp-fwd - 'DHCP Forwarder user' %{_sharedstatedir}/dhcp-fwd -
EOF

%build
%configure \
 --enable-release \
 --with-systemd-unitdir=%_unitdir \
 --disable-dietlibc

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

install -d %{buildroot}/%{_sharedstatedir}/dhcp-fwd \
 %{buildroot}/%{_unitdir} %{buildroot}/%{_sysconfdir}
make DESTDIR=%{buildroot} install
install %{SOURCE2} %{buildroot}/%{_unitdir}/dhcp-forwarder.service
install contrib/dhcp-fwd.conf %{buildroot}/%{_sysconfdir}

install -m0644 -D dhcp-forwarder.sysusers.conf %{buildroot}%{_sysusersdir}/dhcp-forwarder.conf

%check
make check

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %attr(0755,root,root) %{_sharedstatedir}/dhcp-fwd
%_sbindir/*
%_mandir/*/*
%attr(0644,root,root) %{_unitdir}/dhcp-forwarder.service
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/dhcp-fwd.conf
%{_sysusersdir}/dhcp-forwarder.conf

%post
%systemd_post dhcp-forwarder.service

%preun
%systemd_preun dhcp-forwarder.service

%postun
%systemd_postun_with_restart dhcp-forwarder.service

%changelog
%autochangelog
