%global source0_hash 5cb1fc680b38eed6fad4c02b3871c09d2c81db8c96aa4e9c0a34904c830f09b5
%bcond check 0
%global debug_package %{nil}
%global crate slog-term
Name:           rust-slog-term
Version:        2.9.2
Release:        1%{?dist}
Summary:        Unix terminal drain and formatter for slog-rs
License:        MPL-2.0 OR MIT OR Apache-2.0
URL:            https://crates.io/crates/slog-term
Source0:        https://static.crates.io/crates/slog-term/slog-term-%{version}.crate
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

%package     -n %{name}+erased-serde-devel
Summary:        Unix terminal drain and formatter for slog-rs
BuildArch:      noarch
%description -n %{name}+erased-serde-devel

This package contains library source intended for building other packages which
use the "erased-serde" feature of the "%{crate}" crate.

%package     -n %{name}+nested-values-devel
Summary:        Unix terminal drain and formatter for slog-rs
BuildArch:      noarch
%description -n %{name}+nested-values-devel

This package contains library source intended for building other packages which
use the "nested-values" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Unix terminal drain and formatter for slog-rs
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Unix terminal drain and formatter for slog-rs
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

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
%files -n rust-slog-term-devel -f %{oreon_filedir}/rust-slog-term-devel.list

%changelog

%autochangelog
