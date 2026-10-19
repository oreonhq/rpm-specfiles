%global source1_hash 81c8b92050a85af69f079455868cb1e2fae3345f976a7206b2d70e158ae25653
%global source0_hash 4d98e0e799c53340069f6793c58bbee75c1cd321c19ffca35e5b18ea592682f4
%bcond_without check
%global crate bootupd
Name:           rust-%{crate}
Version:        0.3.2
Release:        1%{?dist}
Summary:        Bootloader updater
License:        Apache-2.0
URL:            https://github.com/coreos/bootupd
Source0:        https://crates.io/api/v1/crates/bootupd/0.3.2/download#/bootupd-0.3.2.crate
Source1:        https://github.com/coreos/bootupd/releases/download/v%{version}/bootupd-0.3.2-vendor.tar.zstd
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  rustc
BuildRequires:  systemd
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Bootloader updater
License:        Apache-2.0 AND (Apache-2.0 WITH LLVM-exception) AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
%{?systemd_requires}
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1 -a1
%oreon_vendor_cargo
%build

%cargo_build
%cargo_vendor_manifest
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%install
%make_install INSTALL="install -p -c"
%{__make} install-grub-static DESTDIR=%{?buildroot} INSTALL="%{__install} -p"
%{__make} install-systemd-unit DESTDIR=%{?buildroot} INSTALL="%{__install} -p"
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bootupd -f %{oreon_filedir}/bootupd.list

%changelog

%autochangelog
