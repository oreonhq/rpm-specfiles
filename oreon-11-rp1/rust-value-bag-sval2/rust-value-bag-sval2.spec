%global source0_hash 0bf9832097ca044466ae3f1aa43a943d4e450b7c3b8cdf65363875df07da79a0
%bcond check 0
%global debug_package %{nil}
%global crate value-bag-sval2
Name:           rust-value-bag-sval2
Version:        1.13.1
Release:        1%{?dist}
Summary:        Implementation detail for value-bag
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/value-bag-sval2
Source0:        https://static.crates.io/crates/value-bag-sval2/value-bag-sval2-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+serde1-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+serde1-devel

This package contains library source intended for building other packages which
use the "serde1" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+sval_json-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+sval_json-devel

This package contains library source intended for building other packages which
use the "sval_json" feature of the "%{crate}" crate.

%package     -n %{name}+sval_serde-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+sval_serde-devel

This package contains library source intended for building other packages which
use the "sval_serde" feature of the "%{crate}" crate.

%package     -n %{name}+sval_test-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+sval_test-devel

This package contains library source intended for building other packages which
use the "sval_test" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

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
%files -n rust-value-bag-sval2-devel -f %{oreon_filedir}/rust-value-bag-sval2-devel.list

%changelog

%autochangelog
