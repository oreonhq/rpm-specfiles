%global source0_hash 1de7b9db599617af81868e242424509c9b81308fe1c0998611cdb16b007a3662

Name:    trezor-common
Version: 2.3.6
Release: 12%{?dist}
Summary: udev rules and protobuf messages for the hardware wallet Trezor

# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:       LGPL-3.0-or-later
URL:           https://github.com/trezor
Source0:       https://github.com/trezor/trezor-firmware/archive/refs/tags/core/v%{version}.tar.gz#/trezor-firmware-core-v%{version}.tar.gz

BuildArch:     noarch

BuildRequires: systemd
Conflicts:     python3-trezor <= 0.12.2-2

%description
Provides udev rules and protobuf messages for all the hardware wallets from
TREZOR.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n trezor-firmware-core-v%{version}

%build
#Nothing to build

%install
pushd common
install -Dpm 644 udev/51-trezor.rules %{buildroot}%{_udevrulesdir}/51-trezor.rules

for file in $(find ./protob -name \*.proto); do
  install -Dpm 644 $file %{buildroot}%{_datadir}/trezor/$file
done
popd

%files
%doc common/README.md
%license common/COPYING
%{_udevrulesdir}/51-trezor.rules
%{_datadir}/trezor

%changelog
%autochangelog
