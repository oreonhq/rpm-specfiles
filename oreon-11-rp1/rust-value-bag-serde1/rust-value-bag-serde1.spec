%global source0_hash 5b92170db3db8a6354f12a5b7f13a5453928433e08fc46aee51eedfa8f7a28a1
%bcond check 0
%global debug_package %{nil}
%global crate value-bag-serde1
Name:           rust-value-bag-serde1
Version:        1.13.1
Release:        1%{?dist}
Summary:        Implementation detail for value-bag
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/value-bag-serde1
Source0:        https://static.crates.io/crates/value-bag-serde1/value-bag-serde1-%{version}.crate
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

%package     -n %{name}+owned-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+owned-devel

This package contains library source intended for building other packages which
use the "owned" feature of the "%{crate}" crate.

%package     -n %{name}+serde_buf-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+serde_buf-devel

This package contains library source intended for building other packages which
use the "serde_buf" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+serde_test-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+serde_test-devel

This package contains library source intended for building other packages which
use the "serde_test" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Implementation detail for value-bag
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-value-bag-serde1-devel -f %{oreon_filedir}/rust-value-bag-serde1-devel.list

%changelog

%autochangelog
