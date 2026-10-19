%global source0_hash ec1db3da2ff1c397b356c19890cbd4cb7bb9cdaa436476de09a6f0eba47d3758
%bcond check 1
%global crate snpguest
Name:           rust-snpguest
Version:        0.9.2
Release:        1%{?dist}
Summary:        AMD SEV-SNP guest utility tool
License:        Apache-2.0
URL:            https://crates.io/crates/snpguest
Source0:        https://static.crates.io/crates/snpguest/snpguest-%{version}.crate
Patch:          snpguest-fix-metadata.diff
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        AMD SEV-SNP guest utility tool
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND ISC AND MIT AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT)
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
%files -n snpguest -f %{oreon_filedir}/snpguest.list

%changelog

%autochangelog
