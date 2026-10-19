%global source0_hash 9c845311f0ff7951c5506121a9ad75aec44d083c31583b2ea5a30bcb0b0abba0
%bcond check 0
%global debug_package %{nil}
%global crate rstest_macros
Name:           rust-rstest_macros0.26
Version:        0.26.1
Release:        1%{?dist}
Summary:        Rust fixture based test framework
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rstest_macros
Source0:        https://static.crates.io/crates/rstest_macros/rstest_macros-%{version}.crate
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
Summary:        Rust fixture based test framework
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-timeout-devel
Summary:        Rust fixture based test framework
BuildArch:      noarch
%description -n %{name}+async-timeout-devel

This package contains library source intended for building other packages which
use the "async-timeout" feature of the "%{crate}" crate.

%package     -n %{name}+crate-name-devel
Summary:        Rust fixture based test framework
BuildArch:      noarch
%description -n %{name}+crate-name-devel

This package contains library source intended for building other packages which
use the "crate-name" feature of the "%{crate}" crate.

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
%files -n rust-rstest_macros0.26-devel -f %{oreon_filedir}/rust-rstest_macros0.26-devel.list

%changelog

%autochangelog
