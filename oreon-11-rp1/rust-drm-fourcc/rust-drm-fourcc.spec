%global source0_hash 0aafbcdb8afc29c1a7ee5fbe53b5d62f4565b35a042a662ca9fecd0b54dae6f4
%bcond check 1
%global debug_package %{nil}
%global crate drm-fourcc
Name:           rust-drm-fourcc
Version:        2.2.0
Release:        1%{?dist}
Summary:        Enum with every valid Direct Rendering Manager (DRM) format fourcc
License:        MIT
URL:            https://crates.io/crates/drm-fourcc
Source0:        https://static.crates.io/crates/drm-fourcc/drm-fourcc-%{version}.crate
Patch:          drm-fourcc-fix-metadata.diff
Patch2:         https://github.com/danielzfranklin/drm-fourcc-rs/pull/21.patch
Patch3:         0001-adapt-to-bindgen-API-changes.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  rustfmt
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Enum with every valid Direct Rendering Manager (DRM) format fourcc
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        Enum with every valid Direct Rendering Manager (DRM) format fourcc
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+build_bindings-devel
Summary:        Enum with every valid Direct Rendering Manager (DRM) format fourcc
BuildArch:      noarch
%description -n %{name}+build_bindings-devel

This package contains library source intended for building other packages which
use the "build_bindings" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Enum with every valid Direct Rendering Manager (DRM) format fourcc
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Enum with every valid Direct Rendering Manager (DRM) format fourcc
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Enum with every valid Direct Rendering Manager (DRM) format fourcc
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f build_bindings
%install
%cargo_install -f build_bindings
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f build_bindings
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-drm-fourcc-devel -f %{oreon_filedir}/rust-drm-fourcc-devel.list

%changelog

%autochangelog
