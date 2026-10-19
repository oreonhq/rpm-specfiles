%global source0_hash f973c28c0a4871a7926fc90c8377d4458fd6cbb19692f56582b4d2022313ae90
%bcond check 0
%global debug_package %{nil}
%global crate gix-config
Name:           rust-gix-config
Version:        0.60.0
Release:        1%{?dist}
Summary:        A git-config file parser and editor from the gitoxide project
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-config
Source0:        https://static.crates.io/crates/gix-config/gix-config-%{version}.crate
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

%package     -n %{name}+document-features-devel
Summary:        A git-config file parser and editor from the gitoxide project
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A git-config file parser and editor from the gitoxide project
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
%files -n rust-gix-config-devel -f %{oreon_filedir}/rust-gix-config-devel.list

%changelog

%autochangelog
