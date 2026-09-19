%global source0_hash 4703a58ad11b777af04019a4f1b114ec4591c05aa1ca6b9c7ff5743ff3d14ae1

%global _hardened_build 1
%global _version        2025-09-R1

## {Local macros...
%global cfgdir          %_sysconfdir/%name
%global _rpmversion     0.0.%(echo %_version | tr - .)
## ...local macros}

%{!?apply:%global  apply(p:n:b:) %patch%%{-n:%%{-n*}} %%{-p:-p%%{-p*}} %%{-b:-b%%{-b*}} \
%nil}

Summary:        WLAN detector, sniffer and IDS
Name:           kismet
Version:        %_rpmversion
Release:        3%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.kismetwireless.net/
Source0:        http://www.kismetwireless.net/code/%{name}-%_version.tar.xz

Patch0:         kismet-include.patch
Patch1:         kismet-install.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel diffutils
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel libcap-devel libnl3-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  libmicrohttpd-devel protobuf-devel protobuf-c-devel
BuildRequires:  NetworkManager-libnm-devel libusb1-devel
BuildRequires:  sqlite-devel libwebsockets-devel
BuildRequires:  rtl-sdr-devel
BuildRequires:  mosquitto-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  make

%description
Kismet is an 802.11 layer2 wireless network detector, sniffer, and
intrusion detection system. Kismet will work with any wireless card
which supports raw monitoring (rfmon) mode, and can sniff 802.11b,
802.11a, and 802.11g traffic.

Kismet identifies networks by passively collecting packets and detecting
standard named networks, detecting (and given time, decloaking) hidden
networks, and infering the presence of nonbeaconing networks via data
traffic.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{_version}

%patch -P 0 -p0
%patch -P 1 -p0

sed -i 's!\$(prefix)/lib/!%{_libdir}/!g' plugin-*/Makefile

# set our 'kismet' user, disable GPS and log into %%logdir by
# default
sed -i \
    -e '\!^ouifile=/etc/manuf!d' \
    -e '\!^ouifile=/usr/share/wireshark/wireshark/manuf!d' \
    conf/kismet.conf

sed -i s/@VERSION@/%{version}/g packaging/kismet.pc.in

# Create a sysusers.d config file
cat >kismet.sysusers.conf <<EOF
g kismet -
EOF

%build

export ac_cv_lib_uClibcpp_main=no # we do not want to build against uClibc++, even when available
export LDFLAGS='-Wl,--as-needed'
%configure \
           --enable-wifi-coconut \
           --sysconfdir=%cfgdir \
           CXXFLAGS="$RPM_OPT_FLAGS -D__STDC_FORMAT_MACROS" \
           --disable-python-tools

%make_build

%install
BIN=$RPM_BUILD_ROOT/bin ETC=$RPM_BUILD_ROOT/etc %{__make} suidinstall DESTDIR=%{?buildroot} INSTALL="%{__install} -p"

install -m0644 -D kismet.sysusers.conf %{buildroot}%{_sysusersdir}/kismet.conf

%files
%doc README*
%dir %attr(0755,root,root) %cfgdir
%config(noreplace) %cfgdir/*
%{_bindir}/kismet
%{_bindir}/kismet_cap_kismetdb
%{_bindir}/kismet_cap_pcapfile
%{_bindir}/kismet_discovery
%{_bindir}/kismet_server
%{_bindir}/kismetdb_clean
%{_bindir}/kismetdb_dump_devices
%{_bindir}/kismetdb_statistics
%{_bindir}/kismetdb_strip_packets
%{_bindir}/kismetdb_to_gpx
%{_bindir}/kismetdb_to_kml
%{_bindir}/kismetdb_to_pcap
%{_bindir}/kismetdb_to_wiglecsv
%{_bindir}/kismet_cap_antsdr_droneid
%{_bindir}/kismet_cap_freaklabs_zigbee
%{_bindir}/kismet_cap_radiacode_usb
%{_bindir}/kismet_cap_sdr_rtl433
%{_bindir}/kismet_cap_sdr_rtladsb
%{_bindir}/kismet_cap_serial_radview

%attr(4755,root,root) %{_bindir}/kismet_cap_hak5_wifi_coconut
%attr(4755,root,root) %{_bindir}/kismet_cap_linux_bluetooth
%attr(4755,root,root) %{_bindir}/kismet_cap_linux_wifi
%attr(4755,root,root) %{_bindir}/kismet_cap_nrf_51822
%attr(4755,root,root) %{_bindir}/kismet_cap_nrf_52840
%attr(4755,root,root) %{_bindir}/kismet_cap_nrf_mousejack
%attr(4755,root,root) %{_bindir}/kismet_cap_nxp_kw41z
%attr(4755,root,root) %{_bindir}/kismet_cap_rz_killerbee
%attr(4755,root,root) %{_bindir}/kismet_cap_ti_cc_2531
%attr(4755,root,root) %{_bindir}/kismet_cap_ti_cc_2540
%{_datadir}/kismet
%{_libdir}/pkgconfig/kismet.pc
%{_sysusersdir}/kismet.conf

%changelog
%autochangelog
