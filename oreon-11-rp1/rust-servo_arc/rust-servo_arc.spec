%global source0_hash 170fb83ab34de17dc69aa7c67482b22218ddb85da56546f9bd6b929e32a05930
%bcond check 1
%global debug_package %{nil}
%global crate servo_arc
Name:           rust-servo_arc
Version:        0.4.3
Release:        1%{?dist}
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/servo_arc
Source0:        https://static.crates.io/crates/servo_arc/servo_arc-%{version}.crate
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
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gecko_refcount_logging-devel
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references
BuildArch:      noarch
%description -n %{name}+gecko_refcount_logging-devel

This package contains library source intended for building other packages which
use the "gecko_refcount_logging" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+servo-devel
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references
BuildArch:      noarch
%description -n %{name}+servo-devel

This package contains library source intended for building other packages which
use the "servo" feature of the "%{crate}" crate.

%package     -n %{name}+track_alloc_size-devel
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references
BuildArch:      noarch
%description -n %{name}+track_alloc_size-devel

This package contains library source intended for building other packages which
use the "track_alloc_size" feature of the "%{crate}" crate.

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
%files -n rust-servo_arc-devel -f %{oreon_filedir}/rust-servo_arc-devel.list

%changelog

%autochangelog
