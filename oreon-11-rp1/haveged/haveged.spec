%global source0_hash b835fa02b52ee7d06276e028571cadcb14d08f5e5a4b5767adf81451f70561c7

%define dracutlibdir lib/dracut
Summary:        A Linux entropy source using the HAVEGE algorithm
Name:           haveged
Version:        1.9.18
Release:        11%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/jirka-h/haveged
Source0:        https://github.com/jirka-h/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

BuildRequires:  gcc
BuildRequires:  make automake coreutils glibc-common systemd-units
Enhances:       apache2 gpg2 openssl openvpn php5 smtp_daemon systemd

%description
A Linux entropy source using the HAVEGE algorithm

Haveged is a user space entropy daemon which is not dependent upon the
standard mechanisms for harvesting randomness for the system entropy
pool. This is important in systems with high entropy needs or limited
user interaction (e.g. headless servers).

Haveged uses HAVEGE (HArdware Volatile Entropy Gathering and Expansion)
to maintain a 1M pool of random bytes used to fill /dev/random
whenever the supply of random bits in /dev/random falls below the low
water mark of the device. The principle inputs to haveged are the
sizes of the processor instruction and data caches used to setup the
HAVEGE collector. The haveged default is a 4kb data cache and a 16kb
instruction cache. On machines with a cpuid instruction, haveged will
attempt to select appropriate values from internal tables.

%package devel
Summary:   Headers and shared development libraries for HAVEGE algorithm
Requires:  %{name} = %{version}-%{release}

%description devel
Headers and shared object symbolic links for the HAVEGE algorithm

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
#autoreconf -fiv
%configure --disable-enttest --enable-nistest --disable-static
#SMP build is not working
#make %{?_smp_mflags}
make

%check
make check

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

chmod 0644 COPYING README ChangeLog AUTHORS

#Install systemd service file
sed -e 's:@SBIN_DIR@:%{_sbindir}:g' -i contrib/Fedora/*service
sed -i '/^ConditionKernelVersion/d' contrib/Fedora/*service

install -Dpm 0644 contrib/Fedora/haveged.service %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 contrib/Fedora/haveged-switch-root.service %{buildroot}%{_unitdir}/%{name}-switch-root.service
install -Dpm 0644 contrib/Fedora/haveged-once.service %{buildroot}%{_unitdir}/%{name}-once.service
install -Dpm 0755 contrib/Fedora/haveged-dracut.module %{buildroot}/%{_prefix}/%{dracutlibdir}/modules.d/98%{name}/module-setup.sh
install -Dpm 0644 contrib/Fedora/90-haveged.rules %{buildroot}%{_udevrulesdir}/90-%{name}.rules

# We don't ship .la files.
rm -rf %{buildroot}%{_libdir}/libhavege.*a

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp -p COPYING README ChangeLog AUTHORS contrib/build/havege_sample.c %{buildroot}%{_defaultdocdir}/%{name}

%post
/sbin/ldconfig
%systemd_post %{name}.service %{name}-switch-root.service

%preun
%systemd_preun %{name}.service %{name}-switch-root.service

%postun
%systemd_postun_with_restart %{name}.service %{name}-switch-root.service
/sbin/ldconfig

%files
%{_mandir}/man8/haveged.8*
%{_sbindir}/haveged
%{_unitdir}/*.service
%{_libdir}/*so.*
%{_defaultdocdir}/*
%{_udevrulesdir}/*-%{name}.rules
%dir %{_prefix}/%{dracutlibdir}/modules.d/98%{name}
%{_prefix}/%{dracutlibdir}/modules.d/98%{name}/*

%files devel
%{_mandir}/man3/libhavege.3*
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/havege.h
%doc contrib/build/havege_sample.c
%{_libdir}/*.so

%changelog
%autochangelog
