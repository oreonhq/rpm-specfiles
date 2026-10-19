%global source0_hash 2af50177e190e07a26ab74f8b1efbfe2ef87da2116221318cb1c2e82baf7de06
%bcond check 1
%global debug_package %{nil}
%global crate base64ct
Name:           rust-base64ct
Version:        1.8.3
Release:        1%{?dist}
Summary:        Pure Rust implementation of Base64 (RFC 4648) which avoids any usages of
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/base64ct
Source0:        https://static.crates.io/crates/base64ct/base64ct-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of Base64 (RFC 4648) which avoids any usages of
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of Base64 (RFC 4648) which avoids any usages of
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-base64ct-devel -f %{oreon_filedir}/rust-base64ct-devel.list

%changelog

%autochangelog
