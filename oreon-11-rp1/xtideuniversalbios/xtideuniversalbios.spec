%global source0_hash f92d1e3f88d8ce971d443168a4b59f08f5db414c64b50472412f719410ca0761
%global date 20230219
%global revision 625
Name:           xtideuniversalbios
Version:        2.0.0^%{date}svn%{revision}
Release:        1%{?dist}
Summary:        XTIDE Universal BIOS
License:        GPL-2.0-or-later
URL:            https://www.xtideuniversalbios.org
Source0:        %{name}-r%{revision}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  mingw32-gcc-c++
BuildRequires:  nasm
BuildRequires:  perl
BuildRequires:  sed
BuildRequires:  upx
# /oreon:deps
%description
XTIDE Universal BIOS makes it possible to use modern large ATA hard disks or
Compact Flash cards on old PC's. You can then enjoy quiet or noiseless drives
with more capacity than you'll ever need for old computers.

XTIDE Universal BIOS (also known as simply "XUB") can be used on any IBM PC,
XT, AT or 100% compatible system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-r%{revision}

# Convert makefiles from Windows to Linux
find . -type f -name makefile -exec sed -i '{}' -e 's:\\:/:g' -e 's:\*\.\*:*:g' \;
sed -i Serial_Server/makefile \
  -e 's:/c :-c :g' \
  -e 's:/Febuild:-o build:g' \
  -e 's:/Fobuild:-o build:g'

# Fix end of line encoding
sed -i 's/\r$//' XTIDE_Universal_BIOS/Doc/*.txt

%build

for target in \
  BIOS_Drive_Information_Tool \
  XTIDE_Universal_BIOS
do
  %make_build -C "$target" \
    AS="nasm" \
    MAKE="make" \
    RM="rm -rf"
done
for target in \
  Configurator \
  Serial_Server \
  XTIDE_Universal_BIOS_Configurator_v2
do
  %make_build -C "$target" release \
    AS="nasm" \
    CXX="%{mingw32_target}-g++" \
    CXXFLAGS="-Os -DWIN32 -fpermissive" \
    MAKE="make" \
    RM="rm -rf"
done
%install
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name} \
  BIOS_Drive_Information_Tool/Build/biosdrvs.com \
  Configurator/Build/idecfg.com \
  Serial_Server/build/serdrive.exe \
  XTIDE_Universal_BIOS/Build/*.bin \
  XTIDE_Universal_BIOS_Configurator_v2/Build/xtidecfg.com
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
