%global source0_hash c1e04941e6acf6d42b8ff109e35a0f0237334aee1bfd7ad43a7f18d38451e0d9
%bcond check 0
%global debug_package %{nil}
%global crate dcv-color-primitives
Name:           rust-dcv-color-primitives
Version:        1.0.0
Release:        1%{?dist}
Summary:        a library to perform image color model conversion
License:        MIT-0
URL:            https://crates.io/crates/dcv-color-primitives
Source0:        https://static.crates.io/crates/dcv-color-primitives/dcv-color-primitives-%{version}.crate
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

%package     -n %{name}+test_instruction_sets-devel
Summary:        a library to perform image color model conversion
BuildArch:      noarch
%description -n %{name}+test_instruction_sets-devel

This package contains library source intended for building other packages which
use the "test_instruction_sets" feature of the "%{crate}" crate.

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
%files -n rust-dcv-color-primitives-devel -f %{oreon_filedir}/rust-dcv-color-primitives-devel.list

%changelog

%autochangelog
