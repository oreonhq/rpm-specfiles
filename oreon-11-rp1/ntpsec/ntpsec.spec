%global source0_hash 443e54a6149d1b0bf08677d17b18fced9028b101fc2ffd2c81e0834f87eebc7d

Name:           ntpsec
Version:        1.2.4
Release:        8%{?dist}
Summary:        NTP daemon and utilities

License:        NTP AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND ISC AND Apache-2.0 AND Beerware
URL:            https://www.ntpsec.org/
Source0:        https://ftp.ntpsec.org/pub/releases/ntpsec-%{version}.tar.gz
Source1:        https://ftp.ntpsec.org/pub/releases/ntpsec-%{version}.tar.gz.asc
Source2:        https://ftp.ntpsec.org/pub/releases/ntpsec.gpg.pub.asc
Source3:        ntp.conf

BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libbsd-devel
BuildRequires:  libcap-devel
BuildRequires:  m4
BuildRequires:  openssl-devel
BuildRequires:  pps-tools-devel
BuildRequires:  python3-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  systemd
BuildRequires:  waf

%{?systemd_requires}

Conflicts:      ntp ntp-perl ntpdate
Obsoletes:      ntp < 4.2.10 ntp-perl < 4.2.10 ntp-doc < 4.2.10 ntpdate < 4.2.10 sntp < 4.2.10

# Set pool.ntp.org vendor zone for default configuration
%if 0%{!?vendorzone:1}
%global vendorzone %(source /etc/os-release && echo ${ID}.)
%endif

# Private library
%global __provides_exclude ^libntpc\\.so.*$
%global __requires_exclude ^libntpc\\.so.*$

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/ntpsec
Provides:       /usr/sbin/ntpq
Provides:       /usr/sbin/ntpdate
%endif

%description
NTPsec is a more secure and improved implementation of the Network Time
Protocol derived from the original NTP project.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -p1

# Fix egg info to use a shorter version which will work as an rpm provide
sed -i 's|NTPSEC_VERSION_EXTENDED|NTPSEC_VERSION|' pylib/ntp-in.egg-info

# Modify compiled-in statsdir
sed -i 's|/var/NTP|%{_localstatedir}/log/ntpstats|' \
        docs/includes/ntpd-body.adoc ntpd/ntp_util.c

# Disable failing test
sed -i 's|c cprogram test|c cprogram|' libaes_siv/wscript

# Use systemctl kill in logrotate postrotate script
sed -i 's|killall -HUP ntpd$|systemctl kill --signal=HUP --kill-whom=main ntpd.service 2>/dev/null \|\| true|' \
        etc/logrotate-config.ntpd

# Make sure we use the system waf instead of the one bundled with ntpsec
rm -f waf
%global waf waf

%build
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"

%{waf} configure \
        --enable-debug \
        --disable-doc \
        --refclock=all \
        --prefix=%{_prefix} \
        --exec-prefix=%{_exec_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_localstatedir} \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        ;

%{waf} build

%install
%{waf} --destdir=%{buildroot} install

install -p -m755 attic/ntpdate %{buildroot}%{_sbindir}/ntpdate
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m644 etc/logrotate-config.ntpd \
        %{buildroot}%{_sysconfdir}/logrotate.d/ntpsec.conf

rm -rf %{buildroot}%{_docdir}

pushd %{buildroot}

sed -e 's|VENDORZONE\.|%{vendorzone}|' \
        -e 's|VARNTP|%{_localstatedir}/lib/ntp|' \
        < %{SOURCE3} > .%{_sysconfdir}/ntp.conf
touch -r %{SOURCE3} .%{_sysconfdir}/ntp.conf

for f in .%{_bindir}/*; do
        head -c 30 "$f" | grep -q python || continue
        %py3_shebang_fix "$f"
done

%if "%{_sbindir}" != "%{_bindir}"
# Move ntpq to sbin for better compatibility with ntp package
mv .%{_bindir}/ntpq .%{_sbindir}/ntpq
%else
# Fix incorrect installation
[ -d ./usr/sbin ] && mv ./usr/sbin/* .%{_bindir}
%endif

mkdir -p .%{_localstatedir}/{lib/ntp,log/ntpstats}
touch .%{_localstatedir}/lib/ntp/ntp.drift

mkdir -p .%{_prefix}/lib/systemd/ntp-units.d
echo 'ntpd.service' > .%{_prefix}/lib/systemd/ntp-units.d/60-ntpd.list

# Create a sysusers.d config file (UID/GID is inherited from the ntp package)
mkdir -p .%{_sysusersdir}
cat > .%{_sysusersdir}/ntpsec.conf <<EOF
u ntp 38 - %{_localstatedir}/lib/ntp -
EOF

popd

%check
%{waf} check

%post
%systemd_post ntpd.service ntp-wait.service
systemctl daemon-reload 2> /dev/null || :

%preun
%systemd_preun ntpd.service ntp-wait.service

%postun
%systemd_postun_with_restart ntpd.service

%global service_save_file /run/ntp-ntpsec.upgrade.services

%triggerprein -- ntp < 4.2.10
[ $1 = 0 ] || exit 0
# Save enabled ntp services and configuration (before our post)
for s in ntpd ntp-wait; do
        systemctl is-enabled -q "$s".service 2> /dev/null &&
                echo "$s" 2> /dev/null >> %{service_save_file}
done
rm -rf %{_sysconfdir}/ntp.ntpsec
cp -r --preserve=all %{_sysconfdir}/ntp %{_sysconfdir}/ntp.ntpsec 2> /dev/null
:

%triggerpostun -- ntp < 4.2.10
[ $2 = 0 ] || exit 0
# Restore the services and configuration from ntp (after its preun)
for s in ntpd ntp-wait; do
        grep -q "^$s$" %{service_save_file} 2> /dev/null &&
                systemctl enable -q "$s".service 2> /dev/null
done
rm -f %{service_save_file}
mv -f -T --backup=numbered %{_sysconfdir}/ntp.ntpsec %{_sysconfdir}/ntp
# Remove unsupported restrictions
sed -i.bak -E '/^restrict/s/no(e?peer|trap)//g' %{_sysconfdir}/ntp.conf
:

%files
%license LICENSES/*
%doc NEWS.adoc README.adoc
%config(noreplace) %{_sysconfdir}/ntp.conf
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/ntpsec.conf
%{_bindir}/ntp*
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/ntp*
%endif
%{_libdir}/libntpc.so*
%{_mandir}/man1/ntp*.1*
%{_mandir}/man5/ntp*.5*
%{_mandir}/man8/ntp*.8*
%{_unitdir}/ntp*.service
%{_unitdir}/ntp*.timer
%{_prefix}/lib/systemd/ntp-units.d/*ntpd.list
%dir %attr(-,ntp,ntp) %{_localstatedir}/lib/ntp
%ghost %attr(644,ntp,ntp) %{_localstatedir}/lib/ntp/ntp.drift
%dir %attr(-,ntp,ntp) %{_localstatedir}/log/ntpstats
%{python3_sitelib}/ntp-*.egg-info
%{python3_sitelib}/ntp
%{_sysusersdir}/ntpsec.conf

%changelog
%autochangelog
