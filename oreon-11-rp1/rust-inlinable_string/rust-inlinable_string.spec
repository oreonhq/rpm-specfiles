%global source0_hash c8fae54786f62fb2918dcfae3d568594e50eb9b5c25bf04371af6fe7516452fb
%bcond check 0
%global debug_package %{nil}
%global crate inlinable_string
Name:           rust-inlinable_string
Version:        0.1.15
Release:        1%{?dist}
Summary:        The `inlinable_string` crate provides the `InlinableString` type -- a...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/inlinable_string
Source0:        https://static.crates.io/crates/inlinable_string/inlinable_string-%{version}.crate
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

%package     -n %{name}+nightly-devel
Summary:        The `inlinable_string` crate provides the `InlinableString` type -- a...
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        The `inlinable_string` crate provides the `InlinableString` type -- a...
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        The `inlinable_string` crate provides the `InlinableString` type -- a...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-inlinable_string-devel -f %{oreon_filedir}/rust-inlinable_string-devel.list

%changelog

%autochangelog
