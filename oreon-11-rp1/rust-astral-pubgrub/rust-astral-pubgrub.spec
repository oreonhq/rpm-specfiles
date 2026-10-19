%global source0_hash d6cb15b4f5096a3a1b41fdc2736a1c33d87c78f34d3c1ec2b669e766edadd559
%bcond check 1
%global debug_package %{nil}
%global crate astral-pubgrub
Name:           rust-astral-pubgrub
Version:        0.3.3
Release:        1%{?dist}
Summary:        PubGrub version solving algorithm
License:        MPL-2.0
URL:            https://crates.io/crates/astral-pubgrub
Source0:        https://static.crates.io/crates/astral-pubgrub/astral-pubgrub-%{version}.crate
Patch:          astral-pubgrub-fix-metadata.diff
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
Summary:        PubGrub version solving algorithm
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        PubGrub version solving algorithm
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-astral-pubgrub-devel -f %{oreon_filedir}/rust-astral-pubgrub-devel.list

%changelog

%autochangelog
