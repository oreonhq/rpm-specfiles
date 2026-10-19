%global source0_hash 1ebdb1f8f8d2815bbe7b369a7da10343c82026a4503b68bd1279ba557611e96d
%bcond check 1
%global debug_package %{nil}
%global crate educe
Name:           rust-educe
Version:        0.8.1
Release:        1%{?dist}
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
License:        MIT
URL:            https://crates.io/crates/educe
Source0:        https://static.crates.io/crates/educe/educe-%{version}.crate
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
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+Clone-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+Clone-devel

This package contains library source intended for building other packages which
use the "Clone" feature of the "%{crate}" crate.

%package     -n %{name}+Copy-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+Copy-devel

This package contains library source intended for building other packages which
use the "Copy" feature of the "%{crate}" crate.

%package     -n %{name}+Debug-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+Debug-devel

This package contains library source intended for building other packages which
use the "Debug" feature of the "%{crate}" crate.

%package     -n %{name}+Default-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+Default-devel

This package contains library source intended for building other packages which
use the "Default" feature of the "%{crate}" crate.

%package     -n %{name}+Deref-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+Deref-devel

This package contains library source intended for building other packages which
use the "Deref" feature of the "%{crate}" crate.

%package     -n %{name}+DerefMut-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+DerefMut-devel

This package contains library source intended for building other packages which
use the "DerefMut" feature of the "%{crate}" crate.

%package     -n %{name}+Eq-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+Eq-devel

This package contains library source intended for building other packages which
use the "Eq" feature of the "%{crate}" crate.

%package     -n %{name}+Hash-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+Hash-devel

This package contains library source intended for building other packages which
use the "Hash" feature of the "%{crate}" crate.

%package     -n %{name}+Into-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+Into-devel

This package contains library source intended for building other packages which
use the "Into" feature of the "%{crate}" crate.

%package     -n %{name}+Ord-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+Ord-devel

This package contains library source intended for building other packages which
use the "Ord" feature of the "%{crate}" crate.

%package     -n %{name}+PartialEq-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+PartialEq-devel

This package contains library source intended for building other packages which
use the "PartialEq" feature of the "%{crate}" crate.

%package     -n %{name}+PartialOrd-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+PartialOrd-devel

This package contains library source intended for building other packages which
use the "PartialOrd" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Procedural macros to help you implement Rust-built-in traits quickly
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

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
%files -n rust-educe-devel -f %{oreon_filedir}/rust-educe-devel.list

%changelog

%autochangelog
