%global source0_hash 1a1e4b117c4e8177c359b14cbea439ff70c4d8c91f81f1361c49987f8890e8c7
%bcond check 0
%global debug_package %{nil}
%global crate subplot-build
Name:           rust-subplot-build
Version:        0.13.0
Release:        1%{?dist}
Summary:        A library for using Subplot code generation from another project's
License:        MIT-0
URL:            https://crates.io/crates/subplot-build
Source0:        https://static.crates.io/crates/subplot-build/subplot-build-%{version}.crate
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
Summary:        A library for using Subplot code generation from another project's
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
%files -n rust-subplot-build-devel -f %{oreon_filedir}/rust-subplot-build-devel.list

%changelog

%autochangelog
