%global source0_hash 25b31d01485e0ce2b05b001f0f19f8a03f58aee2a8e6799cfada88fd22be94ae
%bcond check 0
%global crate eif_build
Name:           rust-eif_build
Version:        0.2.1
Release:        1%{?dist}
Summary:        CLI tool to create EIF files for AWS Nitro Enclaves
License:        Apache-2.0
URL:            https://crates.io/crates/eif_build
Source0:        https://static.crates.io/crates/eif_build/eif_build-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        CLI tool to create EIF files for AWS Nitro Enclaves
License:        Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT) AND MIT
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
%files -n eif_build -f %{oreon_filedir}/eif_build.list

%changelog

%autochangelog
