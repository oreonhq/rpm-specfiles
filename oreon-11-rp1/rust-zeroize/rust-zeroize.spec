%global source0_hash e13c156562582aa81c60cb29407084cdb54c4164760106ab78e6c5b0858cf64e
%bcond check 1
%global debug_package %{nil}
%global crate zeroize
Name:           rust-zeroize
Version:        1.9.0
Release:        2%{?dist}
Summary:        Securely clear secrets from memory with a simple trait built on
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/zeroize
Source0:        https://static.crates.io/crates/zeroize/zeroize-%{version}.crate
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
Summary:        Securely clear secrets from memory with a simple trait built on
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aarch64-devel
Summary:        Securely clear secrets from memory with a simple trait built on
BuildArch:      noarch
%description -n %{name}+aarch64-devel

This package contains library source intended for building other packages which
use the "aarch64" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Securely clear secrets from memory with a simple trait built on
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Securely clear secrets from memory with a simple trait built on
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        Securely clear secrets from memory with a simple trait built on
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Securely clear secrets from memory with a simple trait built on
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
%files -n rust-zeroize-devel -f %{oreon_filedir}/rust-zeroize-devel.list

%changelog

%autochangelog
