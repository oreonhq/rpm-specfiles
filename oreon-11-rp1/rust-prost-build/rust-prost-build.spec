%global source0_hash 03da047801ff44bb6a4d407d4860c05fd70bb81714e6b2f3812603d5b145b042
%bcond check 1
%global debug_package %{nil}
%global crate prost-build
Name:           rust-prost-build
Version:        0.14.4
Release:        1%{?dist}
Summary:        Generate Prost annotated Rust types from Protocol Buffers files
License:        Apache-2.0
URL:            https://crates.io/crates/prost-build
Source0:        https://static.crates.io/crates/prost-build/prost-build-%{version}.crate
Patch:          prost-build-fix-metadata.diff
# oreon:deps
BuildRequires:  /usr/bin/protoc
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       /usr/bin/protoc
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Generate Prost annotated Rust types from Protocol Buffers files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+format-devel
Summary:        Generate Prost annotated Rust types from Protocol Buffers files
BuildArch:      noarch
%description -n %{name}+format-devel

This package contains library source intended for building other packages which
use the "format" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip tests::test_generate_no_empty_outputs
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-prost-build-devel -f %{oreon_filedir}/rust-prost-build-devel.list

%changelog

%autochangelog
