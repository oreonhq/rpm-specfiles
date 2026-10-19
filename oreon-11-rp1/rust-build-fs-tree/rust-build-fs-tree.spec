%global source0_hash 4c68339add1d0c864575cd425203adee58c8b64ea1709b35bb90fc0fc07e4286
%bcond check 0
%global debug_package %{nil}
%global crate build-fs-tree
Name:           rust-build-fs-tree
Version:        0.6.0
Release:        1%{?dist}
Summary:        Generate a filesystem tree from a macro or a YAML tree
License:        MIT
URL:            https://crates.io/crates/build-fs-tree
Source0:        https://static.crates.io/crates/build-fs-tree/build-fs-tree-%{version}.crate
Patch:          build-fs-tree-fix-metadata.diff
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
Summary:        Generate a filesystem tree from a macro or a YAML tree
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Generate a filesystem tree from a macro or a YAML tree
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

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
%files -n rust-build-fs-tree-devel -f %{oreon_filedir}/rust-build-fs-tree-devel.list

%changelog

%autochangelog
