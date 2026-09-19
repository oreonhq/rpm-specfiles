%global source0_hash af254788be98861f2bd9103fe6e60a774ec96a8c374744eef9197f6043075afa

%global _legacy_common_support 1
#global rcVer 1

Name:       openocd
Version:    0.12.0
Release:    3%{?rcVer:.rc%{rcVer}}%{?dist}.5
Summary:    Debugging, in-system programming and boundary-scan testing for embedded devices

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:    GPL-2.0-only
URL:        https://sourceforge.net/projects/openocd
Source0:    https://downloads.sourceforge.net/project/openocd/openocd/%{version}%{?rcVer:-rc%{rcVer}}/%{name}-%{version}%{?rcVer:-rc%{rcVer}}.tar.bz2
Patch0:     0001-openocd-revert-workarounds-for-expr-syntax-change.patch
Patch1:     0003-jtag-vdebug-fix-endianness-support.patch
Patch2:     0004-openocd-fix-build-with-jimtcl-0.83.patch

BuildRequires: capstone-devel
BuildRequires: chrpath
BuildRequires: gcc
BuildRequires: hidapi-devel
BuildRequires: jimtcl-devel
# Only used for gpio bitbang driver
# BuildRequires: libgpiod-devel
BuildRequires: libjaylink-devel
BuildRequires: libftdi-devel
BuildRequires: libusbx-devel
BuildRequires: make
BuildRequires: sdcc
BuildRequires: texinfo

%description
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system programming 
and boundary-scan testing for embedded devices. Various different boards, 
targets, and interfaces are supported to ease development time.

Install OpenOCD if you are looking for an open source solution for hardware 
debugging.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}%{?rcVer:-rc%{rcVer}} -p1
rm -rf jimtcl
rm -f src/jtag/drivers/OpenULINK/ulink_firmware.hex
sed -i 's/MODE=.*/TAG+="uaccess"/' contrib/60-openocd.rules

%build
pushd src/jtag/drivers/OpenULINK
make PREFIX=sdcc hex
popd

%configure \
  --disable-werror \
  --enable-static \
  --disable-shared \
  --enable-dummy \
  --enable-ftdi \
  --enable-stlink \
  --enable-ti-icdi \
  --enable-ulink \
  --enable-usb-blaster-2 \
  --enable-ft232r \
  --enable-vsllink \
  --enable-xds110 \
  --enable-cmsis-dap-v2 \
  --enable-osbdm \
  --enable-opendous \
  --enable-aice \
  --enable-usbprog \
  --enable-rlink \
  --enable-armjtagew \
  --enable-cmsis-dap \
  --enable-nulink \
  --enable-kitprog \
  --enable-usb-blaster \
  --enable-presto \
  --enable-openjtag \
  --enable-jlink \
  --enable-parport \
  --enable-jtag_vpi \
  --enable-jtag_dpi \
  --enable-ioutil \
  --enable-amtjtagaccel \
  --enable-ep39xx \
  --enable-at91rm9200 \
  --enable-gw16012 \
  --enable-oocd_trace \
  --enable-buspirate \
  --enable-sysfsgpio \
  --enable-esp-usb-jtag \
  --enable-xlnx-pcie-xvc \
  --enable-remote-bitbang \
  --disable-internal-jimtcl \
  --disable-doxygen-html \
  --with-capstone \
  CROSS=
%make_build

%install
%make_install
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{_libdir}/libopenocd.*
rm -rf %{buildroot}/%{_datadir}/%{name}/contrib
mkdir -p %{buildroot}/%{_prefix}/lib/udev/rules.d/
install -p -m 644 contrib/60-openocd.rules %{buildroot}/%{_prefix}/lib/udev/rules.d/60-openocd.rules
chrpath --delete %{buildroot}/%{_bindir}/openocd

%files
%license COPYING
%doc AUTHORS NEWS* NEWTAPS README TODO
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/OpenULINK/ulink_firmware.hex
%{_bindir}/%{name}
%{_prefix}/lib/udev/rules.d/60-openocd.rules
# doc
%{_infodir}/%{name}.info*.gz
%{_mandir}/man1/*

%changelog
%autochangelog
