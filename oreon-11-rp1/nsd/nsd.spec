%global source0_hash 5d60e344002a9cc609ab71951a3cdb906314999e42f2a269044f27259ac2f12e
%global _hardened_build 1
Summary:        Fast and lean authoritative DNS Name Server
Name: nsd
Version: 4.14.0
Release:        1%{?dist}
License: BSD-3-Clause
Url: http://www.nlnetlabs.nl/nsd/
Source0:        http://www.nlnetlabs.nl/downloads/%{name}/%{name}-%{version}.tar.gz
Source1: nsd.conf
Source2: nsd.service
Source3: tmpfiles-nsd.conf
Source4: nsd.sysusers.conf
# oreon:deps
BuildRequires:  flex
BuildRequires:  fstrm-devel
BuildRequires:  gcc
BuildRequires:  libevent-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  protobuf-c-compiler
BuildRequires:  protobuf-c-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
NSD is a complete implementation of an authoritative DNS name server.
For further information about what NSD is and what NSD is not please
consult the REQUIREMENTS document which is a part of this distribution.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?prever}

%build

CFLAGS="%{optflags} -fPIE -pie"
LDFLAGS="-Wl,-z,relro,-z,now"
export CFLAGS LDFLAGS
%configure \
    --enable-bind8-stats \
    --enable-zone-stats \
    --enable-checking \
    --enable-nsec3 \
    --with-pidfile="" \
    --with-zonelistfile=%{_sharedstatedir}/nsd/zone.list \
    --with-ssl \
    --with-user=nsd \
    --with-xfrdfile=%{_sharedstatedir}/nsd/ixfr.state \
    --with-dbfile="" \
    --enable-ratelimit \
    --enable-pie \
    --enable-relro-now \
    --enable-recvmmsg \
    --enable-packed \
    --enable-memclean \
    --enable-systemd
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/nsd.conf
mkdir -p %{buildroot}%{_rundir}/nsd
mkdir -p %{buildroot}%{_sharedstatedir}/nsd
install -m 0644 -D %{SOURCE4} %{buildroot}%{_sysusersdir}/nsd.conf
for name in control server; do
    for extension in key pem; do
        touch %{buildroot}%{_sysconfdir}/nsd/nsd_${name}.${extension}
    done
done
mkdir -p %{buildroot}%{_sysconfdir}/nsd/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/nsd/server.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nsd/nsd.conf
rm %{buildroot}%{_sysconfdir}/nsd/nsd.conf.sample
%oreon_autofiles main

%post

%systemd_post nsd.service
%preun

%systemd_preun nsd.service
%postun

%systemd_postun_with_restart nsd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
