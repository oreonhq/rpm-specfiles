%global source0_hash 5180dfd9a7d3d0633a027b0a04f01b45a6a64623813cd48bd54423b90814864e

Summary: Daemon that responds to network cables being plugged in and out
Name: netplug
Version: 1.2.9.2
Release: 31%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://www.red-bean.com/~bos/
Source0: http://www.red-bean.com/~bos/netplug/netplug-%{version}.tar.bz2
Source1: netplugd.service

#execshield patch for netplug <t8m@redhat.com>
Patch1: netplug-1.2.9.2-execshield.patch

Patch2: netplug-1.2.9.2-man.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: systemd
BuildRequires: gettext

Requires: iproute
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Netplug is a daemon that manages network interfaces in response to
link-level events such as cables being plugged in and out.  When a
cable is plugged into an interface, the netplug daemon brings that
interface up.  When the cable is unplugged, the daemon brings that
interface back down.

This is extremely useful for systems such as laptops, which are
constantly being unplugged from one network and plugged into another,
and for moving systems in a machine room from one switch to another
without a need for manual intervention.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .execshield
%patch -P2 -p1 -b .man

%build
export CFLAGS="$RPM_OPT_FLAGS $CFLAGS"
make

%install
make install prefix=%{buildroot} \
             bindir=%{buildroot}/%{_sbindir} \
             mandir=%{buildroot}/%{_mandir}

mkdir -p %{buildroot}/%{_mandir}/man5
ln -fs %{_mandir}/man8/netplugd.8.gz %{buildroot}/%{_mandir}/man5/netplug.5.gz
ln -fs %{_mandir}/man8/netplugd.8.gz %{buildroot}/%{_mandir}/man5/netplug.d.5.gz
ln -fs %{_mandir}/man8/netplugd.8.gz %{buildroot}/%{_mandir}/man5/netplugd.conf.5.gz

# systemd unit files
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}

rm -f %{buildroot}/etc/rc.d/init.d/netplugd

%post
%systemd_post netplugd.service

%preun
%systemd_preun netplugd.service
 
%postun
%systemd_postun_with_restart netplugd.service

%files
%doc COPYING README TODO
%{_sbindir}/netplugd
%{_mandir}/man[58]/*
%dir %{_sysconfdir}/netplug.d
%{_sysconfdir}/netplug.d/netplug
%config(noreplace) %{_sysconfdir}/netplug.d/netplugd.conf
%{_unitdir}/netplugd.service

%changelog
%autochangelog
