%global source0_hash df163f89771bd6654d5e116952b9ab2d0b952cd8e3315ddaa615f6d2bfbb1fde
%bcond check 1
%global debug_package %{nil}
%global crate npm-package-json
Name:           rust-npm-package-json
Version:        0.1.3
Release:        1%{?dist}
Summary:        Rust library for parsing npm's package.json file
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/npm-package-json
Source0:        https://static.crates.io/crates/npm-package-json/npm-package-json-%{version}.crate
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
Summary:        Rust library for parsing npm's package.json file
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
%files -n rust-npm-package-json-devel -f %{oreon_filedir}/rust-npm-package-json-devel.list

%changelog

%autochangelog
