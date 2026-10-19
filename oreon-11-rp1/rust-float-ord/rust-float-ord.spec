%global source0_hash 8ce81f49ae8a0482e4c55ea62ebbd7e5a686af544c00b9d090bba3ff9be97b3d
%bcond check 0
%global debug_package %{nil}
%global crate float-ord
Name:           rust-float-ord
Version:        0.3.2
Release:        1%{?dist}
Summary:        Total ordering for floating-point numbers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/float-ord
Source0:        https://static.crates.io/crates/float-ord/float-ord-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Total ordering for floating-point numbers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
dos2unix README.md
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
%files -n rust-float-ord-devel -f %{oreon_filedir}/rust-float-ord-devel.list

%changelog

%autochangelog
