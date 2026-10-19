%global source0_hash 36eaf5d7b090263e8150820482d5d93cd964a81e4019913c972f4edcc6edb740
%bcond check 0
%global debug_package %{nil}
%global crate bincode
Name:           rust-bincode2
Version:        2.0.1
Release:        1%{?dist}
Summary:        A binary serialization / deserialization strategy for transforming st...
License:        MIT
URL:            https://crates.io/crates/bincode
Source0:        https://static.crates.io/crates/bincode/bincode-%{version}.crate
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
Summary:        A binary serialization / deserialization strategy for transforming st...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A binary serialization / deserialization strategy for transforming st...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+bincode_derive-devel
Summary:        A binary serialization / deserialization strategy for transforming st...
BuildArch:      noarch
%description -n %{name}+bincode_derive-devel

This package contains library source intended for building other packages which
use the "bincode_derive" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        A binary serialization / deserialization strategy for transforming st...
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A binary serialization / deserialization strategy for transforming st...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A binary serialization / deserialization strategy for transforming st...
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
%files -n rust-bincode2-devel -f %{oreon_filedir}/rust-bincode2-devel.list

%changelog

%autochangelog
