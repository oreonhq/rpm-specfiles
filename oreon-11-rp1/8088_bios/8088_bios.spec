%global source0_hash 484c9ae5d07ea58bbccc2032f5c66d0b12b9425ed24442fed77ea8c2645af83a
Name:           8088_bios
Version:        1.0.2
Release:        1%{?dist}
Summary:        BIOS for Intel 8088 based computers
License:        GPL-3.0-or-later
URL:            https://github.com/skiselev/8088_bios
Source0:        https://github.com/skiselev/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  xtideuniversalbios
# /oreon:deps
%description
This package provides a BIOS for Sergey Kiselev's IBM PC/XT compatible systems:
Micro 8088, Xi 8088 and Sergey's XT.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Replace bundled xtide bios with the packaged version padded to 8 kB
dd if=%{_datadir}/xtideuniversalbios/ide_xt.bin of=ide_xt.bin bs=8k count=1 conv=sync

%build

for machine in MACHINE_XI8088 MACHINE_FE2010A; do
  %make_build MACHINE="$machine" XTIDE=ide_xt.bin
  rm bios.bin bios.lst
done
%install
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name} bios*.bin
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
