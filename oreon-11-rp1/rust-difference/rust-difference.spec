%global source0_hash 524cbf6897b527295dff137cec09ecf3a05f4fddffd7dfcd1585403449e74198
%bcond_without check
%global debug_package %{nil}
%global crate difference
Name:           rust-difference
Version:        2.0.0
Release:        1%{?dist}
Summary:        Rust text diffing and assertion library
License:        MIT
URL:            https://crates.io/crates/difference
Source0:        https://static.crates.io/crates/difference/difference-%{version}.crate
Patch:          difference-fix-metadata.diff
Patch:          0001-Fix-inclusive-range.patch
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
Summary:        Rust text diffing and assertion library
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
%files -n rust-difference-devel -f %{oreon_filedir}/rust-difference-devel.list

%changelog

%autochangelog
