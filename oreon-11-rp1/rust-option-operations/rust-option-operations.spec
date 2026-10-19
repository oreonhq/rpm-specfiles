%global source0_hash aca39cf52b03268400c16eeb9b56382ea3c3353409309b63f5c8f0b1faf42754
%bcond check 1
%global debug_package %{nil}
%global crate option-operations
Name:           rust-option-operations
Version:        0.6.1
Release:        1%{?dist}
Summary:        Improve arithmetic operations usability when dealing with Options
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/option-operations
Source0:        https://static.crates.io/crates/option-operations/option-operations-%{version}.crate
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
Summary:        Improve arithmetic operations usability when dealing with Options
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Improve arithmetic operations usability when dealing with Options
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
%files -n rust-option-operations-devel -f %{oreon_filedir}/rust-option-operations-devel.list

%changelog

%autochangelog
