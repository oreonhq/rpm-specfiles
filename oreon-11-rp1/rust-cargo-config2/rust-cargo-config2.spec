%global source0_hash 1f7dacdd4a7586d602c2543e0217304bebc6502bde82154209cd8f09f24a7718
%bcond check 1
%global debug_package %{nil}
%global crate cargo-config2
Name:           rust-cargo-config2
Version:        0.1.43
Release:        1%{?dist}
Summary:        Load and resolve Cargo configuration
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/cargo-config2
Source0:        https://static.crates.io/crates/cargo-config2/cargo-config2-%{version}.crate
Patch:          cargo-config2-fix-metadata-auto.diff
Patch:          cargo-config2-fix-metadata.diff
Patch2:         0001-Skip-test-that-requires-un-published-test-helper-cra.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Load and resolve Cargo configuration
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -- -- %{shrink:
    --skip resolve::tests::parse_cfg_list
    --skip cfg_expr::tests::eval::complex
    --skip cfg_expr::tests::eval::target_family
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-cargo-config2-devel -f %{oreon_filedir}/rust-cargo-config2-devel.list

%changelog

%autochangelog
