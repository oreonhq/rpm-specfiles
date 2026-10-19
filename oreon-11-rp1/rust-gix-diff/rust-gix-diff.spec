%global source0_hash 1b1689ff5ddeee4acfb2a43e875a1072a76d208624b15a9065c938b39cb0da2a
%bcond check 0
%global debug_package %{nil}
%global crate gix-diff
Name:           rust-gix-diff
Version:        0.67.1
Release:        1%{?dist}
Summary:        Calculate differences between various git objects
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-diff
Source0:        https://static.crates.io/crates/gix-diff/gix-diff-%{version}.crate
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
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+blob-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+blob-devel

This package contains library source intended for building other packages which
use the "blob" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+index-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+index-devel

This package contains library source intended for building other packages which
use the "index" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+wasm-devel

This package contains library source intended for building other packages which
use the "wasm" feature of the "%{crate}" crate.

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
%files -n rust-gix-diff-devel -f %{oreon_filedir}/rust-gix-diff-devel.list

%changelog

%autochangelog
