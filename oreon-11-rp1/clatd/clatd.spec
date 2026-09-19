%global source0_hash fd171a7820215c2eaa950b81815c04d032cdcab619e8b5093198e96cdaefb4b0

%global forgeurl https://github.com/toreanderson/clatd

Name:		clatd
Version:	2.1.0
Release:	5%{?dist}
Summary:	CLAT / SIIT-DC Edge Relay implementation for Linux

License:	MIT
URL:		https://github.com/toreanderson/clatd
VCS:		git:%{forgeurl}
Source0:	%{forgeurl}/archive/refs/tags/v%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	coreutils
BuildRequires:	%{_bindir}/pod2man

Requires:	iproute
Requires:	iptables
Requires:	tayga
Requires:	perl-interpreter
Requires:	perl(Net::DNS)
Requires:	perl(IO::Socket::IP)
Requires:	perl(File::Temp)
Requires:	perl(Net::IP)
Requires:       perl(IPC::Cmd)

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd

%description
clatd implements the CLAT component of the 464XLAT network architecture
specified in RFC 6877. It allows an IPv6-only host to have IPv4
connectivity that is translated to IPv6 before being routed to an upstream
PLAT (which is typically a Stateful NAT64 operated by the ISP) and there
translated back to IPv4 before being routed to the IPv4 internet.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q v%{release}.tar.gz

# Unified sbin/bin from fedora 42
%if 0%{?fedora} > 41
sed -i 's/sbin/bin/' Makefile
%endif
sed -i 's,(SYSCONFDIR)/NetworkManager,(PREFIX)/lib/NetworkManager,g' Makefile
sed -i "s,%{_sbindir}/clatd,%{_sbindir}/clatd -c %{_sysconfdir}/%{name}.conf," scripts/*

%build
echo -e '# Default clatd.conf\n# See clatd(8) for a list of config directives' > %{name}.conf

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d

%make_install

install -p -D -m0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
install -p -D -m0644 scripts/%{name}.systemd %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%files
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_prefix}/lib/NetworkManager/dispatcher.d/50-clatd
%doc README.pod
%{_mandir}/man8/*.8*
%license LICENCE
%{_unitdir}/%{name}.service

# Unfortunately, there is no NetworkManager subpackage providing these
%dir %{_prefix}/lib/NetworkManager
%dir %{_prefix}/lib/NetworkManager/dispatcher.d

%changelog
%autochangelog
