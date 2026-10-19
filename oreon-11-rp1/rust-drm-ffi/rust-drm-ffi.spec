%global source0_hash 51a91c9b32ac4e8105dec255e849e0d66e27d7c34d184364fb93e469db08f690
%bcond check 1
%global debug_package %{nil}
%global crate drm-ffi
Name:           rust-drm-ffi
Version:        0.9.1
Release:        1%{?dist}
Summary:        Safe, low-level bindings to the Direct Rendering Manager API
License:        MIT
URL:            https://crates.io/crates/drm-ffi
Source0:        https://static.crates.io/crates/drm-ffi/drm-ffi-%{version}.crate
Patch:          drm-ffi-fix-metadata.diff
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
Summary:        Safe, low-level bindings to the Direct Rendering Manager API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+use_bindgen-devel
Summary:        Safe, low-level bindings to the Direct Rendering Manager API
BuildArch:      noarch
%description -n %{name}+use_bindgen-devel

This package contains library source intended for building other packages which
use the "use_bindgen" feature of the "%{crate}" crate.

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
%files -n rust-drm-ffi-devel -f %{oreon_filedir}/rust-drm-ffi-devel.list

%changelog

%autochangelog
