%global source0_hash 8de9e551ced9d700a31dacb8b168129640240fcd7a279a3fa4d59608b84ebcae
%bcond check 1
%global debug_package %{nil}
%global crate exacl
Name:           rust-exacl
Version:        0.13.0
Release:        1%{?dist}
Summary:        Manipulate file system access control lists
License:        MIT
URL:            https://crates.io/crates/exacl
Source0:        https://static.crates.io/crates/exacl/exacl-%{version}.crate
Patch:          exacl-fix-metadata.diff
Patch2:         exacl-always-generate-bindings.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  libacl-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       libacl-devel
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Manipulate file system access control lists
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+buildtime_bindgen-devel
Summary:        Manipulate file system access control lists
BuildArch:      noarch
%description -n %{name}+buildtime_bindgen-devel

This package contains library source intended for building other packages which
use the "buildtime_bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Manipulate file system access control lists
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

%cargo_test -- -- --exact --skip test_too_many_entries
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-exacl-devel -f %{oreon_filedir}/rust-exacl-devel.list

%changelog

%autochangelog
