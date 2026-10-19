%global source0_hash e183832befac14dc2a0b8e3f2a329edd45d53502a1bb5b9988d61d41eb6af707
%bcond check 0
%global crate kdotool
Name:           rust-kdotool
Version:        0.2.1
Release:        1%{?dist}
Summary:        Xdotool-like tool to manipulate windows on KDE Wayland
License:        Apache-2.0
URL:            https://crates.io/crates/kdotool
Source0:        https://static.crates.io/crates/kdotool/kdotool-%{version}.crate
Patch:          kdotool-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Xdotool-like tool to manipulate windows on KDE Wayland
License:        Apache-2.0 AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n kdotool -f %{oreon_filedir}/kdotool.list

%changelog

%autochangelog
