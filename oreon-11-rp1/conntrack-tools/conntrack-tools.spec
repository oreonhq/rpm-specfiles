%global source0_hash c15afe488a8d408c9d6d61e97dbd19f3c591942f62c13df6453a961ca4231cae
%global source1_hash e8fa3185f1c39aadf2e3d5c2bb4a644335c2a18356410c57c49dfa4961e53097
Name:           conntrack-tools
Version:        1.4.9
Release:        1%{?dist}
Summary:        Manipulate netfilter connection tracking table and run High Availability
License:        GPL-2.0-only
URL:            http://conntrack-tools.netfilter.org/
Source0:        https://www.netfilter.org/pub/conntrack-tools/conntrack-tools-%{version}.tar.xz
Source1:        https://www.netfilter.org/pub/conntrack-tools/conntrack-tools-%{version}.tar.xz.sig
Source2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt
Source3:        conntrackd.service
Source4:        conntrackd.conf
Provides:       conntrack = 1.0-1
Obsoletes:      conntrack < 1.0-1
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libmnl-devel
BuildRequires:  libnetfilter_conntrack-devel
BuildRequires:  libnetfilter_cthelper-devel
BuildRequires:  libnetfilter_cttimeout-devel
BuildRequires:  libnetfilter_queue-devel
BuildRequires:  libnfnetlink-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
%description
With conntrack-tools you can setup a High Availability cluster and
synchronize conntrack state between multiple firewalls.

The conntrack-tools package contains two programs:
- conntrack: the command line interface to interact with the connection
             tracking system.
- conntrackd: the connection tracking userspace daemon that can be used to
              deploy highly available GNU/Linux firewalls and collect
              statistics of the firewall use.

conntrack is used to search, list, inspect and maintain the netfilter
connection tracking subsystem of the Linux kernel.
Using conntrack, you can dump a list of all (or a filtered selection  of)
currently tracked connections, delete connections from the state table,
and even add new ones.
In addition, you can also monitor connection tracking events, e.g.
show an event message (one line) per newly established connection.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

autoreconf -fi
%configure --disable-static --enable-systemd
%make_build
chmod 644 doc/sync/primary-backup.sh
rm -f doc/sync/notrack/conntrackd.conf.orig doc/sync/alarm/conntrackd.conf.orig doc/helper/conntrackd.conf.orig
%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
mkdir -p %{buildroot}%{_sysconfdir}/conntrackd
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/conntrackd/
%oreon_autofiles main

%post

%systemd_post conntrackd.service
%preun

%systemd_preun conntrackd.service
%postun

%systemd_postun conntrackd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
