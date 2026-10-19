%global source0_hash 5180dfd9a7d3d0633a027b0a04f01b45a6a64623813cd48bd54423b90814864e
Summary:        Daemon that responds to network cables being plugged in and out
Name: netplug
Version: 1.2.9.2
Release:        1%{?dist}
License: GPL-2.0-only
URL: http://www.red-bean.com/~bos/
Source0:        http://www.red-bean.com/~bos/netplug/netplug-%{version}.tar.bz2
Source1: netplugd.service
Patch1: netplug-1.2.9.2-execshield.patch
Patch2: netplug-1.2.9.2-man.patch
Requires: iproute
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
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
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
rm -f %{buildroot}/etc/rc.d/init.d/netplugd
%oreon_autofiles main

%post

%systemd_post netplugd.service
%preun

%systemd_preun netplugd.service
%postun

%systemd_postun_with_restart netplugd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
