%global source0_hash e097c4f351a26f1de5339212d9e10d4cf5abc4b8105e4f1c488ef065a903f615

%if 0%{?with_snapshot}
%global gitdate              20220915
%global portable_commit      3f638e16a67691a3f11d5e745e545df531af92c3
%global portable_shortcommit %(c=%{portable_commit}; echo ${c:0:7})
%global openbsd_commit       43b3801c4cc6d22976048c9d833346a4f42bee72
%global openbsd_shortcommit  %(c=%{openbsd_commit}; echo ${c:0:7})
%endif

Summary:        OpenBGPD Routing Daemon
Name:           openbgpd
Version:        9.0
Release:        2%{?with_snapshot:.git%{gitdate}}%{?dist}
# OpenBGPD itself is ISC but uses other source codes, breakdown:
# BSD-2-Clause: include/sys/tree.h
# BSD-3-Clause: compat/{fmt_scaled,setproctitle,sha2,vis}.c and include/{sha2_openbsd,util,vis,sys/queue}.h
# LicenseRef-Fedora-Public-Domain: include/{{endian,sha2,stdlib,string,unistd},net/if,netinet/{in,ip_ipsp}}.h
#                                  and include/sys/{_null,socket,time,types,wait}.h
#                                  and compat/{{explicit_bzero,getrtable}.c,chacha_private.h}
License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://www.openbgpd.org/
%if !0%{?with_snapshot}
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenBGPD/%{name}-%{version}.tar.gz
Source1:        https://ftp.openbsd.org/pub/OpenBSD/OpenBGPD/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/BA3DA14FEE657A6D7931C08EC755429BA6A969A8
%else
Source0:        https://github.com/openbgpd-portable/openbgpd-portable/archive/%{portable_commit}/%{name}-portable-%{version}-%{portable_shortcommit}.tar.gz
Source1:        https://github.com/openbgpd-portable/openbgpd-openbsd/archive/%{openbsd_commit}/%{name}-openbsd-%{version}-%{openbsd_shortcommit}.tar.gz
%endif
Source3:        openbgpd.service
Source4:        openbgpd.tmpfilesd
Source5:        openbgpd.sysusersd
# Adjust path of Validated ROA Payloads (VRP) for rpki-client
Patch0:         openbgpd-6.7p0-rpki-client.patch
%if !0%{?with_snapshot}
BuildRequires:  gnupg2
%else
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  bison
%endif
BuildRequires:  gcc
BuildRequires:  libmnl-devel >= 1.0.4
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
Recommends:     rpki-client
%{?systemd_requires}
%{?sysusers_requires_compat}

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
# Workaround until autoconf generated './configure' supports '--runstatedir=/run/bgpd' option
sed -e 's|^\(runstatedir =\).*|\1 %{_rundir}/bgpd|g' -i {.,compat,include,src/{bgpctl,bgpd,bgplgd}}/Makefile
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir},%{_localstatedir}/empty,%{_rundir}}/bgpd/
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/bgpd.service
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_compat %{SOURCE5}

%post
%systemd_post bgpd.service

%preun
%systemd_preun bgpd.service

%postun
%systemd_postun_with_restart bgpd.service

%files
%license LICENSE
%doc AUTHORS README.md
%config(noreplace) %attr(0640,root,bgpd) %{_sysconfdir}/bgpd.conf
%dir %attr(0750,root,bgpd) %{_sysconfdir}/bgpd/
%{_unitdir}/bgpd.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_sbindir}/bgpctl
%{_sbindir}/bgpd
%{_mandir}/man5/bgpd.conf.5*
%{_mandir}/man8/bgpctl.8*
%{_mandir}/man8/bgpd.8*
%dir %attr(0755,root,root) %{_rundir}/bgpd/
%dir %attr(0711,root,root) %{_localstatedir}/empty/bgpd/

%changelog
%autochangelog
