%global source0_hash 796e8d2b6696392a43bea58116b667fb4c29727dc5abd27d6acf338bb4f688c7
%bcond check 0
%global debug_package %{nil}
%global crate rust-ini
Name:           rust-rust-ini
Version:        0.21.3
Release:        1%{?dist}
Summary:        Ini configuration file parsing library in Rust
License:        MIT
URL:            https://crates.io/crates/rust-ini
Source0:        https://static.crates.io/crates/rust-ini/rust-ini-%{version}.crate
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
Summary:        Ini configuration file parsing library in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+brackets-in-section-names-devel
Summary:        Ini configuration file parsing library in Rust
BuildArch:      noarch
%description -n %{name}+brackets-in-section-names-devel

This package contains library source intended for building other packages which
use the "brackets-in-section-names" feature of the "%{crate}" crate.

%package     -n %{name}+case-insensitive-devel
Summary:        Ini configuration file parsing library in Rust
BuildArch:      noarch
%description -n %{name}+case-insensitive-devel

This package contains library source intended for building other packages which
use the "case-insensitive" feature of the "%{crate}" crate.

%package     -n %{name}+inline-comment-devel
Summary:        Ini configuration file parsing library in Rust
BuildArch:      noarch
%description -n %{name}+inline-comment-devel

This package contains library source intended for building other packages which
use the "inline-comment" feature of the "%{crate}" crate.

%package     -n %{name}+unicase-devel
Summary:        Ini configuration file parsing library in Rust
BuildArch:      noarch
%description -n %{name}+unicase-devel

This package contains library source intended for building other packages which
use the "unicase" feature of the "%{crate}" crate.

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
%files -n rust-rust-ini-devel -f %{oreon_filedir}/rust-rust-ini-devel.list

%changelog

%autochangelog
