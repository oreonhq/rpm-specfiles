%global source0_hash e1b88fcfe09e89d3866a5c11019378088af2d24c3fbd4f0543f96b479ec90697
%bcond check 0
%global debug_package %{nil}
%global crate uncased
Name:           rust-uncased
Version:        0.9.10
Release:        1%{?dist}
Summary:        Case-preserving, ASCII case-insensitive, no_std string types.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/uncased
Source0:        https://static.crates.io/crates/uncased/uncased-%{version}.crate
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
Summary:        Case-preserving, ASCII case-insensitive, no_std string types.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Case-preserving, ASCII case-insensitive, no_std string types.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Case-preserving, ASCII case-insensitive, no_std string types.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+with-serde-devel
Summary:        Case-preserving, ASCII case-insensitive, no_std string types.
BuildArch:      noarch
%description -n %{name}+with-serde-devel

This package contains library source intended for building other packages which
use the "with-serde" feature of the "%{crate}" crate.

%package     -n %{name}+with-serde-alloc-devel
Summary:        Case-preserving, ASCII case-insensitive, no_std string types.
BuildArch:      noarch
%description -n %{name}+with-serde-alloc-devel

This package contains library source intended for building other packages which
use the "with-serde-alloc" feature of the "%{crate}" crate.

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
%files -n rust-uncased-devel -f %{oreon_filedir}/rust-uncased-devel.list

%changelog

%autochangelog
