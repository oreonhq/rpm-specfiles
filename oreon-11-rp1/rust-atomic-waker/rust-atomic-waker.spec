%global source0_hash 1505bd5d3d116872e7271a6d4e16d81d0c8570876c8de68093a09ac269d8aac0
%bcond check 0
%global debug_package %{nil}
%global crate atomic-waker
Name:           rust-atomic-waker
Version:        1.1.2
Release:        1%{?dist}
Summary:        A synchronization primitive for task wakeup
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/atomic-waker
Source0:        https://static.crates.io/crates/atomic-waker/atomic-waker-%{version}.crate
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

%package     -n %{name}+portable-atomic-devel
Summary:        A synchronization primitive for task wakeup
BuildArch:      noarch
%description -n %{name}+portable-atomic-devel

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

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
%files -n rust-atomic-waker-devel -f %{oreon_filedir}/rust-atomic-waker-devel.list

%changelog

%autochangelog
