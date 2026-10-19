%global source0_hash d5d61999272074fd54f3eda7afbfa3f781b0d62ddb89be28fdf56bce30e23576
%bcond check 1
%global debug_package %{nil}
%global crate hecs
Name:           rust-hecs
Version:        0.11.1
Release:        1%{?dist}
Summary:        Fast, minimal, and ergonomic entity-component-system library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hecs
Source0:        https://static.crates.io/crates/hecs/hecs-%{version}.crate
Patch:          hecs-fix-metadata.diff
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
Summary:        Fast, minimal, and ergonomic entity-component-system library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+column-serialize-devel
Summary:        Fast, minimal, and ergonomic entity-component-system library
BuildArch:      noarch
%description -n %{name}+column-serialize-devel

This package contains library source intended for building other packages which
use the "column-serialize" feature of the "%{crate}" crate.

%package     -n %{name}+hecs-macros-devel
Summary:        Fast, minimal, and ergonomic entity-component-system library
BuildArch:      noarch
%description -n %{name}+hecs-macros-devel

This package contains library source intended for building other packages which
use the "hecs-macros" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Fast, minimal, and ergonomic entity-component-system library
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+row-serialize-devel
Summary:        Fast, minimal, and ergonomic entity-component-system library
BuildArch:      noarch
%description -n %{name}+row-serialize-devel

This package contains library source intended for building other packages which
use the "row-serialize" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Fast, minimal, and ergonomic entity-component-system library
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fast, minimal, and ergonomic entity-component-system library
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
%files -n rust-hecs-devel -f %{oreon_filedir}/rust-hecs-devel.list

%changelog

%autochangelog
