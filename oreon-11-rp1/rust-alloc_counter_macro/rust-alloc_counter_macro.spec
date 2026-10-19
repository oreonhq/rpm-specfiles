%global source0_hash 1a52f81f9add01deacdc1fcb05ba09523a8faefdec6c3f69cb752b9fa9c22e5a
%bcond check 0
%global debug_package %{nil}
%global crate alloc_counter_macro
Name:           rust-alloc_counter_macro
Version:        0.0.2
Release:        1%{?dist}
Summary:        The #[no_alloc] macro for the alloc_counter crate.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/alloc_counter_macro
Source0:        https://static.crates.io/crates/alloc_counter_macro/alloc_counter_macro-%{version}.crate
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
Summary:        The #[no_alloc] macro for the alloc_counter crate.
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
%files -n rust-alloc_counter_macro-devel -f %{oreon_filedir}/rust-alloc_counter_macro-devel.list

%changelog

%autochangelog
