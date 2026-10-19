%global source0_hash 13362233b147e57674c37b802d216b7c5e3dcccbed8967c84f0d8d223868ae27
%bcond check 1
%global debug_package %{nil}
%global crate reflink-copy
Name:           rust-reflink-copy
Version:        0.1.29
Release:        1%{?dist}
Summary:        Copy-on-write mechanism on supported file systems
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/reflink-copy
Source0:        https://static.crates.io/crates/reflink-copy/reflink-copy-%{version}.crate
Patch:          reflink-copy-fix-metadata-auto.diff
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
Summary:        Copy-on-write mechanism on supported file systems
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Copy-on-write mechanism on supported file systems
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

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
%files -n rust-reflink-copy-devel -f %{oreon_filedir}/rust-reflink-copy-devel.list

%changelog

%autochangelog
