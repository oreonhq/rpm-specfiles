%global source0_hash 9080b15e63775b9a2ac7dca720f7050a8b955e092ea0f6020a4a80f69998cdc0
%bcond check 0
%global debug_package %{nil}
%global crate io-uring
Name:           rust-io-uring
Version:        0.7.13
Release:        1%{?dist}
Summary:        The low-level `io_uring` userspace interface for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/io-uring
Source0:        https://static.crates.io/crates/io-uring/io-uring-%{version}.crate
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

%package     -n %{name}+direct-syscall-devel
Summary:        The low-level `io_uring` userspace interface for Rust
BuildArch:      noarch
%description -n %{name}+direct-syscall-devel

This package contains library source intended for building other packages which
use the "direct-syscall" feature of the "%{crate}" crate.

%package     -n %{name}+io_safety-devel
Summary:        The low-level `io_uring` userspace interface for Rust
BuildArch:      noarch
%description -n %{name}+io_safety-devel

This package contains library source intended for building other packages which
use the "io_safety" feature of the "%{crate}" crate.

%package     -n %{name}+overwrite-devel
Summary:        The low-level `io_uring` userspace interface for Rust
BuildArch:      noarch
%description -n %{name}+overwrite-devel

This package contains library source intended for building other packages which
use the "overwrite" feature of the "%{crate}" crate.

%package     -n %{name}+sc-devel
Summary:        The low-level `io_uring` userspace interface for Rust
BuildArch:      noarch
%description -n %{name}+sc-devel

This package contains library source intended for building other packages which
use the "sc" feature of the "%{crate}" crate.

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
%files -n rust-io-uring-devel -f %{oreon_filedir}/rust-io-uring-devel.list

%changelog

%autochangelog
