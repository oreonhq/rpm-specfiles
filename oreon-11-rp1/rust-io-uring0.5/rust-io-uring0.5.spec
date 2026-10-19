%global source0_hash dd1e1a01cfb924fd8c5c43b6827965db394f5a3a16c599ce03452266e1cf984c
%bcond check 0
%global debug_package %{nil}
%global crate io-uring
Name:           rust-io-uring0.5
Version:        0.5.13
Release:        1%{?dist}
Summary:        Low-level io_uring userspace interface for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/io-uring
Source0:        https://static.crates.io/crates/io-uring/io-uring-%{version}.crate
Patch:          io-uring-fix-metadata.diff
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
Summary:        Low-level io_uring userspace interface for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+io_safety-devel
Summary:        Low-level io_uring userspace interface for Rust
BuildArch:      noarch
%description -n %{name}+io_safety-devel

This package contains library source intended for building other packages which
use the "io_safety" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Low-level io_uring userspace interface for Rust
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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

%ifnarch %{ix86}
%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-io-uring0.5-devel -f %{oreon_filedir}/rust-io-uring0.5-devel.list

%changelog

%autochangelog
