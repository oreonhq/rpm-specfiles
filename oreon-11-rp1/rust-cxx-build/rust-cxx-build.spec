%global source0_hash 4fde53ca86b9704a943fef0f1e1d836239a6aedca5de3c65fa9f97ec0bd46d39
%bcond check 0
%global debug_package %{nil}
%global crate cxx-build
Name:           rust-cxx-build
Version:        1.0.202
Release:        1%{?dist}
Summary:        C++ code generator for integrating cxx crate into a Cargo build
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cxx-build
Source0:        https://static.crates.io/crates/cxx-build/cxx-build-%{version}.crate
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
Summary:        C++ code generator for integrating cxx crate into a Cargo build
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        C++ code generator for integrating cxx crate into a Cargo build
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

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
%files -n rust-cxx-build-devel -f %{oreon_filedir}/rust-cxx-build-devel.list

%changelog

%autochangelog
