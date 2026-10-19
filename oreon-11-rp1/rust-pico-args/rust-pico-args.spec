%global source0_hash 5be167a7af36ee22fe3115051bc51f6e6c7054c9348e28deb4f49bd6f705a315
%bcond check 0
%global debug_package %{nil}
%global crate pico-args
Name:           rust-pico-args
Version:        0.5.0
Release:        1%{?dist}
Summary:        An ultra simple CLI arguments parser.
License:        MIT
URL:            https://crates.io/crates/pico-args
Source0:        https://static.crates.io/crates/pico-args/pico-args-%{version}.crate
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
Summary:        An ultra simple CLI arguments parser.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+combined-flags-devel
Summary:        An ultra simple CLI arguments parser.
BuildArch:      noarch
%description -n %{name}+combined-flags-devel

This package contains library source intended for building other packages which
use the "combined-flags" feature of the "%{crate}" crate.

%package     -n %{name}+eq-separator-devel
Summary:        An ultra simple CLI arguments parser.
BuildArch:      noarch
%description -n %{name}+eq-separator-devel

This package contains library source intended for building other packages which
use the "eq-separator" feature of the "%{crate}" crate.

%package     -n %{name}+short-space-opt-devel
Summary:        An ultra simple CLI arguments parser.
BuildArch:      noarch
%description -n %{name}+short-space-opt-devel

This package contains library source intended for building other packages which
use the "short-space-opt" feature of the "%{crate}" crate.

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
%files -n rust-pico-args-devel -f %{oreon_filedir}/rust-pico-args-devel.list

%changelog

%autochangelog
