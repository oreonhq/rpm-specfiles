%global source0_hash f3997c7839262f4ef12cf90b818d6340c18e80f263f1a94bf157d0ec4420380e
%bcond check 0
%global debug_package %{nil}
%global crate wasm-bindgen-macro-support
Name:           rust-wasm-bindgen-macro-support
Version:        0.2.126
Release:        2%{?dist}
Summary:        Internal support crate for the wasm-bindgen macro
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/wasm-bindgen-macro-support
Source0:        https://static.crates.io/crates/wasm-bindgen-macro-support/wasm-bindgen-macro-support-%{version}.crate
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
use the "wasm-bindgen-macro-support" crate.

%package     -n %{name}+default-devel
Summary:        Internal support crate for the wasm-bindgen macro
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+extra-traits-devel
Summary:        Internal support crate for the wasm-bindgen macro
BuildArch:      noarch
%description -n %{name}+extra-traits-devel

This package contains library source intended for building other packages which
use the "extra-traits" feature of the "%{crate}" crate.

%package     -n %{name}+strict-macro-devel
Summary:        Internal support crate for the wasm-bindgen macro
BuildArch:      noarch
%description -n %{name}+strict-macro-devel

This package contains library source intended for building other packages which
use the "strict-macro" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-wasm-bindgen-macro-support-devel -f %{oreon_filedir}/rust-wasm-bindgen-macro-support-devel.list

%changelog

%autochangelog
