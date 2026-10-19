%global source0_hash ba1310fcea54c6a9a4fd1aad794ecc02c31682f6bfbecdf460bf19533eed1e3e
%bcond check 1
%global debug_package %{nil}
%global crate tiff
Name:           rust-tiff0.9
Version:        0.9.1
Release:        1%{?dist}
Summary:        Decoding and encoding library in pure Rust
License:        MIT
URL:            https://crates.io/crates/tiff
Source0:        https://static.crates.io/crates/tiff/tiff-%{version}.crate
Patch:          tiff-fix-metadata.diff
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
Summary:        Decoding and encoding library in pure Rust
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

%cargo_test -- --doc
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tiff0.9-devel -f %{oreon_filedir}/rust-tiff0.9-devel.list

%changelog

%autochangelog
