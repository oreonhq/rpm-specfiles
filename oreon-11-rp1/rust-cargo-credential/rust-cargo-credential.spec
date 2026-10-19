%global source0_hash 5de74202293b2bc090da20d0b475aa74821caf0e901f29ba97003353886a5b42
%bcond check 0
%global debug_package %{nil}
%global crate cargo-credential
Name:           rust-cargo-credential
Version:        0.4.11
Release:        1%{?dist}
Summary:        A library to assist writing Cargo credential helpers.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cargo-credential
Source0:        https://static.crates.io/crates/cargo-credential/cargo-credential-%{version}.crate
Patch:          cargo-credential-fix-metadata-auto.diff
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
Summary:        A library to assist writing Cargo credential helpers.
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
%files -n rust-cargo-credential-devel -f %{oreon_filedir}/rust-cargo-credential-devel.list

%changelog

%autochangelog
