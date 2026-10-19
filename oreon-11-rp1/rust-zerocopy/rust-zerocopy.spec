%global source0_hash 6df92bf3d9227be3d53173901ddbffac2babc27ae50f397776ffd6dc33f800cb
%bcond check 0
%global debug_package %{nil}
%global crate zerocopy
Name:           rust-zerocopy
Version:        0.8.59
Release:        1%{?dist}
Summary:        Zerocopy makes zero-cost memory manipulation effortless
License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/zerocopy
Source0:        https://static.crates.io/crates/zerocopy/zerocopy-%{version}.crate
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
Summary:        Zerocopy makes zero-cost memory manipulation effortless
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__internal_use_only_features_that_work_on_stable-devel
Summary:        Zerocopy makes zero-cost memory manipulation effortless
BuildArch:      noarch
%description -n %{name}+__internal_use_only_features_that_work_on_stable-devel

This package contains library source intended for building other packages which
use the "__internal_use_only_features_that_work_on_stable" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Zerocopy makes zero-cost memory manipulation effortless
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Zerocopy makes zero-cost memory manipulation effortless
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+float-nightly-devel
Summary:        Zerocopy makes zero-cost memory manipulation effortless
BuildArch:      noarch
%description -n %{name}+float-nightly-devel

This package contains library source intended for building other packages which
use the "float-nightly" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        Zerocopy makes zero-cost memory manipulation effortless
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+simd-nightly-devel
Summary:        Zerocopy makes zero-cost memory manipulation effortless
BuildArch:      noarch
%description -n %{name}+simd-nightly-devel

This package contains library source intended for building other packages which
use the "simd-nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Zerocopy makes zero-cost memory manipulation effortless
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
%files -n rust-zerocopy-devel -f %{oreon_filedir}/rust-zerocopy-devel.list

%changelog

%autochangelog
