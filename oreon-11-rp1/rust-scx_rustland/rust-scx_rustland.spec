%global source0_hash f14a8ffd8b6b2b9e8e97c8928311cb605591f236e9573467511997413ab5ad9d
%bcond check 0
%global crate scx_rustland
Name:           rust-scx_rustland
Version:        1.1.3
Release:        1%{?dist}
Summary:        A simple user-space scheduler written in Rust
License:        GPL-2.0-only
URL:            https://crates.io/crates/scx_rustland
Source0:        https://static.crates.io/crates/scx_rustland/scx_rustland-%{version}.crate
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        A simple user-space scheduler written in Rust
License:        GPL-2.0-only AND (MIT OR Apache-2.0) AND Unicode-3.0 AND Unicode-DFS-2016 AND Apache-2.0 AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND (BSD-3-Clause OR MIT OR Apache-2.0) AND ISC AND (LGPL-2.1-only OR BSD-2-Clause) AND MIT AND (Unlicense OR MIT) AND Zlib
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
%files -n scx_rustland -f %{oreon_filedir}/scx_rustland.list

%changelog

%autochangelog
