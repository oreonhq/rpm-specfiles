%global source0_hash 5e6ff6a22cf92ba73ebf2e4bbcd9360328b52c7497ef70e4cf11089fa5a216b2

%global _hardened_build 1

Name:             bird
Version:          3.2.0
Release:          3%{?dist}
Summary:          BIRD Internet Routing Daemon

License:          GPL-2.0-or-later
URL:              https://bird.nic.cz/
Source0:          https://bird.nic.cz/download/bird-%{version}.tar.gz
Source1:          bird.service
Source2:          bird.tmpfilesd
Source3:          bird.sysusersd

BuildRequires:    flex
BuildRequires:    bison
BuildRequires:    ncurses-devel
BuildRequires:    readline-devel
BuildRequires:    sed
BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    libssh-devel
BuildRequires:    systemd-rpm-macros
%{?systemd_requires}
%{?sysusers_requires_compat}

Obsoletes:        bird-sysvinit
Obsoletes:        bird6 < 2.0.2-1
Provides:         bird6 = %{version}-%{release}

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

%files
%doc NEWS README
%attr(0640,root,bird) %config(noreplace) %{_sysconfdir}/bird.conf
%{_unitdir}/bird.service
%{_sysusersdir}/bird.conf
%{_tmpfilesdir}/bird.conf
%{_sbindir}/bird
%{_sbindir}/birdc
%{_sbindir}/birdcl
%dir %attr(0750,bird,bird) %{_localstatedir}/lib/bird
%dir %attr(0750,bird,bird) %{_rundir}/bird

%if 0%{!?_without_doc:1}
%files doc
%doc NEWS README
%doc doc/bird.conf.*
%doc obj/doc/bird*.html
%doc obj/doc/bird.pdf
%doc obj/doc/prog*.html
%doc obj/doc/prog.pdf
%endif

%changelog
%autochangelog
