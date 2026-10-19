%global source0_hash 42b76cf645c92e7850d5a1c9205ebf2864bd32c0ab3e978e6daad51fedf7ef54
%bcond check 0
%global debug_package %{nil}
%global crate slog-scope
Name:           rust-slog-scope
Version:        4.4.1
Release:        1%{?dist}
Summary:        Logging scopes for slog-rs
License:        MPL-2.0 OR MIT OR Apache-2.0
URL:            https://crates.io/crates/slog-scope
Source0:        https://static.crates.io/crates/slog-scope/slog-scope-%{version}.crate
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
Summary:        Logging scopes for slog-rs
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
%files -n rust-slog-scope-devel -f %{oreon_filedir}/rust-slog-scope-devel.list

%changelog

%autochangelog
