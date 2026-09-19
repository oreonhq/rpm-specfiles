%global source0_hash 8665f0caf5aba5d55730c0eaed62f174cc93659f9dff3bd5895907759e54883e

%global _hardened_build 1

# Upstream moved to github
%global forgeurl https://github.com/apalrd/tayga
%global	date 20250731
%global commit fb5c58f16adc79d1bda31b103b15fd8d55e7083f
%forgemeta

# tayga no longer builds cleanly on 32bit
ExcludeArch: %{ix86}

Name:		tayga
Version:	0.9.6
Release:	0.3%{?dist}
Summary:	Simple, no-fuss NAT64

License:	GPL-2.0-or-later
URL:		%{forgeurl}
Source0:	%{forgesource}
source1:	tayga.tmpfilesd.conf

Requires:	iproute

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	coreutils
BuildRequires:	systemd-units

%description
TAYGA is an out-of-kernel stateless NAT64 implementation for Linux that uses
the TUN driver to exchange IPv4 and IPv6 packets with the kernel. It is
intended to provide production-quality NAT64 service for networks where
dedicated NAT64 hardware would be overkill.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

echo Building %{forgesource} > /dev/null
%forgesetup
sed -i '
	s,setcap,#setcap,;
	s,\$(sysconfdir)/systemd/system,%{_unitdir},g;
	s,daemon-reload,--version,;
' Makefile

%build
%make_build CFLAGS="%{optflags}"

%check
%make_build test CFLAGS="%{optflags} -Wno-error=unused-but-set-variable -Wno-error=discarded-qualifiers"

%install
rm -rf %{buildroot}
%make_install prefix=%{_prefix} sbindir=%{_sbindir}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
install -p -D -m 0644 %SOURCE1 %{buildroot}%{_tmpfilesdir}/%{name}.conf

# Install a default unit
sed -i 's,%i,default,g' scripts/tayga@.service
install -p -D -m 0644 scripts/tayga@.service %{buildroot}/%{_unitdir}/%{name}.service

%post
%tmpfiles_create_package %{name} %{name}.tmpfilesd.conf
%systemd_post %{name}

%preun
%systemd_preun %{name}@.service

%files
%config(noreplace) %{_sysconfdir}/%{name}/default.conf
%doc README.md
%license LICENSE
%{_sbindir}/%{name}
%{_mandir}/*/*
%{_sharedstatedir}/%{name}
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf

%changelog
%autochangelog
