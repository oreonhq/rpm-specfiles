%global source0_hash aa9c45b374136f52f2d6311062c7146bff20fec063c3f5d46a410bd937746955
%bcond check 0
%global debug_package %{nil}
%global crate rustc-std-workspace-core
Name:           rust-rustc-std-workspace-core
Version:        1.0.1
Release:        1%{?dist}
Summary:        crate for integration of crates.io crates into rust-lang/rust standar...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustc-std-workspace-core
Source0:        https://static.crates.io/crates/rustc-std-workspace-core/rustc-std-workspace-core-%{version}.crate
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
Summary:        crate for integration of crates.io crates into rust-lang/rust standar...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-rustc-std-workspace-core-devel -f %{oreon_filedir}/rust-rustc-std-workspace-core-devel.list

%changelog

%autochangelog
