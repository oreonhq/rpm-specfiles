%global source0_hash 3091d68264354f211516b91dce6f71046e444fab1867716035f736667243affb
%bcond check 1
%global debug_package %{nil}
%global crate auto_enums
Name:           rust-auto_enums
Version:        0.8.10
Release:        1%{?dist}
Summary:        Library for to allow multiple return types by automatically generated enum
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/auto_enums
Source0:        https://static.crates.io/crates/auto_enums/auto_enums-%{version}.crate
Patch:          auto_enums-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+convert-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+convert-devel

This package contains library source intended for building other packages which
use the "convert" feature of the "%{crate}" crate.

%package     -n %{name}+coroutine_trait-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+coroutine_trait-devel

This package contains library source intended for building other packages which
use the "coroutine_trait" feature of the "%{crate}" crate.

%package     -n %{name}+fmt-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+fmt-devel

This package contains library source intended for building other packages which
use the "fmt" feature of the "%{crate}" crate.

%package     -n %{name}+fn_traits-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+fn_traits-devel

This package contains library source intended for building other packages which
use the "fn_traits" feature of the "%{crate}" crate.

%package     -n %{name}+futures03-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+futures03-devel

This package contains library source intended for building other packages which
use the "futures03" feature of the "%{crate}" crate.

%package     -n %{name}+generator_trait-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+generator_trait-devel

This package contains library source intended for building other packages which
use the "generator_trait" feature of the "%{crate}" crate.

%package     -n %{name}+http_body1-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+http_body1-devel

This package contains library source intended for building other packages which
use the "http_body1" feature of the "%{crate}" crate.

%package     -n %{name}+ops-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+ops-devel

This package contains library source intended for building other packages which
use the "ops" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tokio1-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+tokio1-devel

This package contains library source intended for building other packages which
use the "tokio1" feature of the "%{crate}" crate.

%package     -n %{name}+transpose_methods-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+transpose_methods-devel

This package contains library source intended for building other packages which
use the "transpose_methods" feature of the "%{crate}" crate.

%package     -n %{name}+trusted_len-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+trusted_len-devel

This package contains library source intended for building other packages which
use the "trusted_len" feature of the "%{crate}" crate.

%package     -n %{name}+type_analysis-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+type_analysis-devel

This package contains library source intended for building other packages which
use the "type_analysis" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Library for to allow multiple return types by automatically generated enum
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tomcli set Cargo.toml arrays delitem --key path test tests/compiletest.rs
tomcli set Cargo.toml arrays delitem --key path test tests/expandtest.rs
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
%files -n rust-auto_enums-devel -f %{oreon_filedir}/rust-auto_enums-devel.list

%changelog

%autochangelog
