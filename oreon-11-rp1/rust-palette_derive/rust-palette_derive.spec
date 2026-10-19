%global source0_hash f5030daf005bface118c096f510ffb781fc28f9ab6a32ab224d8631be6851d30
%bcond check 0
%global debug_package %{nil}
%global crate palette_derive
Name:           rust-palette_derive
Version:        0.7.6
Release:        1%{?dist}
Summary:        Automatically implement traits from the palette crate.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/palette_derive
Source0:        https://static.crates.io/crates/palette_derive/palette_derive-%{version}.crate
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

%package     -n %{name}+find-crate-devel
Summary:        Automatically implement traits from the palette crate.
BuildArch:      noarch
%description -n %{name}+find-crate-devel

This package contains library source intended for building other packages which
use the "find-crate" feature of the "%{crate}" crate.

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
%files -n rust-palette_derive-devel -f %{oreon_filedir}/rust-palette_derive-devel.list

%changelog

%autochangelog
