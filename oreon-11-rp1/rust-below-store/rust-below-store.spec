%global source0_hash 60bf6c6add4f6bf3f2db68d64dbd6f352fe8459ae0331c7893301995b2b6cc38
%bcond check 1
%global debug_package %{nil}
%global crate below-store
%global unsupported_arches %{ix86}
Name:           rust-below-store
Version:        0.9.0
Release:        1%{?dist}
Summary:        Store crate for below
License:        Apache-2.0
URL:            https://crates.io/crates/below-store
Source0:        https://static.crates.io/crates/below-store/below-store-%{version}.crate
Patch:          below-store-fix-metadata.diff
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
Summary:        Store crate for below
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+no-vendor-devel
Summary:        Store crate for below
BuildArch:      noarch
%description -n %{name}+no-vendor-devel

This package contains library source intended for building other packages which
use the "no-vendor" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifnarch %{unsupported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifnarch %{unsupported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-below-store-devel -f %{oreon_filedir}/rust-below-store-devel.list

%changelog

%autochangelog
