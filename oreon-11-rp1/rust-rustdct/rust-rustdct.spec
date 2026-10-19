%global source0_hash 8b61555105d6a9bf98797c063c362a1d24ed8ab0431655e38f1cf51e52089551
%bcond check 0
%global debug_package %{nil}
%global crate rustdct
Name:           rust-rustdct
Version:        0.7.1
Release:        1%{?dist}
Summary:        Compute Discrete Cosine Transforms (DCT) in O(nlogn) time
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustdct
Source0:        https://static.crates.io/crates/rustdct/rustdct-%{version}.crate
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
Summary:        Compute Discrete Cosine Transforms (DCT) in O(nlogn) time
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-rustdct-devel -f %{oreon_filedir}/rust-rustdct-devel.list

%changelog

%autochangelog
