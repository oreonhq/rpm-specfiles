%global source0_hash b28f966ff5113ecb0aa8d35312d2dc1b853a851c2ce92693cc4c631bb5821058
%bcond check 1
%global cargo_install_lib 0
%global crate muvm
Name:           rust-muvm
Version:        0.5.1
Release:        1%{?dist}
Summary:        Run programs from your system in a microVM
License:        MIT
URL:            https://crates.io/crates/muvm
Source0:        https://static.crates.io/crates/muvm/muvm-%{version}.crate
Source2:        50-muvm-access.conf
Source3:        access-muvm.lua
ExclusiveArch:  x86_64 aarch64
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Run programs from your system in a microVM
License:        Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
Obsoletes:      krun < 0.1.0-2
Requires:       libkrun >= 1.9.8-1
Requires:       passt
Requires:       socat
Requires:       (wireplumber if pipewire)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
mkdir -p %{buildroot}%{_datadir}/wireplumber/wireplumber.conf.d
mkdir -p %{buildroot}%{_datadir}/wireplumber/scripts/client
cp -p %SOURCE2 %{buildroot}%{_datadir}/wireplumber/wireplumber.conf.d
cp -p %SOURCE3 %{buildroot}%{_datadir}/wireplumber/scripts/client
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n muvm -f %{oreon_filedir}/muvm.list

%changelog

%autochangelog
