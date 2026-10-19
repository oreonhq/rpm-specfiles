%global source0_hash 75c54236f9045c8004a77942bebc52145b4844639db934a5c70fe08617fbe61a
%bcond check 0
%global crate handlebars
Name:           rust-handlebars
Version:        6.4.4
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

%package     -n %{crate}
Summary:        Handlebars templating implemented in Rust
License:        MIT AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
%description -n %{crate}

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

%package     -n %{name}+heck-devel
Summary:        Handlebars templating implemented in Rust
BuildArch:      noarch
%description -n %{name}+heck-devel

This package contains library source intended for building other packages which
use the "heck" feature of the "%{crate}" crate.

%package     -n %{name}+no_logging-devel
Summary:        Handlebars templating implemented in Rust
BuildArch:      noarch
%description -n %{name}+no_logging-devel

This package contains library source intended for building other packages which
use the "no_logging" feature of the "%{crate}" crate.

%package     -n %{name}+string_helpers-devel
Summary:        Handlebars templating implemented in Rust
BuildArch:      noarch
%description -n %{name}+string_helpers-devel

This package contains library source intended for building other packages which
use the "string_helpers" feature of the "%{crate}" crate.

%package     -n %{name}+walkdir-devel
Summary:        Handlebars templating implemented in Rust
BuildArch:      noarch
%description -n %{name}+walkdir-devel

This package contains library source intended for building other packages which
use the "walkdir" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm examples/dev_mode.rs
rm -rv wasm
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n handlebars -f %{oreon_filedir}/handlebars.list
%files -n rust-handlebars-devel -f %{oreon_filedir}/rust-handlebars-devel.list

%changelog

%autochangelog
