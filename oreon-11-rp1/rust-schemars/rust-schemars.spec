%global source0_hash 687274d293b6cdc6e73e0fee520bf2049650090d7164f87672d212a3c530cf4a
%bcond check 0
%global debug_package %{nil}
%global crate schemars
Name:           rust-schemars
Version:        1.2.2
Release:        1%{?dist}
Summary:        Generate JSON Schemas from Rust code
License:        MIT
URL:            https://crates.io/crates/schemars
Source0:        https://static.crates.io/crates/schemars/schemars-%{version}.crate
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
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+_ui_test-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+_ui_test-devel

This package contains library source intended for building other packages which
use the "_ui_test" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+preserve_order-devel

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

%package     -n %{name}+raw_value-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+raw_value-devel

This package contains library source intended for building other packages which
use the "raw_value" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-schemars-devel -f %{oreon_filedir}/rust-schemars-devel.list

%changelog

%autochangelog
