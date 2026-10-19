%global source0_hash c4da24a77a3d8a6d4862d95f72e6fdb9c09a643ecdb402d754004a557f2bec75
%bcond check 1
%global debug_package %{nil}
%global crate lock_api
Name:           rust-lock_api0.3
Version:        0.3.4
Release:        1%{?dist}
Summary:        Wrappers to create fully-featured Mutex and RwLock types
License:        Apache-2.0 OR MIT
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
%files -n rust-lock_api0.3-devel -f %{oreon_filedir}/rust-lock_api0.3-devel.list

%changelog

%autochangelog
