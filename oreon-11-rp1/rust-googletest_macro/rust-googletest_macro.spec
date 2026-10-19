%global source0_hash 2ae6abc96141edd26bf5aeec0f119c129c44de3ced09e5073711a02cb74725d0
%bcond check 0
%global debug_package %{nil}
%global crate googletest_macro
Name:           rust-googletest_macro
Version:        0.14.3
Release:        1%{?dist}
Summary:        Procedural macros for GoogleTest Rust
License:        Apache-2.0
URL:            https://crates.io/crates/googletest_macro
Source0:        https://static.crates.io/crates/googletest_macro/googletest_macro-%{version}.crate
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
Summary:        Procedural macros for GoogleTest Rust
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-googletest_macro-devel -f %{oreon_filedir}/rust-googletest_macro-devel.list

%changelog

%autochangelog
