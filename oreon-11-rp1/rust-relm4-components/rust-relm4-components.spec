%global source101_hash 23f18e03dc49df91622fe2a76176497404e46ced8a715d9d2b67a7446571cca3
%global source100_hash 62c7a1e35f56406896d7aa7ca52d0cc0d272ac022b5d2796e7d6905db8a3636a
%global source0_hash 62088215be530760481537aa8add43fdbe4b3794bf6cb4673a39083eb993307b
%bcond check 0
%global debug_package %{nil}
%global crate relm4-components
Name:           rust-relm4-components
Version:        0.11.0
Release:        1%{?dist}
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/relm4-components
Source0:        https://static.crates.io/crates/relm4-components/relm4-components-%{version}.crate
Source100:      https://raw.githubusercontent.com/Relm4/Relm4/main/LICENSE-APACHE
Source101:      https://raw.githubusercontent.com/Relm4/Relm4/main/LICENSE-MIT
Patch:          relm4-components-fix-metadata.diff
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
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+libadwaita-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+libadwaita-devel

This package contains library source intended for building other packages which
use the "libadwaita" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+reqwest-devel

This package contains library source intended for building other packages which
use the "reqwest" feature of the "%{crate}" crate.

%package     -n %{name}+web-devel
Summary:        Idiomatic GUI library inspired by Elm and based on gtk4-rs
BuildArch:      noarch
%description -n %{name}+web-devel

This package contains library source intended for building other packages which
use the "web" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE100} %{SOURCE101} .
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
%files -n rust-relm4-components-devel -f %{oreon_filedir}/rust-relm4-components-devel.list

%changelog

%autochangelog
