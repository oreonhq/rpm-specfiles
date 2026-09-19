%global source0_hash 3f880349cbe4c8e27f02d276b2d3318e6b721cad6c0ab2ba8e2c1768251fd494

Name: soundmodem
Version: 0.20
Release: 38%{?dist}
Summary: Soundcard Packet Radio Modem
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://gna.org/projects/soundmodem
Source: http://download.gna.org/soundmodem/%{name}-%{version}.tar.gz
Source1: soundmodem.service
Patch1: %{name}-0.16-dirfix.patch
#fixes security error caused by non-void return in void function
#as function seems used we silently drop it to avoid reusing it.
Patch2: %{name}-0.20-void.patch
Patch3: %{name}-0.20-i386-fix.patch
Patch4: %{name}-0.20-gcc10-fix.patch
Patch5: soundmodem-hamlib42.patch
Patch6: soundmodem-0.20-sighandler.patch
ExcludeArch:   i686
# Requires: /sbin/ifconfig /sbin/route /sbin/arp
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: gtk2-devel
BuildRequires: alsa-lib-devel
BuildRequires: libxml2-devel
BuildRequires: audiofile-devel
BuildRequires: hamlib-devel
BuildRequires:  systemd
%{?systemd_requires}

%description
This package contains the driver and the diagnostic utility for
userspace SoundModem. It allows you to use soundcards
as Amateur Packet Radio modems.

%package devel

Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%if "%version" < "0.20"
# Versions prior to 0.20 are not c11 compiliant
# Work-around by fallin back to -std=gnu89
%configure CFLAGS="${RPM_OPT_FLAGS} -std=gnu89"
%else
# Versions >= 0.20 seem to be c11 compliant
%configure
%endif
make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/ax25
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/soundmodem.service
mkdir -p %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/modem.h %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/simd.h %{buildroot}%{_includedir}/%{name}
%find_lang %{name}

%post
%systemd_post soundmodem.service

%preun
%systemd_preun soundmodem.service

%postun
%systemd_postun_with_restart soundmodem.service

%files -f %{name}.lang
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/*/*
%{_unitdir}/soundmodem.service
%doc AUTHORS ChangeLog NEWS README newqpsk/README.newqpsk
%license COPYING

%files devel
%{_includedir}/%{name}

%changelog
%autochangelog
