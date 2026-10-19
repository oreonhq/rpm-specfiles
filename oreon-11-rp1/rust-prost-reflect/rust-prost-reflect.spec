%global source0_hash 01b80ea363c31af2de2b92e3c07ed1156628f7838c4afb4df75ee78a37fedbd1
%bcond check 1
%global debug_package %{nil}
%global crate prost-reflect
Name:           rust-prost-reflect
Version:        0.16.5
Release:        1%{?dist}
Summary:        Protobuf library extending prost with reflection support and dynamic messages
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/prost-reflect
Source0:        https://static.crates.io/crates/prost-reflect/prost-reflect-%{version}.crate
Patch:          prost-reflect-fix-metadata.diff
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
Summary:        Protobuf library extending prost with reflection support and dynamic messages
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+miette-devel
Summary:        Protobuf library extending prost with reflection support and dynamic messages
BuildArch:      noarch
%description -n %{name}+miette-devel

This package contains library source intended for building other packages which
use the "miette" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Protobuf library extending prost with reflection support and dynamic messages
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+text-format-devel
Summary:        Protobuf library extending prost with reflection support and dynamic messages
BuildArch:      noarch
%description -n %{name}+text-format-devel

This package contains library source intended for building other packages which
use the "text-format" feature of the "%{crate}" crate.

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
%files -n rust-prost-reflect-devel -f %{oreon_filedir}/rust-prost-reflect-devel.list

%changelog

%autochangelog
