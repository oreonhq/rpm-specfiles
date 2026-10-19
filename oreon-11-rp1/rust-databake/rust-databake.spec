%global source0_hash 74d4b1db5ca40636726f1f73daff0d626accbd49bcd8136fcade87d7cf1e6bbb
%bcond check 0
%global debug_package %{nil}
%global crate databake
Name:           rust-databake
Version:        0.2.1
Release:        1%{?dist}
Summary:        Trait that lets structs represent themselves as (const) Rust expressions
License:        Unicode-3.0
URL:            https://crates.io/crates/databake
Source0:        https://static.crates.io/crates/databake/databake-%{version}.crate
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

%package     -n %{name}+derive-devel
Summary:        Trait that lets structs represent themselves as (const) Rust expressions
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

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
%files -n rust-databake-devel -f %{oreon_filedir}/rust-databake-devel.list

%changelog

%autochangelog
