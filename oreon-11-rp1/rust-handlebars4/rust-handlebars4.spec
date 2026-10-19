%global source0_hash faa67bab9ff362228eb3d00bd024a4965d8231bbb7921167f0cfa66c6626b225
%bcond check 1
%global debug_package %{nil}
%global crate handlebars
Name:           rust-handlebars4
Version:        4.5.0
Release:        1%{?dist}
Summary:        Handlebars templating implemented in Rust
License:        MIT
URL:            https://crates.io/crates/handlebars
Source0:        https://static.crates.io/crates/handlebars/handlebars-%{version}.crate
Patch:          handlebars-fix-metadata.diff
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
Summary:        Handlebars templating implemented in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dir_source-devel
Summary:        Handlebars templating implemented in Rust
BuildArch:      noarch
%description -n %{name}+dir_source-devel

This package contains library source intended for building other packages which
use the "dir_source" feature of the "%{crate}" crate.

%package     -n %{name}+no_logging-devel
Summary:        Handlebars templating implemented in Rust
BuildArch:      noarch
%description -n %{name}+no_logging-devel

This package contains library source intended for building other packages which
use the "no_logging" feature of the "%{crate}" crate.

%package     -n %{name}+script_helper-devel
Summary:        Handlebars templating implemented in Rust
BuildArch:      noarch
%description -n %{name}+script_helper-devel

This package contains library source intended for building other packages which
use the "script_helper" feature of the "%{crate}" crate.

%package     -n %{name}+string_helpers-devel
Summary:        Handlebars templating implemented in Rust
BuildArch:      noarch
%description -n %{name}+string_helpers-devel

This package contains library source intended for building other packages which
use the "string_helpers" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm examples/dev_mode.rs
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
%files -n rust-handlebars4-devel -f %{oreon_filedir}/rust-handlebars4-devel.list

%changelog

%autochangelog
