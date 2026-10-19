%global source0_hash 41e67cd8309bbd06cd603a9e693a784ac2e5d1e955f11286e355089fcab3047c
%bcond check 0
%global debug_package %{nil}
%global crate atomic_refcell
Name:           rust-atomic_refcell
Version:        0.1.13
Release:        1%{?dist}
Summary:        Threadsafe RefCell
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/atomic_refcell
Source0:        https://static.crates.io/crates/atomic_refcell/atomic_refcell-%{version}.crate
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
Summary:        Threadsafe RefCell
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Threadsafe RefCell
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-atomic_refcell-devel -f %{oreon_filedir}/rust-atomic_refcell-devel.list

%changelog

%autochangelog
