%global source0_hash c2db04e74f0a9a93103b50e90b96024c9b2bdca8bce6a632ec71b88736d3d359
%bcond check 1
%global debug_package %{nil}
%global crate doctest-file
Name:           rust-doctest-file
Version:        1.1.1
Release:        1%{?dist}
Summary:        Macro for sourcing doctests from dedicated files into Rustdoc
License:        0BSD
URL:            https://crates.io/crates/doctest-file
Source0:        https://static.crates.io/crates/doctest-file/doctest-file-%{version}.crate
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
Summary:        Macro for sourcing doctests from dedicated files into Rustdoc
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

%cargo_test -- --bins
%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-doctest-file-devel -f %{oreon_filedir}/rust-doctest-file-devel.list

%changelog

%autochangelog
