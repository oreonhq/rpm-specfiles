%global source0_hash 6b1e7f9a428571be2dc5bc0505c13fb6bf936822b894ec87abf8a08a4e51742d
%bcond check 1
%global debug_package %{nil}
%global crate rustc-hash
Name:           rust-rustc-hash
Version:        2.1.3
Release:        1%{?dist}
Summary:        Speedy, non-cryptographic hashing algorithm used by rustc
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/rustc-hash
Source0:        https://static.crates.io/crates/rustc-hash/rustc-hash-%{version}.crate
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
Summary:        Speedy, non-cryptographic hashing algorithm used by rustc
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Speedy, non-cryptographic hashing algorithm used by rustc
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Speedy, non-cryptographic hashing algorithm used by rustc
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
%files -n rust-rustc-hash-devel -f %{oreon_filedir}/rust-rustc-hash-devel.list

%changelog

%autochangelog
