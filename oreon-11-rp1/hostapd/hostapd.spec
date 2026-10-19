%global source0_hash f43502561c28ba47ab77e18e1a973d07361c68cc8b14178e619bd5796b70eabd
%global _hardened_build 1
Name:           hostapd
Version:        2.12
Release:        1%{?dist}
Summary:        IEEE 802.11 AP, IEEE 802.1X/WPA/WPA2/EAP/RADIUS Authenticator
License:        BSD-3-Clause
URL:            http://w1.fi/hostapd
Source0:        http://w1.fi/releases/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.conf
Source3:        %{name}.conf.5
Source4:        %{name}.sysconfig
Source5:        %{name}.init
Patch1: OpenSSL-Use-pkcs11-provider-when-OPENSSL_NO_ENGINE-i.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libnl3-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
%{name} is a user space daemon for access point and authentication servers. It
implements IEEE 802.11 access point management, IEEE 802.1X/WPA/WPA2/EAP
Authenticators and RADIUS authentication server.

%{name} is designed to be a "daemon" program that runs in the back-ground and
acts as the backend component controlling authentication. %{name} supports
separate frontend programs and an example text-based frontend, hostapd_cli, is
included with %{name}.

%package logwatch
Summary:        Logwatch scripts for hostapd
Requires:       %{name} = %{version}-%{release}
Requires:       logwatch
Requires:       perl-interpreter
%description logwatch
Logwatch scripts for hostapd.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
sed \
    -e '$ a CONFIG_SAE=y' \
    -e '$ a CONFIG_SUITEB192=y' \
    -e '$ a CONFIG_P2P=y' \
    -e '$ a CONFIG_P2P_MANAGER=y' \
    -e '/^#CONFIG_DRIVER_NL80211=y/s/^#//' \
    -e '/^#CONFIG_RADIUS_SERVER=y/s/^#//' \
    -e '/^#CONFIG_DRIVER_WIRED=y/s/^#//' \
    -e '/^#CONFIG_DRIVER_NONE=y/s/^#//' \
    -e '/^#CONFIG_IEEE80211N=y/s/^#//' \
    -e '/^#CONFIG_IEEE80211R=y/s/^#//' \
    -e '/^#CONFIG_IEEE80211AC=y/s/^#//' \
    -e '/^#CONFIG_IEEE80211AX=y/s/^#//' \
    -e '/^#CONFIG_IEEE80211BE=y/s/^#//' \
    -e '/^#CONFIG_FULL_DYNAMIC_VLAN=y/s/^#//' \
    -e '/^#CONFIG_LIBNL32=y/s/^#//' \
    -e '/^#CONFIG_ACS=y/s/^#//' \
    -e '/^#CONFIG_OCV=y/s/^#//' \
    -e '/^#CONFIG_OWE=y/s/^#//' \
    -e '/^#CONFIG_WPS=y/s/^#//' \
    -e '/^#CONFIG_WPA_CLI_EDIT=y/s/^#//' \
    < hostapd/defconfig \
    > hostapd/.config
echo "CFLAGS += -I%{_includedir}/libnl3 -DOPENSSL_NO_ENGINE" >> hostapd/.config
echo "LIBS += -L%{_libdir}" >> hostapd/.config

%build

make %{?_smp_mflags} EXTRA_CFLAGS="$RPM_OPT_FLAGS -DOPENSSL_NO_ENGINE" -C hostapd
%install
install -p -m 755 -D %{SOURCE5} %{buildroot}%{_initrddir}/%{name}
install -d %{buildroot}/%{_sysconfdir}/logwatch/conf/services
install -pm 0644 %{name}/logwatch/%{name}.conf  \
        %{buildroot}/%{_sysconfdir}/logwatch/conf/services/%{name}.conf
install -d %{buildroot}/%{_sysconfdir}/logwatch/scripts/services
install -pm 0755 %{name}/logwatch/%{name} \
        %{buildroot}/%{_sysconfdir}/logwatch/scripts/services/%{name}
install -d %{buildroot}/%{_sysconfdir}/%{name}
install -pm 0600 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}
install -d %{buildroot}/%{_sysconfdir}/sysconfig
install -pm 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install -d %{buildroot}/%{_sbindir}
install -pm 0755 %{name}/%{name} %{buildroot}%{_sbindir}/%{name}
install -pm 0755 %{name}/%{name}_cli %{buildroot}%{_sbindir}/%{name}_cli
install -d %{buildroot}%{_mandir}/man{1,5,8}
install -pm 0644 %{name}/%{name}_cli.1 %{buildroot}%{_mandir}/man1
install -pm 0644 %{SOURCE3} %{buildroot}%{_mandir}/man5
install -pm 0644 %{name}/%{name}.8 %{buildroot}%{_mandir}/man8
cp %{name}/README ./README.%{name}
cp %{name}/README-WPS ./README-WPS.%{name}
cp %{name}/logwatch/README ./README.logwatch
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hostapd-logwatch -f %{oreon_filedir}/hostapd-logwatch.list

%changelog

%autochangelog
