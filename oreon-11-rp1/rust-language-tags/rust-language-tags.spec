%global source0_hash d4345964bb142484797b161f473a503a434de77149dd8c7427788c6e13379388
%bcond check 0
%global debug_package %{nil}
%global crate language-tags
Name:           rust-language-tags
Version:        0.3.2
Release:        1%{?dist}
Summary:        Language tags for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/language-tags
Source0:        https://static.crates.io/crates/language-tags/language-tags-%{version}.crate
Patch0:         https://github.com/pyfisch/rust-language-tags/pull/41.patch
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
Summary:        Language tags for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Language tags for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-language-tags-devel -f %{oreon_filedir}/rust-language-tags-devel.list

%changelog

%autochangelog
