%global source0_hash 6a140f41f55ff1f2126aed96961bad2387ae31d7f9bbd0e98ec888073beaac6f
%bcond check 0
%global debug_package %{nil}
%global crate cose-rust
Name:           rust-cose-rust
Version:        0.1.8
Release:        1%{?dist}
Summary:        COSE Rust implementation
License:        MIT
URL:            https://crates.io/crates/cose-rust
Source0:        https://static.crates.io/crates/cose-rust/cose-rust-%{version}.crate
Patch0: use-system-OpenSSL-instead-of-vendored.patch
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
Summary:        COSE Rust implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+hex-devel
Summary:        COSE Rust implementation
BuildArch:      noarch
%description -n %{name}+hex-devel

This package contains library source intended for building other packages which
use the "hex" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        COSE Rust implementation
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        COSE Rust implementation
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
%files -n rust-cose-rust-devel -f %{oreon_filedir}/rust-cose-rust-devel.list

%changelog

%autochangelog
