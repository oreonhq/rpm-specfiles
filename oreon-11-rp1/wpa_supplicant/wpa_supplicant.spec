# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 912ea06f74e30a8e36fbb68064d6cdff218d8d591db0fc5d75dee6c81ac7fc0a
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global _hardened_build 1
%if 0%{?fedora}
%bcond_without gui
%else
%bcond_with gui
%endif

Summary: WPA/WPA2/IEEE 802.1X Supplicant
Name: wpa_supplicant
Epoch: 1
Version: 2.11
Release: 10%{?dist}
License: BSD-3-Clause
Source0: http://w1.fi/releases/%{name}-%{version}.tar.gz
Source1: wpa_supplicant.conf
Source2: wpa_supplicant.service
Source3: wpa_supplicant.sysconfig
Source4: wpa_supplicant.logrotate

# Distro specific customization and not suitable for upstream,
# Fedora-specific updates to defconfig
Patch0: wpa_supplicant-defconfig-keep-options-we-ve-traditionally-used-enab.patch
# Works around busted drivers
Patch1: wpa_supplicant-assoc-timeout.patch
# Ensures that debug output gets flushed immediately to help diagnose driver
# bugs, not suitable for upstream
Patch2: wpa_supplicant-flush-debug-output.patch
# Quiet an annoying and frequent syslog message
Patch3: wpa_supplicant-quiet-scan-results-message.patch
# Distro specific customization for Qt4 build tools, not suitable for upstream
Patch4: wpa_supplicant-gui-qt4.patch
# We keep WEP enabled for now to avoid breaking user setups
Patch6: wpa_supplicant-defconfig-keep-CONFIG_WEP-enabled.patch
# FIXME: Explain why are these two here
Patch7: wpa_supplicant-defconfig-enable-WPA-EAP-SUITE-B-192-ciphers.patch
Patch8: wpa_supplicant-defconfig-enable-OCV-support.patch
# Allow legacy renegotiation with openssl 3.0 to fix connection to
# PEAP/Radius servers that don't support secure renegotiation:
# https://bugzilla.redhat.com/show_bug.cgi?id=2072070
# From James Ralston in comment #24, thanks to James
Patch9: wpa_supplicant-allow-legacy-renegotiation.patch
# Revert 41638606054 ("Mark authorization completed on driver indication during
# 4-way HS offload") as it break authentication on at least brcmfmac.
# see https://bugzilla.redhat.com/show_bug.cgi?id=2302577
Patch10: wpa_supplicant-Revert-Mark-authorization-completed-on-driver-indica.patch
# Move signal strength change messages to debug to drastically reduce logging spew
# see https://bugzilla.redhat.com/2309148
# From: https://w1.fi/cgit/hostap/commit/?id=c330b5820eefa8e703dbce7278c2a62d9c69166a
Patch11: wpa_supplicant-Send-signal-change-as-debug-msg.patch
# use pkcs11-provider instead of OpenSSL engine
Patch12: wpa_supplicant-OpenSSL-Use-pkcs11-provider-when-OPENSSL_NO_ENGINE-i.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2439303
Patch13: wpa_supplicant-OpenSSL-Support-PEM-encoded-chain-from-ca_cert-blob.patch

URL: http://w1.fi/wpa_supplicant/

%if %with gui
BuildRequires: qt-devel >= 4.0
%endif
BuildRequires: openssl-devel
BuildRequires: readline-devel
BuildRequires: dbus-devel
BuildRequires: libnl3-devel
BuildRequires: systemd-units
BuildRequires: docbook-utils
BuildRequires: gcc
%if 0%{?fedora} >= 41
BuildRequires: openssl-devel-engine
%endif
Requires(post): systemd-sysv
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%if 0%{?rhel} >= 10
Requires: pkcs11-provider >= 1.0
%endif

# libeap used to be built from wpa_supplicant with some fairly horrible
# hackery, solely for use by WiMAX. We dropped all WiMAX support around
# F21. This is here so people don't wind up with obsolete libeap packages
# lying around. If it's ever resurrected for any reason, this needs
# dropping.
Obsoletes: libeap < %{epoch}:%{version}-%{release}
Obsoletes: libeap-devel < %{epoch}:%{version}-%{release}

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
%oreon_verify_sources
%autosetup -p1 -n %{name}-%{version}


%build
pushd wpa_supplicant
  cp defconfig .config
  export CFLAGS="${CFLAGS:-%optflags} -fPIE -DPIE"
%if 0%{?rhel} >= 10
  export CFLAGS="$CFLAGS -DOPENSSL_NO_ENGINE"
%endif
  export CXXFLAGS="${CXXFLAGS:-%optflags} -fPIE -DPIE"
  export LDFLAGS="${LDFLAGS:-%optflags} -pie -Wl,-z,now"
  # yes, BINDIR=_sbindir
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
# config
install -D -m 0600 %{SOURCE1} %{buildroot}/%{_sysconfdir}/wpa_supplicant/wpa_supplicant.conf

# init scripts
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_unitdir}/wpa_supplicant.service
install -D -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysconfig/wpa_supplicant
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/logrotate.d/wpa_supplicant

# binary
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
# gui
install -d %{buildroot}/%{_bindir}
install -m 0755 wpa_supplicant/wpa_gui-qt4/wpa_gui %{buildroot}/%{_bindir}
%endif

# man pages
install -d %{buildroot}%{_mandir}/man{5,8}
install -m 0644 wpa_supplicant/doc/docbook/*.8 %{buildroot}%{_mandir}/man8
install -m 0644 wpa_supplicant/doc/docbook/*.5 %{buildroot}%{_mandir}/man5

# some cleanup in docs and examples
rm -f  wpa_supplicant/doc/.cvsignore
rm -rf wpa_supplicant/doc/docbook
chmod -R 0644 wpa_supplicant/examples/*.py


%post
%systemd_post wpa_supplicant.service


%preun
%systemd_preun wpa_supplicant.service

%triggerun -- wpa_supplicant < 0.7.3-10
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply wpa_supplicant
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save wpa_supplicant >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del wpa_supplicant >/dev/null 2>&1 || :
/bin/systemctl try-restart wpa_supplicant.service >/dev/null 2>&1 || :


%files
%config(noreplace) %{_sysconfdir}/wpa_supplicant/wpa_supplicant.conf
%config(noreplace) %{_sysconfdir}/sysconfig/wpa_supplicant
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/wpa_supplicant
%{_unitdir}/wpa_supplicant.service
%{_datadir}/dbus-1/system.d/wpa_supplicant.conf
%{_datadir}/dbus-1/system-services/fi.w1.wpa_supplicant1.service
%{_sbindir}/wpa_passphrase
%{_sbindir}/wpa_supplicant
%{_sbindir}/wpa_cli
%{_sbindir}/eapol_test
%dir %{_sysconfdir}/wpa_supplicant
%{_mandir}/man8/wpa_supplicant.8.gz
%{_mandir}/man8/wpa_priv.8.gz
%{_mandir}/man8/wpa_passphrase.8.gz
%{_mandir}/man8/wpa_cli.8.gz
%{_mandir}/man8/wpa_background.8.gz
%{_mandir}/man8/eapol_test.8.gz
%{_mandir}/man5/*
%doc README
%doc wpa_supplicant/ChangeLog
%doc wpa_supplicant/eap_testing.txt
%doc wpa_supplicant/todo.txt
%doc wpa_supplicant/wpa_supplicant.conf
%doc wpa_supplicant/examples
%license COPYING


%if %with gui
%files gui
%{_bindir}/wpa_gui
%{_mandir}/man8/wpa_gui.8.gz
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.11-10
- Prepare for Oreon 11 (RP1)
