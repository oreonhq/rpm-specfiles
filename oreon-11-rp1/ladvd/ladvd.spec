%global source0_hash e9ec66c817de80de5b0ae8bd361aa678ae033a6ab5d84c880c0ca09f799f4894

%define selinux_variants mls strict targeted
%define modulename ladvd

Name:           ladvd
Version:        1.1.4
Release:        4%{?dist}
Summary:        CDP/LLDP sender for UNIX

License:        ISC
URL:            http://www.blinkenlights.nl/software/ladvd/
Source0:        https://github.com/sspans/ladvd/archive/v%{version}.tar.gz
Source1:        %{name}.conf.sysusers
# 2016-11 TODO: rewrite selinux policy using CIL
Source3:        %{modulename}.te
Source4:        %{modulename}.fc
Source5:        %{modulename}.if

Recommends:	%{name}-selinux

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libevent-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libpcap-devel
BuildRequires:  libteam-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  pkgconfig
BuildRequires:  systemd

%{?systemd_requires}

%description
ladvd uses CDP / LLDP frames to inform switches about connected hosts, which
simplifies Ethernet switch management. Every 30 seconds it will transmit CDP/
LLDP packets reflecting the current system state. Interfaces (bridge, bonding,
wireless), capabilities (bridging, forwarding, wireless) and addresses (IPv4,
IPv6) are detected dynamically.

%package selinux
Summary:        SELinux policy module supporting %{name}
BuildRequires:  checkpolicy, selinux-policy-devel, hardlink
%if "%{_selinux_policy_version}" != ""
Requires:       selinux-policy >= %{_selinux_policy_version}
%endif
Requires:       %{name} = %{version}-%{release}
Requires(post):   /usr/sbin/semodule, /sbin/restorecon
Requires(postun): /usr/sbin/semodule, /sbin/restorecon

%description selinux
SELinux policy module supporting %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
mkdir SELinux
cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} SELinux

%build
autoreconf -fi
%configure \
        --with-user=ladvd \
        --with-pid-dir=%{_rundir}
make %{?_smp_mflags}

cd SELinux
for selinuxvariant in %{selinux_variants}
do
make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
mv %{modulename}.pp %{modulename}.pp.${selinuxvariant}
make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_docdir}/ladvd
mkdir -p %{buildroot}%{_unitdir}
install -m 0444 -D %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

cd SELinux
for selinuxvariant in %{selinux_variants}
do
install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
install -p -m 644 %{modulename}.pp.${selinuxvariant} \
%{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp
done
cd -

/usr/bin/hardlink -cv %{buildroot}%{_datadir}/selinux

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%post selinux
for selinuxvariant in %{selinux_variants}
do
/usr/sbin/semodule -s ${selinuxvariant} -i \
%{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp &> /dev/null || :
done

%postun selinux
if [ $1 -eq 0 ] ; then
for selinuxvariant in %{selinux_variants}
do
/usr/sbin/semodule -s ${selinuxvariant} -r %{modulename} &> /dev/null || :
done
fi

%files
%doc doc/README doc/TODO
%license doc/LICENSE
%{_sbindir}/%{name}
%{_sbindir}/%{name}c
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}c.8*
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf

%files selinux
%doc SELinux/*
%{_datadir}/selinux/*/%{modulename}.pp

%changelog
%autochangelog
