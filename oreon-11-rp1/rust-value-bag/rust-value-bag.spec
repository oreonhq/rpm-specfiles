%global source0_hash 2799ffb329a792ecfd902b71306c8a815a6ef1c0470fa9953a6aa4d4cecbe511
%bcond check 0
%global debug_package %{nil}
%global crate value-bag
Name:           rust-value-bag
Version:        1.14.1
Release:        1%{?dist}
Summary:        Anonymous structured values
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/value-bag
Source0:        https://static.crates.io/crates/value-bag/value-bag-%{version}.crate
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
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+error-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+error-devel

This package contains library source intended for building other packages which
use the "error" feature of the "%{crate}" crate.

%package     -n %{name}+inline-i128-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+inline-i128-devel

This package contains library source intended for building other packages which
use the "inline-i128" feature of the "%{crate}" crate.

%package     -n %{name}+inline-str-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+inline-str-devel

This package contains library source intended for building other packages which
use the "inline-str" feature of the "%{crate}" crate.

%package     -n %{name}+inline-str-l-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+inline-str-l-devel

This package contains library source intended for building other packages which
use the "inline-str-l" feature of the "%{crate}" crate.

%package     -n %{name}+owned-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+owned-devel

This package contains library source intended for building other packages which
use the "owned" feature of the "%{crate}" crate.

%package     -n %{name}+seq-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+seq-devel

This package contains library source intended for building other packages which
use the "seq" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde1-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+serde1-devel

This package contains library source intended for building other packages which
use the "serde1" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+sval-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+sval-devel

This package contains library source intended for building other packages which
use the "sval" feature of the "%{crate}" crate.

%package     -n %{name}+sval2-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+sval2-devel

This package contains library source intended for building other packages which
use the "sval2" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%package     -n %{name}+value-bag-serde1-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+value-bag-serde1-devel

This package contains library source intended for building other packages which
use the "value-bag-serde1" feature of the "%{crate}" crate.

%package     -n %{name}+value-bag-sval2-devel
Summary:        Anonymous structured values
BuildArch:      noarch
%description -n %{name}+value-bag-sval2-devel

This package contains library source intended for building other packages which
use the "value-bag-sval2" feature of the "%{crate}" crate.

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
%files -n rust-value-bag-devel -f %{oreon_filedir}/rust-value-bag-devel.list

%changelog

%autochangelog
