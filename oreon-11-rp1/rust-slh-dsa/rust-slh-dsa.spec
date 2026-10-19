%global source0_hash bd2f20f4049197e03db1104a6452f4d9e96665d79f880198dce4a7026ba5f267
%bcond check 0
%global debug_package %{nil}
%global crate slh-dsa
Name:           rust-slh-dsa
Version:        0.0.3
Release:        1%{?dist}
Summary:        Pure Rust implementation of SLH-DSA (aka SPHINCS+) as described in the
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/slh-dsa
Source0:        https://static.crates.io/crates/slh-dsa/slh-dsa-%{version}.crate
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
Summary:        Pure Rust implementation of SLH-DSA (aka SPHINCS+) as described in the
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of SLH-DSA (aka SPHINCS+) as described in the
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

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
%files -n rust-slh-dsa-devel -f %{oreon_filedir}/rust-slh-dsa-devel.list

%changelog

%autochangelog
