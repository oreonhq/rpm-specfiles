%global source0_hash e9440a47cc67d7f1f5b78c1a9fc6aecfdcd644674ae2edf926b49f2d4e5316b6
%bcond check 1
%global crate snphost
Name:           rust-snphost
Version:        0.6.1
Release:        1%{?dist}
Summary:        Administrative utility for AMD SEV-SNP
License:        Apache-2.0
URL:            https://crates.io/crates/snphost
Source0:        https://static.crates.io/crates/snphost/snphost-%{version}.crate
Patch:          snphost-fix-metadata.diff
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Administrative utility for AMD SEV-SNP
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND MPL-2.0 AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
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
%files -n snphost -f %{oreon_filedir}/snphost.list

%changelog

%autochangelog
