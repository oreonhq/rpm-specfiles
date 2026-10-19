%global source0_hash e194c4067397d33af959dcdf13614bc5f57c578da48a9c7d64047c6cc7487b62
%bcond check 1
%global debug_package %{nil}
%global crate unic-locale
Name:           rust-unic-locale
Version:        0.9.6
Release:        1%{?dist}
Summary:        API for managing Unicode Locale Identifiers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unic-locale
Source0:        https://static.crates.io/crates/unic-locale/unic-locale-%{version}.crate
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
Summary:        API for managing Unicode Locale Identifiers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+likelysubtags-devel
Summary:        API for managing Unicode Locale Identifiers
BuildArch:      noarch
%description -n %{name}+likelysubtags-devel

This package contains library source intended for building other packages which
use the "likelysubtags" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        API for managing Unicode Locale Identifiers
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+unic-locale-macros-devel
Summary:        API for managing Unicode Locale Identifiers
BuildArch:      noarch
%description -n %{name}+unic-locale-macros-devel

This package contains library source intended for building other packages which
use the "unic-locale-macros" feature of the "%{crate}" crate.

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
%files -n rust-unic-locale-devel -f %{oreon_filedir}/rust-unic-locale-devel.list

%changelog

%autochangelog
