%global source0_hash d4d0ceb932f7909033988f82e244109c50e5f3978ca031c576533dd3480a7605
%bcond check 0
%global debug_package %{nil}
%global crate futures-test
Name:           rust-futures-test
Version:        0.3.34
Release:        1%{?dist}
Summary:        Common utilities for testing components built off futures-rs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/futures-test
Source0:        https://static.crates.io/crates/futures-test/futures-test-%{version}.crate
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
Summary:        Common utilities for testing components built off futures-rs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Common utilities for testing components built off futures-rs
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
%files -n rust-futures-test-devel -f %{oreon_filedir}/rust-futures-test-devel.list

%changelog

%autochangelog
