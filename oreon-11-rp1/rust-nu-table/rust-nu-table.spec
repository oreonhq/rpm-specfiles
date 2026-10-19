%global source0_hash 9d56f95eb8573d12ce1ff11686bb3df13e0fa6c4d9dd782f093038995b5db84d
%bcond check 1
%global debug_package %{nil}
%global crate nu-table
Name:           rust-nu-table
Version:        0.99.1
Release:        1%{?dist}
Summary:        Nushell table printing
License:        MIT
URL:            https://crates.io/crates/nu-table
Source0:        https://static.crates.io/crates/nu-table/nu-table-%{version}.crate
Patch:          nu-table-fix-metadata.diff
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
Summary:        Nushell table printing
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
%files -n rust-nu-table-devel -f %{oreon_filedir}/rust-nu-table-devel.list

%changelog

%autochangelog
