%global source0_hash eae7b9aee968036d54dce06cebaefd919e4472e753296daccd6d344e3e2df0c2
%bcond check 0
%global debug_package %{nil}
%global crate io-lifetimes
Name:           rust-io-lifetimes1
Version:        1.0.11
Release:        1%{?dist}
Summary:        A low-level I/O ownership and borrowing library
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/io-lifetimes
Source0:        https://static.crates.io/crates/io-lifetimes/io-lifetimes-%{version}.crate
Patch:          io-lifetimes-drop-nonlinux-deps.diff
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
Summary:        A low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+close-devel
Summary:        A low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+close-devel

This package contains library source intended for building other packages which
use the "close" feature of the "%{crate}" crate.

%package     -n %{name}+fs-err-devel
Summary:        A low-level I/O ownership and borrowing library
BuildArch:      noarch
%description -n %{name}+fs-err-devel

This package contains library source intended for building other packages which
use the "fs-err" feature of the "%{crate}" crate.

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
%files -n rust-io-lifetimes1-devel -f %{oreon_filedir}/rust-io-lifetimes1-devel.list

%changelog

%autochangelog
