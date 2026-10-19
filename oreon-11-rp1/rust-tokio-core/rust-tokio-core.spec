%global source0_hash 87b1395334443abca552f63d4f61d0486f12377c2ba8b368e523f89e828cffd4
%bcond check 0
%global debug_package %{nil}
%global crate tokio-core
Name:           rust-tokio-core
Version:        0.1.18
Release:        1%{?dist}
Summary:        Core I/O and event loop primitives for asynchronous I/O in Rust. Foun...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tokio-core
Source0:        https://static.crates.io/crates/tokio-core/tokio-core-%{version}.crate
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
Summary:        Core I/O and event loop primitives for asynchronous I/O in Rust. Foun...
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
%files -n rust-tokio-core-devel -f %{oreon_filedir}/rust-tokio-core-devel.list

%changelog

%autochangelog
