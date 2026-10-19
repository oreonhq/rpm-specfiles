%global source0_hash 21297d7a02edd700ae82de5a630055a9cb88a99e2e7e45551bc7d6c1e5b4de2c
%global _hardened_build 1
Name:             bird
Version:          3.3.2
Release:        1%{?dist}
Summary:        BIRD Internet Routing Daemon
License:          GPL-2.0-or-later
URL:              https://bird.nic.cz/
Source0:        https://bird.nic.cz/download/bird-%{version}.tar.gz
Source1:          bird.service
Source2:          bird.tmpfilesd
Source3:          bird.sysusersd
%{?systemd_requires}
%{?sysusers_requires_compat}
Obsoletes:        bird-sysvinit
Obsoletes:        bird6 < 2.0.2-1
Provides:         bird6 = %{version}-%{release}
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libssh-devel
BuildRequires:  linuxdoc-tools
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl(FindBin)
BuildRequires:  readline-devel
BuildRequires:  sed
BuildRequires:  sgml-common
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
BIRD is a dynamic IP routing daemon supporting both, IPv4 and IPv6, Border
Gateway Protocol (BGPv4), Routing Information Protocol (RIPv2, RIPng), Open
Shortest Path First protocol (OSPFv2, OSPFv3), Babel Routing Protocol (Babel),
Bidirectional Forwarding Detection (BFD), IPv6 router advertisements, static
routes, inter-table protocol, command-line interface allowing on-line control
and inspection of the status of the daemon, soft reconfiguration as well as a
powerful language for route filtering.

%if 0%{!?_without_doc:1}
%package doc
Summary:          Documentation for BIRD Internet Routing Daemon
BuildRequires:    linuxdoc-tools sgml-common perl(FindBin)
BuildArch:        noarch
%description doc
Documentation for users and programmers of the BIRD Internet Routing Daemon.

BIRD is a dynamic IP routing daemon supporting both, IPv4 and IPv6, Border
Gateway Protocol (BGPv4), Routing Information Protocol (RIPv2, RIPng), Open
Shortest Path First protocol (OSPFv2, OSPFv3), Babel Routing Protocol (Babel),
Bidirectional Forwarding Detection (BFD), IPv6 router advertisements, static
routes, inter-table protocol, command-line interface allowing on-line control
and inspection of the status of the daemon, soft reconfiguration as well as a
powerful language for route filtering.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --runstatedir=%{_rundir}/bird
%make_build all %{!?_without_doc:docs}
%install
%make_install
install -d %{buildroot}{%{_localstatedir}/lib/bird,%{_rundir}/bird}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/bird.service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/bird.conf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/bird.conf
%oreon_autofiles bird-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%pre

%sysusers_create_compat %{SOURCE3}
%post

%systemd_post bird.service
%preun

%systemd_preun bird.service
%postun

%systemd_postun_with_restart bird.service
%files -f %{oreon_filedir}/main.list
%files -n bird-doc -f %{oreon_filedir}/bird-doc.list

%changelog

%autochangelog
