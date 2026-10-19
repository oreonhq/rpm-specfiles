%global source0_hash a5d440709e79d88e51ac01c4b72fc6cb7314017bb7da9eeff678aa94c10e3ea8
%bcond check 0
%global debug_package %{nil}
%global crate serde_bytes
Name:           rust-serde_bytes
Version:        0.11.19
Release:        1%{?dist}
Summary:        Optimized handling of &[u8] and Vec<u8> for Serde
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_bytes
Source0:        https://static.crates.io/crates/serde_bytes/serde_bytes-%{version}.crate
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
Summary:        Optimized handling of &[u8] and Vec<u8> for Serde
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Optimized handling of &[u8] and Vec<u8> for Serde
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Optimized handling of &[u8] and Vec<u8> for Serde
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
%files -n rust-serde_bytes-devel -f %{oreon_filedir}/rust-serde_bytes-devel.list

%changelog

%autochangelog
