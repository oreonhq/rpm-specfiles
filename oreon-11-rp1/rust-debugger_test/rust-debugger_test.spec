%global source0_hash da325a995e01a935dcb146718bb8543400fc7a69790399c904d0005d701f355a
%bcond check 0
%global debug_package %{nil}
%global crate debugger_test
Name:           rust-debugger_test
Version:        0.2.0
Release:        1%{?dist}
Summary:        Provides a proc macro for writing tests that launch a debugger and
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/debugger_test
Source0:        https://static.crates.io/crates/debugger_test/debugger_test-%{version}.crate
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
Summary:        Provides a proc macro for writing tests that launch a debugger and
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
%files -n rust-debugger_test-devel -f %{oreon_filedir}/rust-debugger_test-devel.list

%changelog

%autochangelog
