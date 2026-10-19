%global source0_hash aa9a19cbb55df58761df49b23516a86d432839add4af60fc256da840f66ed35b
%bcond check 0
%global debug_package %{nil}
%global crate foreign-types-shared
Name:           rust-foreign-types-shared
Version:        0.3.1
Release:        1%{?dist}
Summary:        An internal crate used by foreign-types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/foreign-types-shared
Source0:        https://static.crates.io/crates/foreign-types-shared/foreign-types-shared-%{version}.crate
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
Summary:        An internal crate used by foreign-types
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
%files -n rust-foreign-types-shared-devel -f %{oreon_filedir}/rust-foreign-types-shared-devel.list

%changelog

%autochangelog
