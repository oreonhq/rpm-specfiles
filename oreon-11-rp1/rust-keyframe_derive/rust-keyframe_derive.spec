%global source1_hash e9f026792cccd5996dda8ceb2111e70543f256dfbdbc198b70aab68fd690f1cf
%global source0_hash 377d191d4db9904c659a7336fc943feb17bc737e18e8d7dbf4c3cfc86698f610
%bcond check 0
%global debug_package %{nil}
%global crate keyframe_derive
Name:           rust-keyframe_derive
Version:        1.0.0
Release:        1%{?dist}
Summary:        Implements #[derive(CanTween)] for keyframe
License:        MIT
URL:            https://crates.io/crates/keyframe_derive
Source0:        https://static.crates.io/crates/keyframe_derive/keyframe_derive-%{version}.crate
Source1:        https://raw.githubusercontent.com/hannesmann/keyframe/master/LICENSE
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
Summary:        Implements #[derive(CanTween)] for keyframe
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
install -Dpm644 %{SOURCE1} %{buildroot}%{crate_instdir}/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-keyframe_derive-devel -f %{oreon_filedir}/rust-keyframe_derive-devel.list

%changelog

%autochangelog
