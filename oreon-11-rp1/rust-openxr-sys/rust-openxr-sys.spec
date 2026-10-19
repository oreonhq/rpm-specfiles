%global source0_hash f10e7e38c47f2175fc39363713b656db899fa0b4a14341029702cbdfa6f44d05
%bcond check 0
%global debug_package %{nil}
%global crate openxr-sys
Name:           rust-openxr-sys
Version:        0.11.0
Release:        1%{?dist}
Summary:        OpenXR FFI bindings
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/openxr-sys
Source0:        https://static.crates.io/crates/openxr-sys/openxr-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(openxr)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(openxr)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        OpenXR FFI bindings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cmake-devel
Summary:        OpenXR FFI bindings
BuildArch:      noarch
%description -n %{name}+cmake-devel

This package contains library source intended for building other packages which
use the "cmake" feature of the "%{crate}" crate.

%package     -n %{name}+linked-devel
Summary:        OpenXR FFI bindings
BuildArch:      noarch
%description -n %{name}+linked-devel

This package contains library source intended for building other packages which
use the "linked" feature of the "%{crate}" crate.

%package     -n %{name}+mint-devel
Summary:        OpenXR FFI bindings
BuildArch:      noarch
%description -n %{name}+mint-devel

This package contains library source intended for building other packages which
use the "mint" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        OpenXR FFI bindings
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -rf OpenXR-SDK
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
%files -n rust-openxr-sys-devel -f %{oreon_filedir}/rust-openxr-sys-devel.list

%changelog

%autochangelog
