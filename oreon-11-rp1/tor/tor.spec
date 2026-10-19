%global source2_hash 6cf4145742311615cbc239d5bc16ad390dabe88ad5283c78777b83078c36b73d
%global source1_hash f73bd4c5499e1de3ca528d92eb28d47cae6b2a405d524b370818116d724f4f8d
%global source0_hash c0d307c9dcdaee4848a8ca53e9d6c4ec92823e4f30be12790b0fbddfc6515f5b
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
Version:    0.4.9.12
Release:        1%{?dist}
License:    BSD-3-Clause
Summary:        Anonymizing overlay network for TCP
URL:        https://www.torproject.org
Source0:        https://www.torproject.org/dist/tor-%{version}.tar.gz
Source1:    https://www.torproject.org/dist/tor-%{version}.tar.gz.sha256sum
Source2:    https://www.torproject.org/dist/tor-%{version}.tar.gz.sha256sum.asc
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
%{?sysusers_requires_compat}
%if 0%{with libseccomp}
%endif
Requires:         torsocks
Requires(pre):    shadow-utils
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcap-devel
BuildRequires:  libevent-devel
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
rm -rf %{buildroot}%{_datadir}/doc
%oreon_autofiles main

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
