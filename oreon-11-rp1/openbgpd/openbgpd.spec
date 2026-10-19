%global source2_hash 7c3a4b6b2d32bb813e841a7aee9fdcf2f8c8a9fec6ea3e50844ee4f794925085
%global source1_hash ad5ee9bbb1a98039a6172dac841b2a251142646625f3ad92bdb2fd6890497a7c
%global source0_hash 4e21ab5f478efc898640966a9115d9b6be42fabe114ea600dc9c22cf4e0f03aa
%if 0%{?with_snapshot}
%global gitdate              20220915
%global portable_commit      3f638e16a67691a3f11d5e745e545df531af92c3
%global portable_shortcommit %(c=%{portable_commit}; echo ${c:0:7})
%global openbsd_commit       43b3801c4cc6d22976048c9d833346a4f42bee72
%global openbsd_shortcommit  %(c=%{openbsd_commit}; echo ${c:0:7})
%endif
Summary:        OpenBGPD Routing Daemon
Name:           openbgpd
Version:        9.2
Release:        1%{?dist}
License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://www.openbgpd.org/
%if !0%{?with_snapshot}
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenBGPD/%{name}-%{version}.tar.gz
Source1:        https://ftp.openbsd.org/pub/OpenBSD/OpenBGPD/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/BA3DA14FEE657A6D7931C08EC755429BA6A969A8
%else
Source1:        https://github.com/openbgpd-portable/openbgpd-openbsd/archive/%{openbsd_commit}/%{name}-openbsd-%{version}-%{openbsd_shortcommit}.tar.gz
%endif
Source3:        openbgpd.service
Source4:        openbgpd.tmpfilesd
Source5:        openbgpd.sysusersd
Patch0:         openbgpd-6.7p0-rpki-client.patch
%if !0%{?with_snapshot}
%else
%endif
Recommends:     rpki-client
%{?systemd_requires}
%{?sysusers_requires_compat}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libmnl-devel
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
OpenBGPD is a free implementation of the Border Gateway Protocol (BGP),
Version 4. It allows ordinary machines to be used as routers exchanging
routes with other systems speaking the BGP protocol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if !0%{?with_snapshot}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%else
%setup -q -n %{name}-portable-%{portable_commit}
tar xfz %{SOURCE1}
mv -f %{name}-openbsd-%{openbsd_commit} openbsd
./autogen.sh
%endif
%patch -P0 -p1 -b .rpki-client
touch -c -r bgpd.conf{.rpki-client,}

%build

%configure --with-privsep-user=bgpd --disable-bgplgd
sed -e 's|^\(runstatedir =\).*|\1 %{_rundir}/bgpd|g' -i {.,compat,include,src/{bgpctl,bgpd,bgplgd}}/Makefile
%make_build
%install
%make_install
mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir},%{_localstatedir}/empty,%{_rundir}}/bgpd/
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/bgpd.service
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
%oreon_autofiles main

%pre

%sysusers_create_compat %{SOURCE5}
%post

%systemd_post bgpd.service
%preun

%systemd_preun bgpd.service
%postun

%systemd_postun_with_restart bgpd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
