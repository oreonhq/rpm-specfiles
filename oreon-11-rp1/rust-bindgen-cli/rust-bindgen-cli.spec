%global source0_hash 5622e043625b6d1f32c84f53699690a44d1419e657879de26eb252699f5ebb7c
%bcond check 1
%global crate bindgen-cli
Name:           rust-bindgen-cli
Version:        0.73.2
Release:        1%{?dist}
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
License:        BSD-3-Clause
URL:            https://crates.io/crates/bindgen-cli
Source0:        https://static.crates.io/crates/bindgen-cli/bindgen-cli-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
License:        %{shrink:
    BSD-3-Clause AND
    Apache-2.0 AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
Provides:       bindgen = %{version}-%{release}
Obsoletes:      bindgen < 0.61
Requires:       clang-libs
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
%files -n bindgen-cli -f %{oreon_filedir}/bindgen-cli.list

%changelog

%autochangelog
