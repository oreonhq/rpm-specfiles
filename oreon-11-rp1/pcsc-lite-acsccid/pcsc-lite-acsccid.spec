%global source0_hash 8b19aba103ec03c448b9d1b562c8322f8d2ff37cf21d4cb8b0cf522c5f385c9f

%global dropdir %(pkg-config libpcsclite --variable usbdropdir 2>/dev/null)

Name:		pcsc-lite-acsccid
Version:	1.1.13
Release:	3%{?dist}
Summary:	ACS CCID PC/SC Driver for Linux/Mac OS X

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://acsccid.sourceforge.io/
Source0:	https://downloads.sourceforge.net/acsccid/acsccid-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	gettext-devel
BuildRequires:	autoconf automake libtool
BuildRequires:	autoconf-archive
BuildRequires:	gcc
BuildRequires:	pcsc-lite-devel
BuildRequires:	libusb-compat-0.1-devel
BuildRequires:	flex
BuildRequires:	perl
BuildRequires:	pkg-config
# for udev.pc dependency
BuildRequires:  systemd
Requires(post): systemd
Requires(postun): systemd
BuildRequires:	systemd-rpm-macros

Requires:	pcsc-lite

# This is bundled from pcsc-lite-ccid and pcsc-lite upstreams
Provides: bundled(simclist) = 1.6
# There are parts of openct project, last import to CCID on 2004
Provides: bundled(openct) = 0.6.0

%description
acsccid is a PC/SC driver for Linux/Mac OS X and it supports ACS CCID smart card
readers. This library provides a PC/SC IFD handler implementation and
communicates with the readers through the PC/SC Lite resource manager (pcscd).

acsccid is based on ccid. See CCID free software driver [1] for more
information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n acsccid-%{version}

%build
%configure --disable-silent-rules
%make_build

%install
%make_install
install -p -m 644 src/openct/LICENSE LICENSE.openct
install -p -m 644 src/towitoko/README README.towitoko

install -Dpm 644 src/92_pcscd_acsccid.rules %{buildroot}%{_udevrulesdir}/92_pcscd_acsccid.rules

%post
%systemd_postun_with_restart pcscd.service

%preun
%systemd_preun pcscsd.service

%postun
%systemd_postun_with_restart pcscd.service

%files
%doc AUTHORS README README.towitoko
%license COPYING LICENSE.openct
%dir %{dropdir}/ifd-acsccid.bundle/
%dir %{dropdir}/ifd-acsccid.bundle/Contents/
%{dropdir}/ifd-acsccid.bundle/Contents/Info.plist
%dir %{dropdir}/ifd-acsccid.bundle/Contents/Linux/
%{dropdir}/ifd-acsccid.bundle/Contents/Linux/libacsccid.so
%{_prefix}/lib/udev/rules.d/92_pcscd_acsccid.rules

%changelog
%autochangelog
