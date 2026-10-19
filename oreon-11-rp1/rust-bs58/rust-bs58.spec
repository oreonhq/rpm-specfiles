%global source0_hash bf88ba1141d185c399bee5288d850d63b8369520c1eafc32a0430b5b6c287bf4
%bcond check 0
%global debug_package %{nil}
%global crate bs58
Name:           rust-bs58
Version:        0.5.1
Release:        1%{?dist}
Summary:        Another Base58 codec implementation.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bs58
Source0:        https://static.crates.io/crates/bs58/bs58-%{version}.crate
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
Summary:        Another Base58 codec implementation.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Another Base58 codec implementation.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+cb58-devel
Summary:        Another Base58 codec implementation.
BuildArch:      noarch
%description -n %{name}+cb58-devel

This package contains library source intended for building other packages which
use the "cb58" feature of the "%{crate}" crate.

%package     -n %{name}+check-devel
Summary:        Another Base58 codec implementation.
BuildArch:      noarch
%description -n %{name}+check-devel

This package contains library source intended for building other packages which
use the "check" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Another Base58 codec implementation.
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        Another Base58 codec implementation.
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Another Base58 codec implementation.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tinyvec-devel
Summary:        Another Base58 codec implementation.
BuildArch:      noarch
%description -n %{name}+tinyvec-devel

This package contains library source intended for building other packages which
use the "tinyvec" feature of the "%{crate}" crate.

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
%files -n rust-bs58-devel -f %{oreon_filedir}/rust-bs58-devel.list

%changelog

%autochangelog
