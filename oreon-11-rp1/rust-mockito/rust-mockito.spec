%global source0_hash 90820618712cab19cfc46b274c6c22546a82affcb3c3bdf0f29e3db8e1bb92c0
%bcond check 1
%global debug_package %{nil}
%global crate mockito
Name:           rust-mockito
Version:        1.7.2
Release:        1%{?dist}
Summary:        HTTP mocking for Rust
License:        MIT
URL:            https://crates.io/crates/mockito
Source0:        https://static.crates.io/crates/mockito/mockito-%{version}.crate
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
Summary:        HTTP mocking for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        HTTP mocking for Rust
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+colored-devel
Summary:        HTTP mocking for Rust
BuildArch:      noarch
%description -n %{name}+colored-devel

This package contains library source intended for building other packages which
use the "colored" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        HTTP mocking for Rust
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

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

%cargo_test -n
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-mockito-devel -f %{oreon_filedir}/rust-mockito-devel.list

%changelog

%autochangelog
