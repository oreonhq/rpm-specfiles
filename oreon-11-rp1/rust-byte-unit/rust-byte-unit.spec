%global source0_hash 4a813de7f2bbedb7dce265b64f1cf5908ebe4d56281ece8d847e98113788b9b0
%bcond check 0
%global debug_package %{nil}
%global crate byte-unit
Name:           rust-byte-unit
Version:        5.2.5
Release:        1%{?dist}
Summary:        A library for interacting with units of bytes.
License:        MIT
URL:            https://crates.io/crates/byte-unit
Source0:        https://static.crates.io/crates/byte-unit/byte-unit-%{version}.crate
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
Summary:        A library for interacting with units of bytes.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bit-devel
Summary:        A library for interacting with units of bytes.
BuildArch:      noarch
%description -n %{name}+bit-devel

This package contains library source intended for building other packages which
use the "bit" feature of the "%{crate}" crate.

%package     -n %{name}+byte-devel
Summary:        A library for interacting with units of bytes.
BuildArch:      noarch
%description -n %{name}+byte-devel

This package contains library source intended for building other packages which
use the "byte" feature of the "%{crate}" crate.

%package     -n %{name}+rocket-devel
Summary:        A library for interacting with units of bytes.
BuildArch:      noarch
%description -n %{name}+rocket-devel

This package contains library source intended for building other packages which
use the "rocket" feature of the "%{crate}" crate.

%package     -n %{name}+rust_decimal-devel
Summary:        A library for interacting with units of bytes.
BuildArch:      noarch
%description -n %{name}+rust_decimal-devel

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+schemars-devel
Summary:        A library for interacting with units of bytes.
BuildArch:      noarch
%description -n %{name}+schemars-devel

This package contains library source intended for building other packages which
use the "schemars" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A library for interacting with units of bytes.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A library for interacting with units of bytes.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+u128-devel
Summary:        A library for interacting with units of bytes.
BuildArch:      noarch
%description -n %{name}+u128-devel

This package contains library source intended for building other packages which
use the "u128" feature of the "%{crate}" crate.

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
%files -n rust-byte-unit-devel -f %{oreon_filedir}/rust-byte-unit-devel.list

%changelog

%autochangelog
