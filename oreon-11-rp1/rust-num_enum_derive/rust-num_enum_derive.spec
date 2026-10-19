%global source0_hash 680998035259dcfcafe653688bf2aa6d3e2dc05e98be6ab46afb089dc84f1df8
%bcond check 0
%global debug_package %{nil}
%global crate num_enum_derive
Name:           rust-num_enum_derive
Version:        0.7.6
Release:        1%{?dist}
Summary:        Internal implementation details for num_enum
License:        BSD-3-Clause OR MIT OR Apache-2.0
URL:            https://crates.io/crates/num_enum_derive
Source0:        https://static.crates.io/crates/num_enum_derive/num_enum_derive-%{version}.crate
Patch:          num_enum_derive-fix-metadata.diff
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
Summary:        Internal implementation details for num_enum
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+complex-expressions-devel
Summary:        Internal implementation details for num_enum
BuildArch:      noarch
%description -n %{name}+complex-expressions-devel

This package contains library source intended for building other packages which
use the "complex-expressions" feature of the "%{crate}" crate.

%package     -n %{name}+external_doc-devel
Summary:        Internal implementation details for num_enum
BuildArch:      noarch
%description -n %{name}+external_doc-devel

This package contains library source intended for building other packages which
use the "external_doc" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro-crate-devel
Summary:        Internal implementation details for num_enum
BuildArch:      noarch
%description -n %{name}+proc-macro-crate-devel

This package contains library source intended for building other packages which
use the "proc-macro-crate" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Internal implementation details for num_enum
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
%files -n rust-num_enum_derive-devel -f %{oreon_filedir}/rust-num_enum_derive-devel.list

%changelog

%autochangelog
