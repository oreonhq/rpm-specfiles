%global source0_hash b40688ea6389c8171614b25491f71d4a27946e0c7ce2da1c6de27e25abf1a0ae
%bcond check 0
%global debug_package %{nil}
%global crate triomphe
Name:           rust-triomphe
Version:        0.1.16
Release:        1%{?dist}
Summary:        A fork of std::sync::Arc with some extra functionality and without we...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/triomphe
Source0:        https://static.crates.io/crates/triomphe/triomphe-%{version}.crate
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
Summary:        A fork of std::sync::Arc with some extra functionality and without we...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arc-swap-devel
Summary:        A fork of std::sync::Arc with some extra functionality and without we...
BuildArch:      noarch
%description -n %{name}+arc-swap-devel

This package contains library source intended for building other packages which
use the "arc-swap" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A fork of std::sync::Arc with some extra functionality and without we...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+stable_deref_trait-devel
Summary:        A fork of std::sync::Arc with some extra functionality and without we...
BuildArch:      noarch
%description -n %{name}+stable_deref_trait-devel

This package contains library source intended for building other packages which
use the "stable_deref_trait" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A fork of std::sync::Arc with some extra functionality and without we...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unsize-devel
Summary:        A fork of std::sync::Arc with some extra functionality and without we...
BuildArch:      noarch
%description -n %{name}+unsize-devel

This package contains library source intended for building other packages which
use the "unsize" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_dropck_eyepatch-devel
Summary:        A fork of std::sync::Arc with some extra functionality and without we...
BuildArch:      noarch
%description -n %{name}+unstable_dropck_eyepatch-devel

This package contains library source intended for building other packages which
use the "unstable_dropck_eyepatch" feature of the "%{crate}" crate.

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
%files -n rust-triomphe-devel -f %{oreon_filedir}/rust-triomphe-devel.list

%changelog

%autochangelog
