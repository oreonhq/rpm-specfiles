%global source0_hash e3df53c20ec0ce366a7fbda4a6bfea70a72c8630a26afa9f0e4b0f927163b975
%bcond check 1
%global debug_package %{nil}
%global crate nu-json
Name:           rust-nu-json
Version:        0.99.1
Release:        1%{?dist}
Summary:        Fork of serde-hjson
License:        MIT
URL:            https://crates.io/crates/nu-json
Source0:        https://static.crates.io/crates/nu-json/nu-json-%{version}.crate
Patch:          nu-json-fix-metadata.diff
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
Summary:        Fork of serde-hjson
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+linked-hash-map-devel
Summary:        Fork of serde-hjson
BuildArch:      noarch
%description -n %{name}+linked-hash-map-devel

This package contains library source intended for building other packages which
use the "linked-hash-map" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        Fork of serde-hjson
BuildArch:      noarch
%description -n %{name}+preserve_order-devel

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip test_hjson
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-nu-json-devel -f %{oreon_filedir}/rust-nu-json-devel.list

%changelog

%autochangelog
