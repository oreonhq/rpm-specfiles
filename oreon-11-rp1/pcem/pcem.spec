%global source0_hash e66d32669f399a764c87205a3bab4fbf32946dee4fa3fa92771f3f17022d6a02
%global forgeurl https://github.com/sarah-walker-pcem/pcem
%global metadata_forgeurl https://github.com/X-m7/flathub
%global metadata_commit ad9aafaaf2f3c1faccc3a99c11d62daca8520d02
%global build_type_safety_c 2
Name:           pcem
Version:        17
Release:        1%{?dist}
Summary:        IBM PC emulator
License:        GPL-2.0-or-later and MIT and BSD-3-Clause
URL:            https://pcem-emulator.co.uk
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          pcem-c99.patch
Patch:          pcem-wayland-hack.patch
ExcludeArch:    armv7hl i686 ppc64le s390x
Requires:       8088_bios
Requires:       xtideuniversalbios
Provides:       bundled(dosbox) = 20140227
Provides:       bundled(minivhd) = 20201114
Provides:       bundled(resid-fp) = 0.16vice
Provides:       bundled(slirp) = 0.9.0
Provides:       bundled(cwalk) = 1.2.1
Provides:       bundled(libxml2) = 20190613
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openal-soft-devel
BuildRequires:  sed
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
PCem (short for PC Emulator) is an IBM PC emulator that specializes in running
old operating systems and software that are designed for IBM PC compatibles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -b 1

# Use our build flags, freeze the standard version, and disable strict aliasing rules
sed -i configure.ac \
  -e 's:CFLAGS="-O3 -fcommon":CFLAGS="-fcommon %{build_cflags} -std=gnu11 -Wno-strict-aliasing":' \
  -e 's:CXXFLAGS="-O3 -fcommon":CXXFLAGS="-fcommon %{build_cxxflags} -std=gnu++11 -Wno-strict-aliasing":'
echo 'pcem_LDFLAGS = %{build_ldflags}' >>src/Makefile.am

# Rename variable conflicting with global function
sed -r -i 's/\bpause\b/pause_var/g' src/*.[ch]

# Reorganize bundled project licenses
cp -p src/minivhd/CREDITS.md CREDITS.minivhd
cp -p src/minivhd/LICENSE LICENSE.minivhd
cp -p src/resid-fp/COPYING LICENSE.resid-fp
cp -p src/slirp/COPYRIGHT.txt LICENSE.slirp

%build

autoreconf -ivf
%configure --enable-release-build --enable-alsa --enable-networking
%make_build
%install
%make_install
install -Ddpm0755 %{buildroot}%{_datadir}/%{name}/roms/xi8088
ln -s ../../../8088_bios/bios-xi8088.bin %{buildroot}%{_datadir}/%{name}/roms/xi8088/
ln -s ../../xtideuniversalbios/ide_xt.bin %{buildroot}%{_datadir}/%{name}/roms/
ln -s ../../xtideuniversalbios/ide_at.bin %{buildroot}%{_datadir}/%{name}/roms/
install -Dpm0644 -t %{buildroot}%{_datadir}/pixmaps \
  ../flathub-%{metadata_commit}/uk.co.pcem_emulator.pcem.svg
desktop-file-install \
  --add-category="System;Emulator" \
  --dir=%{buildroot}%{_datadir}/applications \
  ../flathub-%{metadata_commit}/uk.co.pcem_emulator.pcem.desktop
install -Dpm0644 -t %{buildroot}%{_metainfodir} \
  ../flathub-%{metadata_commit}/uk.co.pcem_emulator.pcem.metainfo.xml
%oreon_autofiles main

%check

desktop-file-validate \
  %{buildroot}/%{_datadir}/applications/uk.co.pcem_emulator.pcem.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/uk.co.pcem_emulator.pcem.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
