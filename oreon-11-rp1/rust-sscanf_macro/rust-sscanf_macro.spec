%global source0_hash 77faf04b02dc0dd55e6713fcae44aa6e8882570bae2bd873949924d6e57cca82
%bcond check 1
%global debug_package %{nil}
%global crate sscanf_macro
Name:           rust-sscanf_macro
Version:        0.4.4
Release:        1%{?dist}
Summary:        Proc-Macros for the sscanf Crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sscanf_macro
Source0:        https://static.crates.io/crates/sscanf_macro/sscanf_macro-%{version}.crate
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
Summary:        Proc-Macros for the sscanf Crate
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
%files -n rust-sscanf_macro-devel -f %{oreon_filedir}/rust-sscanf_macro-devel.list

%changelog

%autochangelog
