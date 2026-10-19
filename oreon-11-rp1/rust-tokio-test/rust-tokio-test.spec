%global source0_hash 3f6d24790a10a7af737693a3e8f1d03faef7e6ca0cc99aae5066f533766de545
%bcond check 1
%global debug_package %{nil}
%global crate tokio-test
Name:           rust-tokio-test
Version:        0.4.5
Release:        1%{?dist}
Summary:        Testing utilities for Tokio- and futures-based code
License:        MIT
URL:            https://crates.io/crates/tokio-test
Source0:        https://static.crates.io/crates/tokio-test/tokio-test-%{version}.crate
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
Summary:        Testing utilities for Tokio- and futures-based code
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
%files -n rust-tokio-test-devel -f %{oreon_filedir}/rust-tokio-test-devel.list

%changelog

%autochangelog
