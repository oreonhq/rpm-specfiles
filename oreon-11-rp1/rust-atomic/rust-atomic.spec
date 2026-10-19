%global source0_hash a89cbf775b137e9b968e67227ef7f775587cde3fd31b0d8599dbd0f598a48340
%bcond check 0
%global debug_package %{nil}
%global crate atomic
Name:           rust-atomic
Version:        0.6.1
Release:        1%{?dist}
Summary:        Generic Atomic<T> wrapper type
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/atomic
Source0:        https://static.crates.io/crates/atomic/atomic-%{version}.crate
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
Summary:        Generic Atomic<T> wrapper type
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+fallback-devel
Summary:        Generic Atomic<T> wrapper type
BuildArch:      noarch
%description -n %{name}+fallback-devel

This package contains library source intended for building other packages which
use the "fallback" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Generic Atomic<T> wrapper type
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Generic Atomic<T> wrapper type
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Generic Atomic<T> wrapper type
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
%files -n rust-atomic-devel -f %{oreon_filedir}/rust-atomic-devel.list

%changelog

%autochangelog
