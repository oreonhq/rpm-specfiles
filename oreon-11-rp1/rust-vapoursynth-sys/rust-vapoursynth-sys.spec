%global source0_hash 2b35092be61a799005aabfd2e9e95d074125984013142d87a5d3edecc039b9b5
%bcond check 0
%global debug_package %{nil}
%global crate vapoursynth-sys
Name:           rust-vapoursynth-sys
Version:        0.4.1
Release:        1%{?dist}
Summary:        Rust bindings for vapoursynth and vsscript.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/vapoursynth-sys
Source0:        https://static.crates.io/crates/vapoursynth-sys/vapoursynth-sys-%{version}.crate
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

%package     -n %{name}+gte-vapoursynth-api-31-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+gte-vapoursynth-api-31-devel

This package contains library source intended for building other packages which
use the "gte-vapoursynth-api-31" feature of the "%{crate}" crate.

%package     -n %{name}+gte-vapoursynth-api-32-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+gte-vapoursynth-api-32-devel

This package contains library source intended for building other packages which
use the "gte-vapoursynth-api-32" feature of the "%{crate}" crate.

%package     -n %{name}+gte-vapoursynth-api-33-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+gte-vapoursynth-api-33-devel

This package contains library source intended for building other packages which
use the "gte-vapoursynth-api-33" feature of the "%{crate}" crate.

%package     -n %{name}+gte-vapoursynth-api-34-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+gte-vapoursynth-api-34-devel

This package contains library source intended for building other packages which
use the "gte-vapoursynth-api-34" feature of the "%{crate}" crate.

%package     -n %{name}+gte-vapoursynth-api-35-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+gte-vapoursynth-api-35-devel

This package contains library source intended for building other packages which
use the "gte-vapoursynth-api-35" feature of the "%{crate}" crate.

%package     -n %{name}+gte-vapoursynth-api-36-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+gte-vapoursynth-api-36-devel

This package contains library source intended for building other packages which
use the "gte-vapoursynth-api-36" feature of the "%{crate}" crate.

%package     -n %{name}+gte-vsscript-api-31-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+gte-vsscript-api-31-devel

This package contains library source intended for building other packages which
use the "gte-vsscript-api-31" feature of the "%{crate}" crate.

%package     -n %{name}+gte-vsscript-api-32-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+gte-vsscript-api-32-devel

This package contains library source intended for building other packages which
use the "gte-vsscript-api-32" feature of the "%{crate}" crate.

%package     -n %{name}+vapoursynth-api-31-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+vapoursynth-api-31-devel

This package contains library source intended for building other packages which
use the "vapoursynth-api-31" feature of the "%{crate}" crate.

%package     -n %{name}+vapoursynth-api-32-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+vapoursynth-api-32-devel

This package contains library source intended for building other packages which
use the "vapoursynth-api-32" feature of the "%{crate}" crate.

%package     -n %{name}+vapoursynth-api-33-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+vapoursynth-api-33-devel

This package contains library source intended for building other packages which
use the "vapoursynth-api-33" feature of the "%{crate}" crate.

%package     -n %{name}+vapoursynth-api-34-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+vapoursynth-api-34-devel

This package contains library source intended for building other packages which
use the "vapoursynth-api-34" feature of the "%{crate}" crate.

%package     -n %{name}+vapoursynth-api-35-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+vapoursynth-api-35-devel

This package contains library source intended for building other packages which
use the "vapoursynth-api-35" feature of the "%{crate}" crate.

%package     -n %{name}+vapoursynth-api-36-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+vapoursynth-api-36-devel

This package contains library source intended for building other packages which
use the "vapoursynth-api-36" feature of the "%{crate}" crate.

%package     -n %{name}+vapoursynth-functions-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+vapoursynth-functions-devel

This package contains library source intended for building other packages which
use the "vapoursynth-functions" feature of the "%{crate}" crate.

%package     -n %{name}+vsscript-api-31-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+vsscript-api-31-devel

This package contains library source intended for building other packages which
use the "vsscript-api-31" feature of the "%{crate}" crate.

%package     -n %{name}+vsscript-api-32-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+vsscript-api-32-devel

This package contains library source intended for building other packages which
use the "vsscript-api-32" feature of the "%{crate}" crate.

%package     -n %{name}+vsscript-functions-devel
Summary:        Rust bindings for vapoursynth and vsscript.
BuildArch:      noarch
%description -n %{name}+vsscript-functions-devel

This package contains library source intended for building other packages which
use the "vsscript-functions" feature of the "%{crate}" crate.

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
%files -n rust-vapoursynth-sys-devel -f %{oreon_filedir}/rust-vapoursynth-sys-devel.list

%changelog

%autochangelog
