%global source0_hash 7e72ed92b67c146290f88e9c89d60ca163ea417a446f61ffd7b72df3e7f1dfd5
%bcond check 1
%global debug_package %{nil}
%global crate fs4
Name:           rust-fs4
Version:        1.1.0
Release:        1%{?dist}
Summary:        No libc, pure Rust cross-platform file locks
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fs4
Source0:        https://static.crates.io/crates/fs4/fs4-%{version}.crate
Patch:          fs4-fix-metadata-auto.diff
Patch:          fs4-fix-metadata.diff
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
Summary:        No libc, pure Rust cross-platform file locks
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        No libc, pure Rust cross-platform file locks
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+fs-err2-devel
Summary:        No libc, pure Rust cross-platform file locks
BuildArch:      noarch
%description -n %{name}+fs-err2-devel

This package contains library source intended for building other packages which
use the "fs-err2" feature of the "%{crate}" crate.

%package     -n %{name}+fs-err2-tokio-devel
Summary:        No libc, pure Rust cross-platform file locks
BuildArch:      noarch
%description -n %{name}+fs-err2-tokio-devel

This package contains library source intended for building other packages which
use the "fs-err2-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+fs-err3-devel
Summary:        No libc, pure Rust cross-platform file locks
BuildArch:      noarch
%description -n %{name}+fs-err3-devel

This package contains library source intended for building other packages which
use the "fs-err3" feature of the "%{crate}" crate.

%package     -n %{name}+fs-err3-tokio-devel
Summary:        No libc, pure Rust cross-platform file locks
BuildArch:      noarch
%description -n %{name}+fs-err3-tokio-devel

This package contains library source intended for building other packages which
use the "fs-err3-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        No libc, pure Rust cross-platform file locks
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        No libc, pure Rust cross-platform file locks
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

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
%files -n rust-fs4-devel -f %{oreon_filedir}/rust-fs4-devel.list

%changelog

%autochangelog
