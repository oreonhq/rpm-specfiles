%global source0_hash f93043ba4ca22f7d495cf86f6311923b67d5e153607dc7634a8b12409de1b114

%global ntp_version 4.2.8p18

Name:		ntp-refclock
Version:	0.7
Release:	3%{?dist}
Summary:	Drivers for hardware reference clocks
License:	BSD-2-Clause AND NTP AND BSD-3-Clause AND BSD-4-Clause AND Beerware
URL:		https://github.com/mlichvar/ntp-refclock
Source0:	https://github.com/mlichvar/ntp-refclock/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	https://downloads.nwtime.org/ntp/4.2.8/ntp-%{ntp_version}.tar.gz
Patch0:		ntp-refclock-configure-c99.patch
Patch1:		ntp-refclock-md5cast.patch

BuildRequires:	gcc make systemd pps-tools-devel

Requires:	udev
%{?systemd_requires}

# The drivers and some code they need are from ntp
Provides:	bundled(ntp) = %{ntp_version}

%description
ntp-refclock is a wrapper for reference clock drivers included in the ntpd
daemon, which enables other NTP implementations to use the supported hardware
reference clocks for synchronization of the system clock.

It provides a minimal environment for the drivers to be able to run in a
separate process, measuring the offset of the system clock relative to the
reference clock and sending the measurements to another process controlling
the system clock.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1
ln -s ntp-%{ntp_version} ntp
# Avoid re-generating the configure scripts.
pushd ntp
preserve_timestamps="configure configure.ac sntp/configure sntp/m4/ntp_ipv6.m4"
for p in $preserve_timestamps ; do
    touch -r $p $p.timestamp
done
%patch -P0 -p1 -b .c99
%patch -P1 -p1 -b .md5cast
for p in $preserve_timestamps ; do
    touch -r $p.timestamp $p
    rm $p.timestamp
done
popd

# Refer to packaged documentation for drivers
sed -i 's|<https:.*refclock.html>|in %{_pkgdocdir}/drivers/|' ntp-refclock.8

# Create a sysusers.d config file
cat >ntp-refclock.sysusers.conf <<EOF
u ntp-refclock - 'Reference clock driver' - -
EOF

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fno-strict-overflow"

pushd ntp

%configure \
	--enable-all-clocks \
	--enable-parse-clocks \
	--disable-ATOM \
	--disable-LOCAL-CLOCK \
	--without-crypto \
	--without-threads \
	--without-sntp

sed -i 's/-Werror=format-security//g' sntp/libopts/Makefile

# Build only objects that may be linked with ntp-refclock
%make_build -C libntp
%make_build -C libparse
%make_build -C sntp/libopts
%make_build -C ntpd

popd

%make_build \
	CFLAGS="$RPM_OPT_FLAGS" \
	LDFLAGS="$RPM_LD_FLAGS" \
	DEFAULT_USER=%{name} \
	DEFAULT_ROOTDIR=/usr/share/empty

%install
%make_install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{sysconfig,udev/rules.d}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -m 644 -p examples/ntp-refclock.sysconfig \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/ntp-refclock
install -m 644 -p examples/ntp-refclock.rules \
	$RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/80-ntp-refclock.rules
install -m 644 -p examples/ntp-refclock.service \
	$RPM_BUILD_ROOT%{_unitdir}/ntp-refclock.service
install -m 644 -p examples/pps-ldattach@.service \
	$RPM_BUILD_ROOT%{_unitdir}/pps-ldattach@.service
install -m 644 -D ntp-refclock.sysusers.conf \
	$RPM_BUILD_ROOT%{_sysusersdir}/ntp-refclock.conf

%post
%systemd_post ntp-refclock.service

%preun
%systemd_preun ntp-refclock.service

%postun
%systemd_postun_with_restart ntp-refclock.service

%files
%license COPYRIGHT*
%doc README NEWS ntp/html/drivers
%config(noreplace) %{_sysconfdir}/sysconfig/ntp-refclock
%config(noreplace) %{_sysconfdir}/udev/rules.d/80-ntp-refclock.rules
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_unitdir}/*.service
%{_sysusersdir}/ntp-refclock.conf

%changelog
%autochangelog
