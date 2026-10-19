%global source0_hash 71dd52191aae121e8611f1e8dc3e324dd0dd1dee1e6dd91d10ee07a3cfb4d9d8
%bcond check 1
%global debug_package %{nil}
%global crate interpolator
Name:           rust-interpolator
Version:        0.5.0
Release:        1%{?dist}
Summary:        Runtime format strings, fully compatible with std's macros
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/interpolator
Source0:        https://static.crates.io/crates/interpolator/interpolator-%{version}.crate
Patch:          interpolator-fix-metadata.diff
Patch10:        0001-Downstream-only-ignore-test-that-requires-assert-dbg.patch
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
Summary:        Runtime format strings, fully compatible with std's macros
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Runtime format strings, fully compatible with std's macros
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+iter-devel
Summary:        Runtime format strings, fully compatible with std's macros
BuildArch:      noarch
%description -n %{name}+iter-devel

This package contains library source intended for building other packages which
use the "iter" feature of the "%{crate}" crate.

%package     -n %{name}+number-devel
Summary:        Runtime format strings, fully compatible with std's macros
BuildArch:      noarch
%description -n %{name}+number-devel

This package contains library source intended for building other packages which
use the "number" feature of the "%{crate}" crate.

%package     -n %{name}+pointer-devel
Summary:        Runtime format strings, fully compatible with std's macros
BuildArch:      noarch
%description -n %{name}+pointer-devel

This package contains library source intended for building other packages which
use the "pointer" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-interpolator-devel -f %{oreon_filedir}/rust-interpolator-devel.list

%changelog

%autochangelog
