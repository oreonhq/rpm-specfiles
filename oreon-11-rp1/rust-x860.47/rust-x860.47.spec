%global source0_hash 55b5be8cc34d017d8aabec95bc45a43d0f20e8b2a31a453cabc804fe996f8dca
%bcond check 0
%global debug_package %{nil}
%global crate x86
Name:           rust-x860.47
Version:        0.47.0
Release:        1%{?dist}
Summary:        Library to program x86 (amd64) hardware. Contains x86 specific data s...
License:        MIT
URL:            https://crates.io/crates/x86
Source0:        https://static.crates.io/crates/x86/x86-%{version}.crate
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

%package     -n %{name}+performance-counter-devel
Summary:        Library to program x86 (amd64) hardware. Contains x86 specific data s...
BuildArch:      noarch
%description -n %{name}+performance-counter-devel

This package contains library source intended for building other packages which
use the "performance-counter" feature of the "%{crate}" crate.

%package     -n %{name}+phf-devel
Summary:        Library to program x86 (amd64) hardware. Contains x86 specific data s...
BuildArch:      noarch
%description -n %{name}+phf-devel

This package contains library source intended for building other packages which
use the "phf" feature of the "%{crate}" crate.

%package     -n %{name}+utest-devel
Summary:        Library to program x86 (amd64) hardware. Contains x86 specific data s...
BuildArch:      noarch
%description -n %{name}+utest-devel

This package contains library source intended for building other packages which
use the "utest" feature of the "%{crate}" crate.

%package     -n %{name}+vmtest-devel
Summary:        Library to program x86 (amd64) hardware. Contains x86 specific data s...
BuildArch:      noarch
%description -n %{name}+vmtest-devel

This package contains library source intended for building other packages which
use the "vmtest" feature of the "%{crate}" crate.

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
%files -n rust-x860.47-devel -f %{oreon_filedir}/rust-x860.47-devel.list

%changelog

%autochangelog
