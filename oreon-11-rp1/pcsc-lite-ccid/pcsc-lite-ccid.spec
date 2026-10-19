%global source0_hash 4ff98151a7feb828a711e2f9d68c6b6065a97c597a81c2cbbd11d7f7edcfe743
%global source1_hash 9dfe2db0b4736c3703cfabee37b16a30b118df37864b28fc66f95d32a3c9abfe
%global dropdir %(pkg-config libpcsclite --variable usbdropdir 2>/dev/null)
%global pcsc_lite_ver 1.8.9
Name:           pcsc-lite-ccid
Version:        1.8.4
Release:        1%{?dist}
Summary:        Generic USB CCID smart card reader driver
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://ccid.apdu.fr/files
Source0:        https://ccid.apdu.fr/files/ccid-%{version}.tar.xz
Source1:        https://ccid.apdu.fr/files/ccid-%{version}.tar.xz.asc
Source2:        gpgkey-F5E11B9FFE911146F41D953D78A1B4DFE8F9C57E.gpg
Patch0:         ccid-1.4.26-omnikey-3121.patch
Requires(post): systemd
Requires(postun): systemd
Requires:       pcsc-lite%{?_isa} >= %{pcsc_lite_ver}
Provides:       pcsc-ifd-handler
Obsoletes:      ccid < 1.4.0-3
Provides:       ccid = %{version}-%{release}
Provides:       bundled(simclist) = 1.6
# oreon:deps
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libusb1-devel
BuildRequires:  meson
BuildRequires:  pcsc-lite-devel
BuildRequires:  perl-Getopt-Long
BuildRequires:  perl-interpreter
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
Generic USB CCID (Chip/Smart Card Interface Devices) driver for use with the
PC/SC Lite daemon.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -n ccid-%{version} -p1

%build

%meson -Dserial=true
%meson_build
%install
%meson_install
cp -p src/openct/LICENSE LICENSE.openct
%oreon_autofiles main

%post

%systemd_postun_with_restart pcscd.service
%preun

%systemd_preun pcscsd.service
%postun

%systemd_postun_with_restart pcscd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
