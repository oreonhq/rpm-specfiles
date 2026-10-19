%global source0_hash 2b40e20979244f65741f32baab82c0f12953b13ce78b15d644764556be123f09
%bcond check 1
%global debug_package %{nil}
%global crate elasticlunr-rs
Name:           rust-elasticlunr-rs
Version:        3.1.0
Release:        1%{?dist}
Summary:        Generate static document search indexes
License:        (MIT OR Apache-2.0) AND MIT
URL:            https://crates.io/crates/elasticlunr-rs
Source0:        https://static.crates.io/crates/elasticlunr-rs/elasticlunr-rs-%{version}.crate
Patch:          elasticlunr-rs-fix-metadata.diff
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
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ar-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+ar-devel

This package contains library source intended for building other packages which
use the "ar" feature of the "%{crate}" crate.

%package     -n %{name}+da-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+da-devel

This package contains library source intended for building other packages which
use the "da" feature of the "%{crate}" crate.

%package     -n %{name}+de-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+de-devel

This package contains library source intended for building other packages which
use the "de" feature of the "%{crate}" crate.

%package     -n %{name}+du-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+du-devel

This package contains library source intended for building other packages which
use the "du" feature of the "%{crate}" crate.

%package     -n %{name}+es-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+es-devel

This package contains library source intended for building other packages which
use the "es" feature of the "%{crate}" crate.

%package     -n %{name}+fi-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+fi-devel

This package contains library source intended for building other packages which
use the "fi" feature of the "%{crate}" crate.

%package     -n %{name}+fr-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+fr-devel

This package contains library source intended for building other packages which
use the "fr" feature of the "%{crate}" crate.

%package     -n %{name}+hu-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+hu-devel

This package contains library source intended for building other packages which
use the "hu" feature of the "%{crate}" crate.

%package     -n %{name}+it-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+it-devel

This package contains library source intended for building other packages which
use the "it" feature of the "%{crate}" crate.

%package     -n %{name}+ko-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+ko-devel

This package contains library source intended for building other packages which
use the "ko" feature of the "%{crate}" crate.

%package     -n %{name}+languages-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+languages-devel

This package contains library source intended for building other packages which
use the "languages" feature of the "%{crate}" crate.

%package     -n %{name}+no-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+no-devel

This package contains library source intended for building other packages which
use the "no" feature of the "%{crate}" crate.

%package     -n %{name}+pt-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+pt-devel

This package contains library source intended for building other packages which
use the "pt" feature of the "%{crate}" crate.

%package     -n %{name}+ro-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+ro-devel

This package contains library source intended for building other packages which
use the "ro" feature of the "%{crate}" crate.

%package     -n %{name}+ru-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+ru-devel

This package contains library source intended for building other packages which
use the "ru" feature of the "%{crate}" crate.

%package     -n %{name}+rust-stemmers-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+rust-stemmers-devel

This package contains library source intended for building other packages which
use the "rust-stemmers" feature of the "%{crate}" crate.

%package     -n %{name}+sv-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+sv-devel

This package contains library source intended for building other packages which
use the "sv" feature of the "%{crate}" crate.

%package     -n %{name}+tr-devel
Summary:        Generate static document search indexes
BuildArch:      noarch
%description -n %{name}+tr-devel

This package contains library source intended for building other packages which
use the "tr" feature of the "%{crate}" crate.

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
%files -n rust-elasticlunr-rs-devel -f %{oreon_filedir}/rust-elasticlunr-rs-devel.list

%changelog

%autochangelog
