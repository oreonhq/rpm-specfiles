%global source0_hash 2e2b94854e8576378ccda7c8de8a66ed8b4e8acbd2c50ec3418ea6c8aaf4b567
%bcond check 1
%global debug_package %{nil}
%global crate derive-where
Name:           rust-derive-where
Version:        1.7.0
Release:        1%{?dist}
Summary:        Deriving with custom trait bounds
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/derive-where
Source0:        https://static.crates.io/crates/derive-where/derive-where-%{version}.crate
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
Summary:        Deriving with custom trait bounds
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Deriving with custom trait bounds
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+safe-devel
Summary:        Deriving with custom trait bounds
BuildArch:      noarch
%description -n %{name}+safe-devel

This package contains library source intended for building other packages which
use the "safe" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Deriving with custom trait bounds
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Deriving with custom trait bounds
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-on-drop-devel
Summary:        Deriving with custom trait bounds
BuildArch:      noarch
%description -n %{name}+zeroize-on-drop-devel

This package contains library source intended for building other packages which
use the "zeroize-on-drop" feature of the "%{crate}" crate.

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
%files -n rust-derive-where-devel -f %{oreon_filedir}/rust-derive-where-devel.list

%changelog

%autochangelog
