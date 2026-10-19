%global source0_hash c049c0be4daef0b145cb3555416b3b8ef5b7888a38aea1a3a155801fe7b0810b
%bcond check 0
%global debug_package %{nil}
%global crate arc-swap
Name:           rust-arc-swap
Version:        1.9.2
Release:        1%{?dist}
Summary:        Atomically swappable Arc
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/arc-swap
Source0:        https://static.crates.io/crates/arc-swap/arc-swap-%{version}.crate
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

%package     -n %{name}+experimental-strategies-devel
Summary:        Atomically swappable Arc
BuildArch:      noarch
%description -n %{name}+experimental-strategies-devel

This package contains library source intended for building other packages which
use the "experimental-strategies" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-thread-local-devel
Summary:        Atomically swappable Arc
BuildArch:      noarch
%description -n %{name}+experimental-thread-local-devel

This package contains library source intended for building other packages which
use the "experimental-thread-local" feature of the "%{crate}" crate.

%package     -n %{name}+internal-test-strategies-devel
Summary:        Atomically swappable Arc
BuildArch:      noarch
%description -n %{name}+internal-test-strategies-devel

This package contains library source intended for building other packages which
use the "internal-test-strategies" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Atomically swappable Arc
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+weak-devel
Summary:        Atomically swappable Arc
BuildArch:      noarch
%description -n %{name}+weak-devel

This package contains library source intended for building other packages which
use the "weak" feature of the "%{crate}" crate.

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
%files -n rust-arc-swap-devel -f %{oreon_filedir}/rust-arc-swap-devel.list

%changelog

%autochangelog
