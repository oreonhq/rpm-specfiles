%global source0_hash 2ee0548edecd1b907be7e67789923b7d02275b9ba4a33ebc33300e2c947a8cb1
%bcond check 0
%global debug_package %{nil}
%global crate valuable-serde
Name:           rust-valuable-serde
Version:        0.1.1
Release:        1%{?dist}
Summary:        `serde::Serialize` implementation for `Valuable` types.
License:        MIT
URL:            https://crates.io/crates/valuable-serde
Source0:        https://static.crates.io/crates/valuable-serde/valuable-serde-%{version}.crate
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
Summary:        `serde::Serialize` implementation for `Valuable` types.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        `serde::Serialize` implementation for `Valuable` types.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        `serde::Serialize` implementation for `Valuable` types.
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
%files -n rust-valuable-serde-devel -f %{oreon_filedir}/rust-valuable-serde-devel.list

%changelog

%autochangelog
