%global source10_hash 8d774b8e55770e19ccdbebe68a10c7505efaa6988257e87bfc58bf0c6675817b
%global source0_hash c50341f21df64b412b4f917e34b7aa786c092d64f3f905f478cb76950c7e980c
%bcond check 1
%global debug_package %{nil}
%global crate cyclonedx-bom-macros
Name:           rust-cyclonedx-bom-macros
Version:        0.1.0
Release:        1%{?dist}
Summary:        Procedural macros used internally by the cyclonedx-bom crate
License:        Apache-2.0
URL:            https://crates.io/crates/cyclonedx-bom-macros
Source0:        https://static.crates.io/crates/cyclonedx-bom-macros/cyclonedx-bom-macros-%{version}.crate
Source10:       https://github.com/CycloneDX/cyclonedx-rust-cargo/raw/649dcba64d9e0e34e233450e0f1e7b96ea95d02d/LICENSE
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
Summary:        Procedural macros used internally by the cyclonedx-bom crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p '%{SOURCE10}' .
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

export TRYBUILD=overwrite
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-cyclonedx-bom-macros-devel -f %{oreon_filedir}/rust-cyclonedx-bom-macros-devel.list

%changelog

%autochangelog
