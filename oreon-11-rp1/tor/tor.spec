%global source0_hash c949c2f86b348e64891976f6b1e49c177655b23df97193049bf1b8cd3099e179

%global _hardened_build 1

%global toruser     toranon
%global torgroup    toranon
%global homedir     %{_localstatedir}/lib/tor
%global logdir      %{_localstatedir}/log/tor
%global rundir      /run/tor

%ifarch %{ix86} x86_64 aarch64
%bcond_without libseccomp
%else
%bcond_with libseccomp
%endif

Name:       tor
Version:    0.4.9.5
Release:    1%{?dist}
License:    BSD-3-Clause
Summary:    Anonymizing overlay network for TCP
URL:        https://www.torproject.org

Source0:    https://www.torproject.org/dist/tor-%{version}.tar.gz
Source1:    https://www.torproject.org/dist/tor-%{version}.tar.gz.sha256sum
Source2:    https://www.torproject.org/dist/tor-%{version}.tar.gz.sha256sum.asc
# gpg --export --export-options export-minimal,export-clean -a 514102454D0A87DB0767A1EBBE6A0531C18A9179 B74417EDDF22AC9F9E90F49142E86A2A11F48D36  > ./tor-keyring.pub
Source5:    tor-keyring.pub
Source6:    tor.logrotate
Source7:    tor.defaults-torrc
Source8:    tor.tmpfiles.d
Source10:   tor.service
Source11:   tor@.service
Source12:   tor-master.service
Source20:   README
Source30:   tor.sysusers

Patch0:     tor-0.4.8.4-torrc-ControlSocket-and-CookieAuthFile.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: libevent-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
BuildRequires: xz-devel
BuildRequires: libcap-devel
BuildRequires: gnupg2
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros
%{?sysusers_requires_compat}
%if 0%{?fedora} >= 41
# https://gitlab.torproject.org/tpo/core/tor/-/issues/40166#note_3055852
# https://bugzilla.redhat.com/show_bug.cgi?id=2301334
BuildRequires: openssl-devel-engine
%endif

%if 0%{with libseccomp}
# Only available on certain architectures.
BuildRequires:    libseccomp-devel
%endif

# /usr/bin/torify is now just a wrapper for torsocks and is only there for
# backwards compatibility.
Requires:         torsocks
Requires(pre):    shadow-utils

%description
The Tor network is a group of volunteer-operated servers that allows people to
improve their privacy and security on the Internet. Tor's users employ this
network by connecting through a series of virtual tunnels rather than making a
direct connection, thus allowing both organizations and individuals to share
information over public networks without compromising their privacy. Along the
same line, Tor is an effective censorship circumvention tool, allowing its
users to reach otherwise blocked destinations or content. Tor can also be used
as a building block for software developers to create new communication tools
with built-in privacy features.

This package contains the Tor software that can act as either a server on the
Tor network, or as a client to connect to the Tor network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

echo "$(cat %{SOURCE1} | cut -d ' ' -f 1) %{SOURCE0}" | sha256sum --check
%{gpgverify} --keyring='%{SOURCE5}' --signature='%{SOURCE2}' --data='%{SOURCE1}'
%autosetup -p1

%build
%configure --with-tor-user=%{toruser} --with-tor-group=%{torgroup} --enable-gpl
%make_build

%install
%make_install
mv %{buildroot}%{_sysconfdir}/tor/torrc.sample \
    %{buildroot}%{_sysconfdir}/tor/torrc

mkdir -p %{buildroot}%{_sysconfdir}/tor/torrc.d/
sed -i 's@^#%include /etc/torrc.d/\*.conf@%include /etc/tor/torrc.d/*.conf@' %{buildroot}%{_sysconfdir}/tor/torrc

install -D -p -m 0644 %{SOURCE20} %{buildroot}%{_sysconfdir}/tor/README

mkdir -p %{buildroot}%{logdir}
mkdir -p %{buildroot}%{homedir}
mkdir -p %{buildroot}%{rundir}

install -D -p -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/tor.service
install -D -p -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/tor@.service
install -D -p -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/tor-master.service
install -D -p -m 0644 %{SOURCE6}  %{buildroot}%{_sysconfdir}/logrotate.d/tor
install -D -p -m 0644 %{SOURCE7}  %{buildroot}%{_datadir}/tor/defaults-torrc
install -D -p -m 0644 %{SOURCE8}  %{buildroot}%{_tmpfilesdir}/tor.conf

install -p -D -m 0644 %{SOURCE30} %{buildroot}%{_sysusersdir}/tor.conf

# Install docs manually.
rm -rf %{buildroot}%{_datadir}/doc

%pre
%sysusers_create_compat %{SOURCE30}

%post
%systemd_post tor.service

%preun
%systemd_preun tor.service
%systemd_preun tor-master.service

%postun
%systemd_postun_with_restart tor.service
%systemd_postun_with_restart tor-master.service

%files
%doc README.md ChangeLog ReleaseNotes doc/HACKING doc/man/*.html
%license LICENSE
%{_bindir}/tor
%{_bindir}/tor-gencert
%{_bindir}/tor-resolve
%{_bindir}/torify
%{_bindir}/tor-print-ed-signing-cert
%{_mandir}/man1/tor.1*
%{_mandir}/man1/tor-gencert.1*
%{_mandir}/man1/tor-resolve.1*
%{_mandir}/man1/torify.1*
%{_mandir}/man1/tor-print-ed-signing-cert.1*
%dir %{_datadir}/tor
%{_datadir}/tor/defaults-torrc
%{_datadir}/tor/geoip
%{_datadir}/tor/geoip6
%{_tmpfilesdir}/tor.conf
%{_unitdir}/tor.service
%{_unitdir}/tor@.service
%{_unitdir}/tor-master.service

%dir %{_sysconfdir}/tor
%dir %{_sysconfdir}/tor/torrc.d
%{_sysconfdir}/tor/README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/tor/torrc
%config(noreplace) %{_sysconfdir}/logrotate.d/tor

%attr(0750,%{toruser},root) %dir %{homedir}
%attr(0750,%{toruser},%{torgroup}) %dir %{logdir}
%attr(0750,%{toruser},%{torgroup}) %dir %{rundir}

%{_sysusersdir}/tor.conf

%changelog
%autochangelog
