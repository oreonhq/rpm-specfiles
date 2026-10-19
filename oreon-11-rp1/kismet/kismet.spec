%global source0_hash 4703a58ad11b777af04019a4f1b114ec4591c05aa1ca6b9c7ff5743ff3d14ae1
%global _hardened_build 1
%global _version        2025-09-R1
%global cfgdir          %_sysconfdir/%name
%global _rpmversion     0.0.%(echo %_version | tr - .)
%{!?apply:%global  apply(p:n:b:) %patch%%{-n:%%{-n*}} %%{-p:-p%%{-p*}} %%{-b:-b%%{-b*}} \
%nil}
Summary:        WLAN detector, sniffer and IDS
Name:           kismet
Version:        %_rpmversion
Release:        3%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.kismetwireless.net/
Source0:        http://www.%{name}wireless.net/code/%{name}-%{_version}.tar.xz
Patch0:         kismet-include.patch
Patch1:         kismet-install.patch
# oreon:deps
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  libusb1-devel
BuildRequires:  libwebsockets-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  make
BuildRequires:  mosquitto-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  protobuf-c-devel
BuildRequires:  protobuf-devel
BuildRequires:  rtl-sdr-devel
BuildRequires:  sqlite-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
