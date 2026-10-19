%global source0_hash 021e079a1bab0ecce6cf4b4b74c0c37afa4a697136eb3b127875c84a8f04a8c3
%bcond check 1
%global debug_package %{nil}
%global crate bisection
Name:           rust-bisection
Version:        0.1.0
Release:        1%{?dist}
Summary:        Rust implementation of the Python bisect module
License:        MIT
URL:            https://crates.io/crates/bisection
Source0:        https://static.crates.io/crates/bisection/bisection-%{version}.crate
Patch:          bisection-fix-metadata.diff
Patch10:        https://github.com/SteadBytes/bisection/pull/4.patch
Patch11:        bisection-0.1.0-fix-use-bisect-examples.patch
Patch12:        https://github.com/SteadBytes/bisection/pull/5.patch
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
Summary:        Rust implementation of the Python bisect module
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
%files -n rust-bisection-devel -f %{oreon_filedir}/rust-bisection-devel.list

%changelog

%autochangelog
