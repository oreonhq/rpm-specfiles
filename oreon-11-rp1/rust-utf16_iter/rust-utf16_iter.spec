%global source0_hash c8232dd3cdaed5356e0f716d285e4b40b932ac434100fe9b7e0e8e935b9e6246
%bcond check 0
%global debug_package %{nil}
%global crate utf16_iter
Name:           rust-utf16_iter
Version:        1.0.5
Release:        2%{?dist}
Summary:        Iterator by char over potentially-invalid UTF-16 in &[u16]
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/utf16_iter
Source0:        https://static.crates.io/crates/utf16_iter/utf16_iter-%{version}.crate
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
Summary:        Iterator by char over potentially-invalid UTF-16 in &[u16]
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
%files -n rust-utf16_iter-devel -f %{oreon_filedir}/rust-utf16_iter-devel.list

%changelog

%autochangelog
