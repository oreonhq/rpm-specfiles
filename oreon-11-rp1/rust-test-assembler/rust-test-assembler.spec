%global source0_hash 9a6da51de149453f5c43fa67d5e73cccd75b3c5727a38a2f18c5f3c47f2db582
%bcond check 0
%global debug_package %{nil}
%global crate test-assembler
Name:           rust-test-assembler
Version:        0.1.6
Release:        1%{?dist}
Summary:        Set of types for building complex binary streams
License:        MIT
URL:            https://crates.io/crates/test-assembler
Source0:        https://static.crates.io/crates/test-assembler/test-assembler-%{version}.crate
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
Summary:        Set of types for building complex binary streams
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
%files -n rust-test-assembler-devel -f %{oreon_filedir}/rust-test-assembler-devel.list

%changelog

%autochangelog
