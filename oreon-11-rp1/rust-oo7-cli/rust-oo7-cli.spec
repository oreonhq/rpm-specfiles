%global source0_hash c124f562b56f14541aa9e08e1c7f19771bc79e3a3bffd0ee5d73ada48845691b
%bcond check 1
%global crate oo7-cli
Name:           rust-oo7-cli
Version:        0.4.3
Release:        1%{?dist}
Summary:        System keyring access from the terminal
License:        MIT
URL:            https://crates.io/crates/oo7-cli
Source0:        https://static.crates.io/crates/oo7-cli/oo7-cli-%{version}.crate
Patch:          oo7-cli-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        System keyring access from the terminal
License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    Unicode-3.0 AND
    (Apache-2.0 AND MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n oo7-cli -f %{oreon_filedir}/oo7-cli.list

%changelog

%autochangelog
