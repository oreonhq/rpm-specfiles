%global source0_hash none
%global source10_hash 34a96eb96b319c64f3cc49e0b3a0ae5a1a0a041aab9adea027ab51875f2b2e83

%global _hardened_build 1
%global clknetsim_ver 6ee99f50dec8
%bcond_without debug
%bcond_without nts

%ifarch %{ix86} x86_64 %{arm} aarch64 mipsel mips64el ppc64 ppc64le s390 s390x
%bcond_without seccomp
%endif

Name:           chrony
Version:        4.8
Release:        6%{?dist}
Summary:        An NTP client/server

License:        GPL-2.0-only
URL:            https://chrony-project.org
Source0:        https://chrony-project.org/releases/chrony-4.8%{?prerelease}.tar.gz
Source1:        https://chrony-project.org/releases/chrony-4.8%{?prerelease}-tar-gz-asc.txt
Source2:        https://chrony-project.org/gpgkey-8F375C7E8D0EE125A3D3BD51537E2B76F7680DAC.asc
Source3:        chrony.dhclient
Source4:        chrony.sysusers
# simulator for test suite (pinned commit, reproducible tree name)
Source10:        https://gitlab.com/chrony/clknetsim/-/archive/6ee99f50dec8/clknetsim-6ee99f50dec8.tar.gz
%{?gitpatch:Patch0: chrony-%{version}%{?prerelease}-%{gitpatch}.patch.gz}

# add distribution-specific bits to DHCP dispatcher
Patch1:         chrony-nm-dispatcher-dhcp.patch
# let systemd create /var/lib/chrony and /var/log/chrony
Patch2:         chrony-servicedirs.patch
# update seccomp filter for new glibc
Patch3:         chrony-seccomp.patch

BuildRequires:  libcap-devel libedit-devel nettle-devel pps-tools-devel
BuildRequires:  gcc gcc-c++ make bison systemd gnupg2
%{?with_nts:BuildRequires: gnutls-devel gnutls-utils}
%{?with_seccomp:BuildRequires: libseccomp-devel}

%{?systemd_requires}
%{?sysusers_requires_compat}

# Needed by the leapseclist directive in default chrony.conf
Requires:       tzdata

# suggest drivers for hardware reference clocks
Suggests:       ntp-refclock

%description
chrony is a versatile implementation of the Network Time Protocol (NTP).
It can synchronise the system clock with NTP servers, reference clocks
(e.g. GPS receiver), and manual input using wristwatch and keyboard. It
can also operate as an NTPv4 (RFC 5905) server and peer to provide a time
service to other computers in the network.

%if 0%{!?vendorzone:1}
%global vendorzone %(source /etc/os-release && echo ${ID}.)
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source10_hash}" = "none" || { f="%{SOURCE10}"; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source10_hash}" || { echo "oreon: Source10 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%setup -q -n %{name}-%{version}%{?prerelease} -a 10
%{?gitpatch:%patch -P 0 -p1}
%patch -P 1 -p1 -b .nm-dispatcher-dhcp
%patch -P 2 -p1 -b .servicedirs
%patch -P 3 -p1 -b .seccomp

%{?gitpatch: echo %{version}-%{gitpatch} > version.txt}

# review changes in packaged configuration files and scripts
md5sum -c <<-EOF | (! grep -v 'OK$')
        5530d6e60f84b76c27495485d2510bac  examples/chrony-wait.service
        3f2ddca6065c3e8f4565d7422739795a  examples/chrony.conf.example2
        6a3178c4670de7de393d9365e2793740  examples/chrony.logrotate
        c3992e2f985550739cd1cd95f98c9548  examples/chrony.nm-dispatcher.dhcp
        4e85d36595727318535af3387411070c  examples/chrony.nm-dispatcher.onoffline
        607c82f56639486f52c31105632909eb  examples/chronyd.service
        5ddbb8a8055f587cb6b0b462ca73ea46  examples/chronyd-restricted.service
EOF

# don't allow packaging without vendor zone
test -n "%{vendorzone}"

# use example chrony.conf as the default config with some modifications:
# - use our vendor zone (2.*pool.ntp.org names include IPv6 addresses)
# - enable leapseclist to get TAI-UTC offset and leap seconds
# - use NTP servers from DHCP
sed -e 's|^\(pool \)\(pool.ntp.org\)|\12.%{vendorzone}\2|' \
    -e 's|#\(leapseclist\)|\1|' \
    -e 's|^pool.*pool.ntp.org.*|&\n\n# Use NTP servers from DHCP.\nsourcedir /run/chrony-dhcp|' \
        < examples/chrony.conf.example2 > chrony.conf

touch -r examples/chrony.conf.example2 chrony.conf

# set selinux context in chronyd-restricted service
sed -i '/^ExecStart/a SELinuxContext=system_u:system_r:chronyd_restricted_t:s0' \
	examples/chronyd-restricted.service

# regenerate the file from getdate.y
rm -f getdate.c

# GitLab top dir is clknetsim-<ref> or clknetsim-<sha>, not always *-<sha> after another segment.
clknetsim_src=$(find . -maxdepth 1 -mindepth 1 -type d -name 'clknetsim-*' -print -quit)
test -n "$clknetsim_src" || { echo 'clknetsim: no directory after %%setup -a 10'; ls -la; exit 1; }
mv "$clknetsim_src" test/simulation/clknetsim

%build
%configure \
%{?with_debug: --enable-debug} \
        --enable-ntp-signd \
%{?with_seccomp: --enable-scfilter} \
%{!?with_nts: --disable-nts} \
        --chronyrundir=/run/chrony \
        --docdir=%{_docdir} \
        --with-ntp-era=$(date -d '1970-01-01 00:00:00+00:00' +'%s') \
        --with-chronyc-user=chrony \
        --with-user=chrony \
        --with-hwclockfile=%{_sysconfdir}/adjtime \
        --with-pidfile=/run/chrony/chronyd.pid \
        --with-sendmail=%{_sbindir}/sendmail
%make_build

%install
%make_install

rm -rf $RPM_BUILD_ROOT%{_docdir}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{sysconfig,logrotate.d}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/{lib,log}/chrony
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dhcp/dhclient.d
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mkdir -p $RPM_BUILD_ROOT%{_sysusersdir}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/NetworkManager/dispatcher.d
mkdir -p $RPM_BUILD_ROOT{%{_unitdir},%{_prefix}/lib/systemd/ntp-units.d}

install -m 644 -p chrony.conf $RPM_BUILD_ROOT%{_sysconfdir}/chrony.conf

install -m 755 -p %{SOURCE3} \
        $RPM_BUILD_ROOT%{_sysconfdir}/dhcp/dhclient.d/chrony.sh
install -m 644 -p examples/chrony.logrotate \
        $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/chrony

install -m 644 -p examples/chronyd.service \
        $RPM_BUILD_ROOT%{_unitdir}/chronyd.service
install -m 644 -p examples/chronyd-restricted.service \
        $RPM_BUILD_ROOT%{_unitdir}/chronyd-restricted.service
install -m 755 -p examples/chrony.nm-dispatcher.onoffline \
        $RPM_BUILD_ROOT%{_prefix}/lib/NetworkManager/dispatcher.d/20-chrony-onoffline
install -m 755 -p examples/chrony.nm-dispatcher.dhcp \
        $RPM_BUILD_ROOT%{_prefix}/lib/NetworkManager/dispatcher.d/20-chrony-dhcp
install -m 644 -p examples/chrony-wait.service \
        $RPM_BUILD_ROOT%{_unitdir}/chrony-wait.service
install -m 644 -p %{SOURCE4} \
        $RPM_BUILD_ROOT%{_sysusersdir}/chrony.conf

cat > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/chronyd <<EOF
# Command-line options for chronyd
OPTIONS="%{?with_seccomp:-F 2}"
EOF

touch $RPM_BUILD_ROOT%{_sysconfdir}/chrony.keys
touch $RPM_BUILD_ROOT%{_localstatedir}/lib/chrony/{drift,rtc}

echo 'chronyd.service' > \
        $RPM_BUILD_ROOT%{_prefix}/lib/systemd/ntp-units.d/50-chronyd.list

%check
# set random seed to get deterministic results
export CLKNETSIM_RANDOM_SEED=24508
%make_build -C test/simulation/clknetsim
make quickcheck

%pre
%sysusers_create_compat %{SOURCE4}

%post
# migrate from chrony-helper to sourcedir directive
if test -a %{_libexecdir}/chrony-helper; then
        grep -qi 'sourcedir /run/chrony-dhcp$' %{_sysconfdir}/chrony.conf 2> /dev/null || \
                echo -e '\n# Use NTP servers from DHCP.\nsourcedir /run/chrony-dhcp' >> \
                        %{_sysconfdir}/chrony.conf
        mkdir -p /run/chrony-dhcp
        for f in %{_localstatedir}/lib/dhclient/chrony.servers.*; do
                sed 's|.*|server &|' < $f > /run/chrony-dhcp/"${f##*servers.}.sources"
        done 2> /dev/null
fi
%systemd_post chronyd.service chronyd-restricted.service chrony-wait.service

%preun
%systemd_preun chronyd.service chronyd-restricted.service chrony-wait.service

%postun
%systemd_postun_with_restart chronyd.service chronyd-restricted.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc FAQ NEWS README examples/chrony.keys.example
%config(noreplace) %{_sysconfdir}/chrony.conf
%ghost %config %attr(640,root,chrony) %{_sysconfdir}/chrony.keys
%config(noreplace) %{_sysconfdir}/logrotate.d/chrony
%config(noreplace) %{_sysconfdir}/sysconfig/chronyd
%{_sysconfdir}/dhcp/dhclient.d/chrony.sh
%{_bindir}/chronyc
%{_sbindir}/chronyd
%{_prefix}/lib/NetworkManager
%{_prefix}/lib/systemd/ntp-units.d/*.list
%{_unitdir}/chrony*.service
%{_sysusersdir}/chrony.conf
%{_mandir}/man[158]/%{name}*.[158]*
%ghost %dir %attr(750,chrony,chrony) %{_localstatedir}/lib/chrony
%ghost %attr(-,chrony,chrony) %{_localstatedir}/lib/chrony/drift
%ghost %attr(-,chrony,chrony) %{_localstatedir}/lib/chrony/rtc
%ghost %dir %attr(750,chrony,chrony) %{_localstatedir}/log/chrony

%changelog
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.8-6
- clknetsim: robust unpack path, pin GitLab archive to %%{clknetsim_ver} (fix %%prep mv on aarch64)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.8-5
- Prepare for Oreon 11 (RP1)
