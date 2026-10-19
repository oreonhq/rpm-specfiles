%global source0_hash 121c2a6cda46980bb0fcd1647ffaf6cd3fc79a013de288782836f6df9c48780e
%bcond check 0
%global debug_package %{nil}
%global crate tower-layer
Name:           rust-tower-layer
Version:        0.3.3
Release:        1%{?dist}
Summary:        Decorates a `Service` to allow easy composition between `Service`s.
License:        MIT
URL:            https://crates.io/crates/tower-layer
Source0:        https://static.crates.io/crates/tower-layer/tower-layer-%{version}.crate
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
Summary:        Decorates a `Service` to allow easy composition between `Service`s.
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tower-layer-devel -f %{oreon_filedir}/rust-tower-layer-devel.list

%changelog

%autochangelog
