%global source0_hash 8e29b54b27b49901092b20ef1177d42a068beec0ce5f3344a664118d586d2443
%bcond check 1
%global debug_package %{nil}
%global crate librsvg-rebind
Name:           rust-librsvg-rebind
Version:        0.3.0
Release:        1%{?dist}
Summary:        Rust bindings for librsvg
License:        MIT
URL:            https://crates.io/crates/librsvg-rebind
Source0:        https://static.crates.io/crates/librsvg-rebind/librsvg-rebind-%{version}.crate
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
Summary:        Rust bindings for librsvg
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v2_58-devel
Summary:        Rust bindings for librsvg
BuildArch:      noarch
%description -n %{name}+v2_58-devel

This package contains library source intended for building other packages which
use the "v2_58" feature of the "%{crate}" crate.

%package     -n %{name}+v2_59-devel
Summary:        Rust bindings for librsvg
BuildArch:      noarch
%description -n %{name}+v2_59-devel

This package contains library source intended for building other packages which
use the "v2_59" feature of the "%{crate}" crate.

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

%cargo_test -- -- --skip src/lib.rs
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-librsvg-rebind-devel -f %{oreon_filedir}/rust-librsvg-rebind-devel.list

%changelog

%autochangelog
