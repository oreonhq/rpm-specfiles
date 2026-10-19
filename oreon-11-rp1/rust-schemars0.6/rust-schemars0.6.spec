%global source0_hash 07569773d6aaf3324812c6572244aec08521b64ce056f2be3b5cc135fb63caec
%bcond check 0
%global debug_package %{nil}
%global crate schemars
Name:           rust-schemars0.6
Version:        0.6.5
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

%package     -n %{name}+arrayvec-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+arrayvec-devel

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+derive_json_schema-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+derive_json_schema-devel

This package contains library source intended for building other packages which
use the "derive_json_schema" feature of the "%{crate}" crate.

%package     -n %{name}+either-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+either-devel

This package contains library source intended for building other packages which
use the "either" feature of the "%{crate}" crate.

%package     -n %{name}+impl_json_schema-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+impl_json_schema-devel

This package contains library source intended for building other packages which
use the "impl_json_schema" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Generate JSON Schemas from Rust code
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

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
%files -n rust-schemars0.6-devel -f %{oreon_filedir}/rust-schemars0.6-devel.list

%changelog

%autochangelog
