%global source0_hash c11bed799433f0ba500d4c86251f2d88770ebd016e2a8a0c2e1c9fe87801639a
%bcond check 1
%global debug_package %{nil}
%global crate struct-patch
Name:           rust-struct-patch
Version:        0.9.5
Release:        1%{?dist}
Summary:        Library that helps you implement partial updates for your structs
License:        MIT
URL:            https://crates.io/crates/struct-patch
Source0:        https://static.crates.io/crates/struct-patch/struct-patch-%{version}.crate
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
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+box-devel
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+box-devel

This package contains library source intended for building other packages which
use the "box" feature of the "%{crate}" crate.

%package     -n %{name}+keep_none-devel
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+keep_none-devel

This package contains library source intended for building other packages which
use the "keep_none" feature of the "%{crate}" crate.

%package     -n %{name}+merge-devel
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+merge-devel

This package contains library source intended for building other packages which
use the "merge" feature of the "%{crate}" crate.

%package     -n %{name}+none_as_default-devel
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+none_as_default-devel

This package contains library source intended for building other packages which
use the "none_as_default" feature of the "%{crate}" crate.

%package     -n %{name}+op-devel
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+op-devel

This package contains library source intended for building other packages which
use the "op" feature of the "%{crate}" crate.

%package     -n %{name}+option-devel
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+option-devel

This package contains library source intended for building other packages which
use the "option" feature of the "%{crate}" crate.

%package     -n %{name}+status-devel
Summary:        Library that helps you implement partial updates for your structs
BuildArch:      noarch
%description -n %{name}+status-devel

This package contains library source intended for building other packages which
use the "status" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library that helps you implement partial updates for your structs
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
%files -n rust-struct-patch-devel -f %{oreon_filedir}/rust-struct-patch-devel.list

%changelog

%autochangelog
