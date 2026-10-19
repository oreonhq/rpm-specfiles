%global source0_hash 224399e74b87b5f3557511d98dff8b14089b3dadafcab6bb93eab67d3aace965
%bcond check 1
%global debug_package %{nil}
%global crate lock_api
Name:           rust-lock_api
Version:        0.4.14
Release:        1%{?dist}
Summary:        Wrappers to create fully-featured Mutex and RwLock types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lock_api
Source0:        https://static.crates.io/crates/lock_api/lock_api-%{version}.crate
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
Summary:        Wrappers to create fully-featured Mutex and RwLock types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arc_lock-devel
Summary:        Wrappers to create fully-featured Mutex and RwLock types
BuildArch:      noarch
%description -n %{name}+arc_lock-devel

This package contains library source intended for building other packages which
use the "arc_lock" feature of the "%{crate}" crate.

%package     -n %{name}+atomic_usize-devel
Summary:        Wrappers to create fully-featured Mutex and RwLock types
BuildArch:      noarch
%description -n %{name}+atomic_usize-devel

This package contains library source intended for building other packages which
use the "atomic_usize" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Wrappers to create fully-featured Mutex and RwLock types
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+owning_ref-devel
Summary:        Wrappers to create fully-featured Mutex and RwLock types
BuildArch:      noarch
%description -n %{name}+owning_ref-devel

This package contains library source intended for building other packages which
use the "owning_ref" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Wrappers to create fully-featured Mutex and RwLock types
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
%files -n rust-lock_api-devel -f %{oreon_filedir}/rust-lock_api-devel.list

%changelog

%autochangelog
