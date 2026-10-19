%global source0_hash b67b6d7d08bcfc247ef6ff0ab88a99c188305a3cf57ae2dfd0bcd9a5b36cd5bb
%define _binaries_in_noarch_packages_terminate_build   0
Summary:        Firmware for several ALSA-supported sound cards
Name:           alsa-firmware
Version:        1.2.4
Release:        1%{?dist}
License:        GPL-1.0-or-later and BSD-3-Clause and GPL-2.0-or-later and GPL-2.0-only and LGPL-2.1-or-later
URL:            https://www.alsa-project.org/
Source0:        https://www.alsa-project.org/files/pub/firmware/alsa-firmware-1.2.4.tar.bz2
Requires:       alsa-tools-firmware >= 1.1.7
Requires:       systemd
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This package contains the firmware binaries for a number of sound cards.
Some (but not all of these) require firmware loaders which are included in
the alsa-tools-firmware package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

sed -i s#'multisound/Makefile \\'## configure.ac
sed -i s#multisound## Makefile.am
autoreconf -vif
%configure --disable-loader
make %{?_smp_mflags}
for i in hdsploader mixartloader pcxhrloader usx2yloader vxloader ca0132
do
  mv ${i}/README README.${i}
done
mv aica/license.txt LICENSE.aica_firmware
mv aica/Dreamcast_sound.txt aica_dreamcast_sound.txt
mv ca0132/creative.txt LICENSE.creative_txt
%install
make install DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.4-17
- Prepare for Oreon 11 (RP1)
