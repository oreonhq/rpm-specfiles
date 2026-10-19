%global source0_hash 5238725303cc9f252800c49cc0d115a79754ebcb2beca9e8df6db44e8a941bff
%bcond check 1
%global crate cargo-insta
Name:           rust-cargo-insta
Version:        1.46.3
Release:        1%{?dist}
Summary:        Review tool for the insta snapshot testing library for Rust
License:        Apache-2.0
URL:            https://crates.io/crates/cargo-insta
Source0:        https://static.crates.io/crates/cargo-insta/cargo-insta-%{version}.crate
Patch:          cargo-insta-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Review tool for the insta snapshot testing library for Rust
License:        %{shrink:
    Apache-2.0 AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
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

%cargo_test -- --bins
%endif
%files -f %{oreon_filedir}/main.list
%files -n cargo-insta -f %{oreon_filedir}/cargo-insta.list

%changelog

%autochangelog
