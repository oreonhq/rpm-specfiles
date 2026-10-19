%global source0_hash bc984f4f9ceb736a7bb755c3e3bd17dc56370af2600c9780dcc48c66453da34d
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate sanitize-filename
Name:           rust-sanitize-filename
Version:        0.6.0
Release:        1%{?dist}
Summary:        Simple filename sanitizer, based on Node's sanitize-filename
License:        MIT
URL:            https://crates.io/crates/sanitize-filename
Source0:        https://static.crates.io/crates/sanitize-filename/sanitize-filename-%{version}.crate
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
Summary:        Simple filename sanitizer, based on Node's sanitize-filename
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
%files -n rust-sanitize-filename-devel -f %{oreon_filedir}/rust-sanitize-filename-devel.list

%changelog

%autochangelog
