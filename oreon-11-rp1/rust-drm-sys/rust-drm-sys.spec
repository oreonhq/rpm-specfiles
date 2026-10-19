%global source0_hash ecc8e1361066d91f5ffccff060a3c3be9c3ecde15be2959c1937595f7a82a9f8
%bcond check 1
%global debug_package %{nil}
%global crate drm-sys
Name:           rust-drm-sys
Version:        0.8.1
Release:        1%{?dist}
Summary:        Bindings to the Direct Rendering Manager API
License:        MIT
URL:            https://crates.io/crates/drm-sys
Source0:        https://static.crates.io/crates/drm-sys/drm-sys-%{version}.crate
Patch:          drm-sys-fix-metadata-auto.diff
Patch:          drm-sys-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libdrm)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Bindings to the Direct Rendering Manager API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        Bindings to the Direct Rendering Manager API
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+pkg-config-devel
Summary:        Bindings to the Direct Rendering Manager API
BuildArch:      noarch
%description -n %{name}+pkg-config-devel

This package contains library source intended for building other packages which
use the "pkg-config" feature of the "%{crate}" crate.

%package     -n %{name}+update_bindings-devel
Summary:        Bindings to the Direct Rendering Manager API
BuildArch:      noarch
Requires:       pkgconfig(libdrm)
%description -n %{name}+update_bindings-devel

This package contains library source intended for building other packages which
use the "update_bindings" feature of the "%{crate}" crate.

%package     -n %{name}+use_bindgen-devel
Summary:        Bindings to the Direct Rendering Manager API
BuildArch:      noarch
Requires:       pkgconfig(libdrm)
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
%files -n rust-drm-sys-devel -f %{oreon_filedir}/rust-drm-sys-devel.list

%changelog

%autochangelog
