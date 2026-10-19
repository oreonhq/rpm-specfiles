%global source0_hash a28ba52c9b05311f4f6e62d5d9d46f094bd6e84cb8df7b3ef952748d752a7d05
%bcond check 1
%global debug_package %{nil}
%global crate unic-langid
Name:           rust-unic-langid
Version:        0.9.6
Release:        1%{?dist}
Summary:        API for managing Unicode Language Identifiers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unic-langid
Source0:        https://static.crates.io/crates/unic-langid/unic-langid-%{version}.crate
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
Summary:        API for managing Unicode Language Identifiers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+likelysubtags-devel
Summary:        API for managing Unicode Language Identifiers
BuildArch:      noarch
%description -n %{name}+likelysubtags-devel

This package contains library source intended for building other packages which
use the "likelysubtags" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        API for managing Unicode Language Identifiers
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        API for managing Unicode Language Identifiers
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+unic-langid-macros-devel
Summary:        API for managing Unicode Language Identifiers
BuildArch:      noarch
%description -n %{name}+unic-langid-macros-devel

This package contains library source intended for building other packages which
use the "unic-langid-macros" feature of the "%{crate}" crate.

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
%files -n rust-unic-langid-devel -f %{oreon_filedir}/rust-unic-langid-devel.list

%changelog

%autochangelog
