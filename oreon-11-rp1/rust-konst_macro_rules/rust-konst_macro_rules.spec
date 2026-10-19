%global source0_hash a4933f3f57a8e9d9da04db23fb153356ecaf00cbd14aee46279c33dc80925c37
%bcond check 0
%global debug_package %{nil}
%global crate konst_macro_rules
Name:           rust-konst_macro_rules
Version:        0.2.19
Release:        1%{?dist}
Summary:        Implementation detail of the konst crate
License:        Zlib
URL:            https://crates.io/crates/konst_macro_rules
Source0:        https://static.crates.io/crates/konst_macro_rules/konst_macro_rules-%{version}.crate
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
Summary:        Implementation detail of the konst crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+deref_raw_in_fn-devel
Summary:        Implementation detail of the konst crate
BuildArch:      noarch
%description -n %{name}+deref_raw_in_fn-devel

This package contains library source intended for building other packages which
use the "deref_raw_in_fn" feature of the "%{crate}" crate.

%package     -n %{name}+mut_refs-devel
Summary:        Implementation detail of the konst crate
BuildArch:      noarch
%description -n %{name}+mut_refs-devel

This package contains library source intended for building other packages which
use the "mut_refs" feature of the "%{crate}" crate.

%package     -n %{name}+nightly_mut_refs-devel
Summary:        Implementation detail of the konst crate
BuildArch:      noarch
%description -n %{name}+nightly_mut_refs-devel

This package contains library source intended for building other packages which
use the "nightly_mut_refs" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_51-devel
Summary:        Implementation detail of the konst crate
BuildArch:      noarch
%description -n %{name}+rust_1_51-devel

This package contains library source intended for building other packages which
use the "rust_1_51" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_55-devel
Summary:        Implementation detail of the konst crate
BuildArch:      noarch
%description -n %{name}+rust_1_55-devel

This package contains library source intended for building other packages which
use the "rust_1_55" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_56-devel
Summary:        Implementation detail of the konst crate
BuildArch:      noarch
%description -n %{name}+rust_1_56-devel

This package contains library source intended for building other packages which
use the "rust_1_56" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_57-devel
Summary:        Implementation detail of the konst crate
BuildArch:      noarch
%description -n %{name}+rust_1_57-devel

This package contains library source intended for building other packages which
use the "rust_1_57" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_61-devel
Summary:        Implementation detail of the konst crate
BuildArch:      noarch
%description -n %{name}+rust_1_61-devel

This package contains library source intended for building other packages which
use the "rust_1_61" feature of the "%{crate}" crate.

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
%files -n rust-konst_macro_rules-devel -f %{oreon_filedir}/rust-konst_macro_rules-devel.list

%changelog

%autochangelog
