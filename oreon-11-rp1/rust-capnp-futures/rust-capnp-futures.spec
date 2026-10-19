%global source0_hash 73b69dfddccc57844f9a90f9d72b44b97c326914851ea94fb7da40ef9cad6e8d
%bcond check 0
%global debug_package %{nil}
%global crate capnp-futures
Name:           rust-capnp-futures
Version:        0.25.2
Release:        1%{?dist}
Summary:        async serialization for Cap'n Proto messages
License:        MIT
URL:            https://crates.io/crates/capnp-futures
Source0:        https://static.crates.io/crates/capnp-futures/capnp-futures-%{version}.crate
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
Summary:        async serialization for Cap'n Proto messages
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
%files -n rust-capnp-futures-devel -f %{oreon_filedir}/rust-capnp-futures-devel.list

%changelog

%autochangelog
