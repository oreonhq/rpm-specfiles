%global source0_hash 84c8b9f757e028cee9fa244aea147aab2a9ec09d5325a9b01e0a49730c2b5269
%bcond check 1
%global debug_package %{nil}
%global crate toml_edit
%global crate_version 0.23.10+spec-1.0.0
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-toml_edit0.23
Version:        0.23.10
Release:        1%{?dist}
Summary:        Yet another format-preserving TOML parser
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/toml_edit
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          toml_edit-fix-metadata-auto.diff
Patch:          toml_edit-fix-metadata.diff
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
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+display-devel
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+display-devel

This package contains library source intended for building other packages which
use the "display" feature of the "%{crate}" crate.

%package     -n %{name}+parse-devel
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+parse-devel

This package contains library source intended for building other packages which
use the "parse" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+unbounded-devel
Summary:        Yet another format-preserving TOML parser
BuildArch:      noarch
%description -n %{name}+unbounded-devel

This package contains library source intended for building other packages which
use the "unbounded" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-toml_edit0.23-devel -f %{oreon_filedir}/rust-toml_edit0.23-devel.list

%changelog

%autochangelog
