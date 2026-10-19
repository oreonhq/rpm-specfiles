%global source0_hash 08e23937e16d0155e55cab2b51f51fbe10d80a1aa91c4e15442645059b737ef6
%global _hardened_build 1
%bcond_with gui
Summary:        WPA/WPA2/IEEE 802.1X Supplicant
Name: wpa_supplicant
Epoch: 1
Version: 2.12
Release:        1%{?dist}
License: BSD-3-Clause
Source0:        http://w1.fi/releases/%{name}-%{version}.tar.gz
Source1: wpa_supplicant.conf
Source2: wpa_supplicant.service
Source3: wpa_supplicant.sysconfig
Source4: wpa_supplicant.logrotate
Patch0: wpa_supplicant-defconfig-keep-options-we-ve-traditionally-used-enab.patch
Patch1: wpa_supplicant-assoc-timeout.patch
Patch2: wpa_supplicant-flush-debug-output.patch
Patch3: wpa_supplicant-quiet-scan-results-message.patch
Patch4: wpa_supplicant-gui-qt4.patch
Patch6: wpa_supplicant-defconfig-keep-CONFIG_WEP-enabled.patch
Patch7: wpa_supplicant-defconfig-enable-WPA-EAP-SUITE-B-192-ciphers.patch
Patch8: wpa_supplicant-defconfig-enable-OCV-support.patch
Patch9: wpa_supplicant-allow-legacy-renegotiation.patch
Patch10: wpa_supplicant-Revert-Mark-authorization-completed-on-driver-indica.patch
URL: http://w1.fi/wpa_supplicant/
%if %with gui
%endif
Requires(post): systemd-sysv
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Obsoletes: libeap < %{epoch}:%{version}-%{release}
Obsoletes: libeap-devel < %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  libnl3-devel
BuildRequires:  openssl-devel
BuildRequires:  qt-devel
BuildRequires:  readline-devel
BuildRequires:  systemd-units
# /oreon:deps
%description
wpa_supplicant is a WPA Supplicant for Linux, BSD and Windows with support
for WPA and WPA2 (IEEE 802.11i / RSN). Supplicant is the IEEE 802.1X/WPA
component that is used in the client stations. It implements key negotiation
with a WPA Authenticator and it controls the roaming and IEEE 802.11
authentication/association of the wlan driver.

%if %with gui
%package gui
Summary: Graphical User Interface for %{name}
%description gui
Graphical User Interface for wpa_supplicant written using QT
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

pushd wpa_supplicant
  cp defconfig .config
  export CFLAGS="${CFLAGS:-%optflags} -fPIE -DPIE"
  export CXXFLAGS="${CXXFLAGS:-%optflags} -fPIE -DPIE"
  export LDFLAGS="${LDFLAGS:-%optflags} -pie -Wl,-z,now"
  export BINDIR="%{_sbindir}"
  export LIBDIR="%{_libdir}"
  make %{_smp_mflags} V=1
%if %with gui
  make wpa_gui-qt4 %{_smp_mflags} V=1 QTDIR=%{_libdir}/qt4 \
    QMAKE='%{qmake_qt4}' LRELEASE='%{_qt4_bindir}/lrelease'
%endif
  make eapol_test V=1
  make -C doc/docbook man V=1
%if !%with gui
  rm doc/docbook/wpa_gui.8
%endif
popd
%install
install -D -m 0600 %{SOURCE1} %{buildroot}/%{_sysconfdir}/wpa_supplicant/wpa_supplicant.conf
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_unitdir}/wpa_supplicant.service
install -D -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysconfig/wpa_supplicant
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/logrotate.d/wpa_supplicant
install -d %{buildroot}/%{_sbindir}
install -m 0755 wpa_supplicant/wpa_passphrase %{buildroot}/%{_sbindir}
install -m 0755 wpa_supplicant/wpa_cli %{buildroot}/%{_sbindir}
install -m 0755 wpa_supplicant/wpa_supplicant %{buildroot}/%{_sbindir}
install -m 0755 wpa_supplicant/eapol_test %{buildroot}/%{_sbindir}
install -D -m 0644 wpa_supplicant/dbus/dbus-wpa_supplicant.conf \
  %{buildroot}/%{_datadir}/dbus-1/system.d/wpa_supplicant.conf
install -D -m 0644 wpa_supplicant/dbus/fi.w1.wpa_supplicant1.service \
  %{buildroot}/%{_datadir}/dbus-1/system-services/fi.w1.wpa_supplicant1.service
%if %with gui
install -d %{buildroot}/%{_bindir}
install -m 0755 wpa_supplicant/wpa_gui-qt4/wpa_gui %{buildroot}/%{_bindir}
%endif
install -d %{buildroot}%{_mandir}/man{5,8}
install -m 0644 wpa_supplicant/doc/docbook/*.8 %{buildroot}%{_mandir}/man8
install -m 0644 wpa_supplicant/doc/docbook/*.5 %{buildroot}%{_mandir}/man5
rm -f  wpa_supplicant/doc/.cvsignore
rm -rf wpa_supplicant/doc/docbook
chmod -R 0644 wpa_supplicant/examples/*.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post wpa_supplicant.service
%preun

%systemd_preun wpa_supplicant.service
%triggerun -- wpa_supplicant < 0.7.3-10

/usr/bin/systemd-sysv-convert --save wpa_supplicant >/dev/null 2>&1 ||:
/sbin/chkconfig --del wpa_supplicant >/dev/null 2>&1 || :
/bin/systemctl try-restart wpa_supplicant.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list
%files -n wpa_supplicant-gui -f %{oreon_filedir}/wpa_supplicant-gui.list

%changelog

%autochangelog
