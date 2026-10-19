%global source0_hash 3eb5bfde6e3d6c97a8ecc16860d67d5f7d45dd45ee2228155b4a7918708a87f2
%bcond check 0
%global debug_package %{nil}
%global crate testing_table
Name:           rust-testing_table
Version:        0.1.1
Release:        1%{?dist}
Summary:        Easy to use library for pretty print tables of Rust structs and enums
License:        MIT
URL:            https://crates.io/crates/testing_table
Source0:        https://static.crates.io/crates/testing_table/testing_table-%{version}.crate
Patch:          testing_table-fix-metadata.diff
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
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansi-devel
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+ansi-devel

This package contains library source intended for building other packages which
use the "ansi" feature of the "%{crate}" crate.

%package     -n %{name}+ansitok-devel
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+ansitok-devel

This package contains library source intended for building other packages which
use the "ansitok" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE1} .
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
%files -n rust-testing_table-devel -f %{oreon_filedir}/rust-testing_table-devel.list

%changelog

%autochangelog
