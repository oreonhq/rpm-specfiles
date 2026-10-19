%global source0_hash 8b95dfd93cc39d3f09d996e5210905cf97f542aa54c08906a8e8b5f6ad5853bb
%bcond check 0
%global debug_package %{nil}
%global crate llvm-bitcode
Name:           rust-llvm-bitcode
Version:        0.1.2
Release:        1%{?dist}
Summary:        LLVM Bitcode parser in Rust
License:        MIT
URL:            https://crates.io/crates/llvm-bitcode
Source0:        https://static.crates.io/crates/llvm-bitcode/llvm-bitcode-%{version}.crate
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
Summary:        LLVM Bitcode parser in Rust
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
%files -n rust-llvm-bitcode-devel -f %{oreon_filedir}/rust-llvm-bitcode-devel.list

%changelog

%autochangelog
