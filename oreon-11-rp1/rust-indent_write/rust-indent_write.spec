%global source0_hash 0cfe9645a18782869361d9c8732246be7b410ad4e919d3609ebabdac00ba12c3
%bcond check 0
%global debug_package %{nil}
%global crate indent_write
Name:           rust-indent_write
Version:        2.2.0
Release:        1%{?dist}
Summary:        Simple Write adapters to add line indentation
License:        MPL-2.0
URL:            https://crates.io/crates/indent_write
Source0:        https://static.crates.io/crates/indent_write/indent_write-%{version}.crate
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
Summary:        Simple Write adapters to add line indentation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Simple Write adapters to add line indentation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-indent_write-devel -f %{oreon_filedir}/rust-indent_write-devel.list

%changelog

%autochangelog
