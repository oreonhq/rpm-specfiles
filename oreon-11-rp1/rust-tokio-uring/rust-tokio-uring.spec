%global source0_hash 0d5e02bb137e030b3a547c65a3bd2f1836d66a97369fdcc69034002b10e155ef
%bcond check 1
%global debug_package %{nil}
%global crate tokio-uring
Name:           rust-tokio-uring
Version:        0.4.0
Release:        1%{?dist}
Summary:        Io-uring support for the Tokio asynchronous runtime
License:        MIT
URL:            https://crates.io/crates/tokio-uring
Source0:        https://static.crates.io/crates/tokio-uring/tokio-uring-%{version}.crate
Patch:          tokio-uring-fix-metadata.diff
Patch10:        0001-UnixListener-do-not-set-unsupported-reuse_port-flag.patch
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
Summary:        Io-uring support for the Tokio asynchronous runtime
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Io-uring support for the Tokio asynchronous runtime
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

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

export RUST_TEST_THREADS=1
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tokio-uring-devel -f %{oreon_filedir}/rust-tokio-uring-devel.list

%changelog

%autochangelog
