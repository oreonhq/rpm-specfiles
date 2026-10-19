%global source0_hash 141489261c0d436be4b92f78faf240c32694426685413d9d50e3585feba5eb79
%global readers_dir %(pkg-config libpcsclite --variable=usbdropdir)
Name:		pcsc-cyberjack
Summary:        PC/SC driver for REINER SCT cyberjack USB chip card reader
Version:	3.99.5final.SP16
%global version_prefix %(c=%{version}; echo ${c:0:6})
%global version_suffix %(c=%{version}; echo ${c:12:4})
Release:        2%{?dist}
License:	GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://www.reiner-sct.com/
Source0:        https://support.reiner-sct.de/downloads/LINUX/V%{version_prefix}_%{version_suffix}/%{name}-%{version}.tar.bz2
Source1:	%{name}-3.99.5final.SP09-README-FEDORA
Source2:	libifd-cyberjack6.udev
Source3:	%{name}.sysusersd
Patch0:		%{name}-3.99.5final.SP09-configure.patch
Requires:	udev
Requires:	pcsc-lite
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libsysfs-devel
BuildRequires:  libtool
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  pcsc-lite-devel
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%package cjflash
Summary:	Flash tool for cyberJack
Requires:	%{name}%{?_isa} = %{version}-%{release}
%package examples
Summary:	Sample code
Requires:	%{name} = %{version}-%{release}
License:	GPL-2.0-or-later
BuildArch:	noarch
%description
REINER SCT cyberJack USB chip card reader user space driver.

This package includes the IFD driver for the cyberJack non-contact (RFID)
and contact USB chip card reader.

For more information regarding installation under Linux see the README.txt
in the documentation directory, esp. regarding compatibility with host
controllers.

For more information about the reader, software updates and a shop see
https://www.reiner-sct.com/

%description cjflash
Tool to flash Reiner SCT cyberJack card readers.

%description examples
Sample code to use/test SCardControl() API by Ludovic Rousseau.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
autoreconf --force --install

# README-FEDORA
install -p -m 0644 %{SOURCE1} README-FEDORA.txt

%build

%configure \
	--disable-static \
	--enable-pcsc \
	--sysconfdir="%{_sysconfdir}" \
	--with-usbdropdir="%{readers_dir}" \
	--enable-release \
	--enable-udev \
	--enable-hal=no
%make_build
pushd doc
for file in LIESMICH.txt README.txt; do
  iconv -f iso-8859-1 -t utf-8 $file -o $file.conv
  touch -c -r $file $file.conv
  mv -f $file.conv $file
done
popd
pushd tools/cjflash
%make_build
popd
%install
%make_install
rm %{buildroot}%{readers_dir}/libifd-cyberjack.bundle/Contents/Linux/libifd-cyberjack.la
mv %{buildroot}/etc/cyberjack.conf.default %{buildroot}/etc/cyberjack.conf
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/93-cyberjack.rules
sed -e 's/GROUP="pcscd"/GROUP="cyberjack"/' -i %{buildroot}%{_udevrulesdir}/93-cyberjack.rules
touch -c -r %{SOURCE2} %{buildroot}%{_udevrulesdir}/93-cyberjack.rules
pushd tools/cjflash
%make_install
popd
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

%sysusers_create_compat %{SOURCE3}
%post

%udev_rules_update
systemctl try-restart pcscd.socket
exit 0
%postun

%udev_rules_update
if [ $1 -eq 0 ]; then
  systemctl try-restart pcscd.socket
fi
exit 0
%files -f %{oreon_filedir}/main.list
%files -n pcsc-cyberjack-cjflash -f %{oreon_filedir}/pcsc-cyberjack-cjflash.list
%files -n pcsc-cyberjack-examples -f %{oreon_filedir}/pcsc-cyberjack-examples.list

%changelog

%autochangelog
