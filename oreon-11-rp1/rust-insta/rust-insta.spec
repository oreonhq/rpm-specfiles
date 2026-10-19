%global source0_hash 86f0f8fee8c926415c58d6ae43a08523a26faccb2323f5e6b644fe7dd4ef6b82
%bcond check 0
%global debug_package %{nil}
%global crate insta
Name:           rust-insta
Version:        1.48.0
Release:        1%{?dist}
Summary:        A snapshot testing library for Rust
License:        Apache-2.0
URL:            https://crates.io/crates/insta
Source0:        https://static.crates.io/crates/insta/insta-%{version}.crate
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
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+console-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+console-devel

This package contains library source intended for building other packages which
use the "console" feature of the "%{crate}" crate.

%package     -n %{name}+_cargo_insta_internal-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+_cargo_insta_internal-devel

This package contains library source intended for building other packages which
use the "_cargo_insta_internal" feature of the "%{crate}" crate.

%package     -n %{name}+colors-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+colors-devel

This package contains library source intended for building other packages which
use the "colors" feature of the "%{crate}" crate.

%package     -n %{name}+csv-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+csv-devel

This package contains library source intended for building other packages which
use the "csv" feature of the "%{crate}" crate.

%package     -n %{name}+filters-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+filters-devel

This package contains library source intended for building other packages which
use the "filters" feature of the "%{crate}" crate.

%package     -n %{name}+glob-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+glob-devel

This package contains library source intended for building other packages which
use the "glob" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+redactions-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+redactions-devel

This package contains library source intended for building other packages which
use the "redactions" feature of the "%{crate}" crate.

%package     -n %{name}+ron-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+ron-devel

This package contains library source intended for building other packages which
use the "ron" feature of the "%{crate}" crate.

%package     -n %{name}+toml-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+toml-devel

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-devel
Summary:        A snapshot testing library for Rust
BuildArch:      noarch
%description -n %{name}+yaml-devel

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

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
%files -n rust-insta-devel -f %{oreon_filedir}/rust-insta-devel.list

%changelog

%autochangelog
