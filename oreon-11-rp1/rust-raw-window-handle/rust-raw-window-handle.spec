%global source0_hash 20675572f6f24e9e76ef639bc5552774ed45f1c30e2951e1e99c59888861c539
%bcond check 0
%global debug_package %{nil}
%global crate raw-window-handle
Name:           rust-raw-window-handle
Version:        0.6.2
Release:        1%{?dist}
Summary:        Interoperability library for Rust Windowing applications
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/raw-window-handle
Source0:        https://static.crates.io/crates/raw-window-handle/raw-window-handle-%{version}.crate
Patch:          raw-window-handle-fix-metadata-auto.diff
Patch:          raw-window-handle-fix-metadata.diff
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
Summary:        Interoperability library for Rust Windowing applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Interoperability library for Rust Windowing applications
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Interoperability library for Rust Windowing applications
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
%files -n rust-raw-window-handle-devel -f %{oreon_filedir}/rust-raw-window-handle-devel.list

%changelog

%autochangelog
