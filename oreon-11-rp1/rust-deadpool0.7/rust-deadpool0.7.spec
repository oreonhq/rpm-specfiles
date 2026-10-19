%global source0_hash 3d126179d86aee4556e54f5f3c6bf6d9884e7cc52cef82f77ee6f90a7747616d
%bcond check 1
%global debug_package %{nil}
%global crate deadpool
Name:           rust-deadpool0.7
Version:        0.7.0
Release:        1%{?dist}
Summary:        Dead simple async pool
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/deadpool
Source0:        https://static.crates.io/crates/deadpool/deadpool-%{version}.crate
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
Summary:        Dead simple async pool
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-trait-devel
Summary:        Dead simple async pool
BuildArch:      noarch
%description -n %{name}+async-trait-devel

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%package     -n %{name}+config-devel
Summary:        Dead simple async pool
BuildArch:      noarch
%description -n %{name}+config-devel

This package contains library source intended for building other packages which
use the "config" feature of the "%{crate}" crate.

%package     -n %{name}+config-crate-devel
Summary:        Dead simple async pool
BuildArch:      noarch
%description -n %{name}+config-crate-devel

This package contains library source intended for building other packages which
use the "config-crate" feature of the "%{crate}" crate.

%package     -n %{name}+managed-devel
Summary:        Dead simple async pool
BuildArch:      noarch
%description -n %{name}+managed-devel

This package contains library source intended for building other packages which
use the "managed" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Dead simple async pool
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+unmanaged-devel
Summary:        Dead simple async pool
BuildArch:      noarch
%description -n %{name}+unmanaged-devel

This package contains library source intended for building other packages which
use the "unmanaged" feature of the "%{crate}" crate.

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
%files -n rust-deadpool0.7-devel -f %{oreon_filedir}/rust-deadpool0.7-devel.list

%changelog

%autochangelog
