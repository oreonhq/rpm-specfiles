%global source0_hash eae1c5aaf1bfdc24a9b5bf6daf3afee62c478afe08706a6bd9fd996f73630494
%bcond check 1
%global debug_package %{nil}
%global crate easy-cast
Name:           rust-easy-cast
Version:        0.7.1
Release:        1%{?dist}
Summary:        Type conversions which are expected to succeed
License:        Apache-2.0
URL:            https://crates.io/crates/easy-cast
Source0:        https://static.crates.io/crates/easy-cast/easy-cast-%{version}.crate
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
Summary:        Type conversions which are expected to succeed
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+always_assert-devel
Summary:        Type conversions which are expected to succeed
BuildArch:      noarch
%description -n %{name}+always_assert-devel

This package contains library source intended for building other packages which
use the "always_assert" feature of the "%{crate}" crate.

%package     -n %{name}+assert_digits-devel
Summary:        Type conversions which are expected to succeed
BuildArch:      noarch
%description -n %{name}+assert_digits-devel

This package contains library source intended for building other packages which
use the "assert_digits" feature of the "%{crate}" crate.

%package     -n %{name}+assert_float-devel
Summary:        Type conversions which are expected to succeed
BuildArch:      noarch
%description -n %{name}+assert_float-devel

This package contains library source intended for building other packages which
use the "assert_float" feature of the "%{crate}" crate.

%package     -n %{name}+assert_int-devel
Summary:        Type conversions which are expected to succeed
BuildArch:      noarch
%description -n %{name}+assert_int-devel

This package contains library source intended for building other packages which
use the "assert_int" feature of the "%{crate}" crate.

%package     -n %{name}+assert_nonzero-devel
Summary:        Type conversions which are expected to succeed
BuildArch:      noarch
%description -n %{name}+assert_nonzero-devel

This package contains library source intended for building other packages which
use the "assert_nonzero" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        Type conversions which are expected to succeed
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Type conversions which are expected to succeed
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

%{cargo_test -- -- --exact %{shrink:
    --skip approx_nan
    --skip approx_f64_f32
    --skip float_trunc_fail1
    --skip int_to_float_inexact
    --skip signed_to_unsigned_n1
    --skip u128_large_to_f32
    --skip u32_max_f32
    --skip unsigned_to_signed_large
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-easy-cast-devel -f %{oreon_filedir}/rust-easy-cast-devel.list

%changelog

%autochangelog
