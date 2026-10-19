%global source0_hash a8855baff5d450715f5d34c1d291a8c77363bd5a20ddacf560d7d6ea2a07f2c3
%bcond check 0
%global debug_package %{nil}
%global crate extract_map
Name:           rust-extract_map
Version:        0.3.1
Release:        1%{?dist}
Summary:        A HashMap for memory efficent storage of value types which contain th...
License:        MIT
URL:            https://crates.io/crates/extract_map
Source0:        https://static.crates.io/crates/extract_map/extract_map-%{version}.crate
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

%package     -n %{name}+gat-lending-iterator-devel
Summary:        A HashMap for memory efficent storage of value types which contain th...
BuildArch:      noarch
%description -n %{name}+gat-lending-iterator-devel

This package contains library source intended for building other packages which
use the "gat-lending-iterator" feature of the "%{crate}" crate.

%package     -n %{name}+iter_mut-devel
Summary:        A HashMap for memory efficent storage of value types which contain th...
BuildArch:      noarch
%description -n %{name}+iter_mut-devel

This package contains library source intended for building other packages which
use the "iter_mut" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A HashMap for memory efficent storage of value types which contain th...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-extract_map-devel -f %{oreon_filedir}/rust-extract_map-devel.list

%changelog

%autochangelog
