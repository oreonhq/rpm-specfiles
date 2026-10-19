%global source0_hash 21db055bc8f87a28a2b9bcf23ad807e9bb3da8537eb7716871da797698ff2c84
%bcond check 1
%global crate ybaas
Name:           rust-ybaas
Version:        0.0.19
Release:        1%{?dist}
Summary:        Yubibomb as a service
License:        GPL-3.0-only
URL:            https://crates.io/crates/ybaas
Source0:        https://static.crates.io/crates/ybaas/ybaas-%{version}.crate
Patch:          ybaas-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Yubibomb as a service
License:        GPL-3.0-only AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
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
%files -n ybaas -f %{oreon_filedir}/ybaas.list

%changelog

%autochangelog
