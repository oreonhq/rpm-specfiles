%global source0_hash 07c34a9410465b45bd9787443bc7370f37735bad04b0f0cd57ff1a3186c98988
%bcond check 1
%global debug_package %{nil}
%global crate globset
Name:           rust-globset
Version:        0.4.20
Release:        1%{?dist}
Summary:        Cross platform single glob and glob set matching
License:        Unlicense OR MIT
URL:            https://crates.io/crates/globset
Source0:        https://static.crates.io/crates/globset/globset-%{version}.crate
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
Summary:        Cross platform single glob and glob set matching
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Cross platform single glob and glob set matching
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Cross platform single glob and glob set matching
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Cross platform single glob and glob set matching
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde1-devel
Summary:        Cross platform single glob and glob set matching
BuildArch:      noarch
%description -n %{name}+serde1-devel

This package contains library source intended for building other packages which
use the "serde1" feature of the "%{crate}" crate.

%package     -n %{name}+simd-accel-devel
Summary:        Cross platform single glob and glob set matching
BuildArch:      noarch
%description -n %{name}+simd-accel-devel

This package contains library source intended for building other packages which
use the "simd-accel" feature of the "%{crate}" crate.

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
%files -n rust-globset-devel -f %{oreon_filedir}/rust-globset-devel.list

%changelog

%autochangelog
