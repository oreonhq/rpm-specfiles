%global source0_hash f29590054abfc12dd8a3249a8356496b12e08a30fc8a723dd781f7742f6f37eb

Name:           8088_bios
Version:        0.9.9
Release:        %autorelease
Summary:        BIOS for Intel 8088 based computers

License:        GPL-3.0-or-later
URL:            https://github.com/skiselev/8088_bios
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  xtideuniversalbios

BuildArch:      noarch

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

%files
%license copyright.tmpl
%doc README.md
%{_datadir}/%{name}/

%changelog
%autochangelog
