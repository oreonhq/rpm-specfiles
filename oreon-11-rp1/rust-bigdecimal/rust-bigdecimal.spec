%global source0_hash 4d6867f1565b3aad85681f1015055b087fcfd840d6aeee6eee7f2da317603695
%bcond check 0
%global debug_package %{nil}
%global crate bigdecimal
Name:           rust-bigdecimal
Version:        0.4.10
Release:        1%{?dist}
Summary:        Arbitrary precision decimal numbers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bigdecimal
Source0:        https://static.crates.io/crates/bigdecimal/bigdecimal-%{version}.crate
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
Summary:        Arbitrary precision decimal numbers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Arbitrary precision decimal numbers
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-json-devel
Summary:        Arbitrary precision decimal numbers
BuildArch:      noarch
%description -n %{name}+serde-json-devel

This package contains library source intended for building other packages which
use the "serde-json" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Arbitrary precision decimal numbers
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Arbitrary precision decimal numbers
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+string-only-devel
Summary:        Arbitrary precision decimal numbers
BuildArch:      noarch
%description -n %{name}+string-only-devel

This package contains library source intended for building other packages which
use the "string-only" feature of the "%{crate}" crate.

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
%files -n rust-bigdecimal-devel -f %{oreon_filedir}/rust-bigdecimal-devel.list

%changelog

%autochangelog
