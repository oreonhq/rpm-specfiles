%global source0_hash 93411e420bcd1a75ddd1dc3caf18c23155eda2c090631a85af21ba19e97093b5
%bcond check 0
%global debug_package %{nil}
%global crate ropey
Name:           rust-ropey
Version:        1.6.1
Release:        1%{?dist}
Summary:        Fast and robust text rope for Rust
License:        MIT
URL:            https://crates.io/crates/ropey
Source0:        https://static.crates.io/crates/ropey/ropey-%{version}.crate
Patch:          ropey-fix-metadata.diff
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
Summary:        Fast and robust text rope for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cr_lines-devel
Summary:        Fast and robust text rope for Rust
BuildArch:      noarch
%description -n %{name}+cr_lines-devel

This package contains library source intended for building other packages which
use the "cr_lines" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        Fast and robust text rope for Rust
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+small_chunks-devel
Summary:        Fast and robust text rope for Rust
BuildArch:      noarch
%description -n %{name}+small_chunks-devel

This package contains library source intended for building other packages which
use the "small_chunks" feature of the "%{crate}" crate.

%package     -n %{name}+unicode_lines-devel
Summary:        Fast and robust text rope for Rust
BuildArch:      noarch
%description -n %{name}+unicode_lines-devel

This package contains library source intended for building other packages which
use the "unicode_lines" feature of the "%{crate}" crate.

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
%files -n rust-ropey-devel -f %{oreon_filedir}/rust-ropey-devel.list

%changelog

%autochangelog
