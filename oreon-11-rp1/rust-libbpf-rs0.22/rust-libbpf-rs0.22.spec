%global source0_hash 98e789d5b4dab748a2b8415974bf5b0fc2e9e782d0b118166222195acb4ac3b6
%bcond check 0
%global debug_package %{nil}
%global crate libbpf-rs
Name:           rust-libbpf-rs0.22
Version:        0.22.1
Release:        1%{?dist}
Summary:        Safe, idiomatic, and opinionated wrapper around libbpf-sys
License:        LGPL-2.1-only OR BSD-2-Clause
URL:            https://crates.io/crates/libbpf-rs
Source0:        https://static.crates.io/crates/libbpf-rs/libbpf-rs-%{version}.crate
Patch:          libbpf-rs-fix-metadata.diff
Patch:          libbpf-rs-rm-unneeded-IntoError-trait-methods.diff
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
Summary:        Safe, idiomatic, and opinionated wrapper around libbpf-sys
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+novendor-devel
Summary:        Safe, idiomatic, and opinionated wrapper around libbpf-sys
BuildArch:      noarch
%description -n %{name}+novendor-devel

This package contains library source intended for building other packages which
use the "novendor" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Safe, idiomatic, and opinionated wrapper around libbpf-sys
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

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

rm tests/test.rs
rm tests/test_tc.rs
rm tests/test_xdp.rs
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-libbpf-rs0.22-devel -f %{oreon_filedir}/rust-libbpf-rs0.22-devel.list

%changelog

%autochangelog
