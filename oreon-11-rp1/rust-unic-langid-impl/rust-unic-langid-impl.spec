%global source0_hash dce1bf08044d4b7a94028c93786f8566047edc11110595914de93362559bc658
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate unic-langid-impl
Name:           rust-unic-langid-impl
Version:        0.9.6
Release:        1%{?dist}
Summary:        API for managing Unicode Language Identifiers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unic-langid-impl
Source0:        https://static.crates.io/crates/unic-langid-impl/unic-langid-impl-%{version}.crate
Patch:          unic-langid-impl-fix-metadata.diff
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

%package     -n %{name}+binary-devel
Summary:        API for managing Unicode Language Identifiers
BuildArch:      noarch
%description -n %{name}+binary-devel

This package contains library source intended for building other packages which
use the "binary" feature of the "%{crate}" crate.

%package     -n %{name}+likelysubtags-devel
Summary:        API for managing Unicode Language Identifiers
BuildArch:      noarch
%description -n %{name}+likelysubtags-devel

This package contains library source intended for building other packages which
use the "likelysubtags" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        API for managing Unicode Language Identifiers
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        API for managing Unicode Language Identifiers
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f binary
%install
%cargo_install -f binary
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f binary -- -- --exact --skip parse
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-unic-langid-impl-devel -f %{oreon_filedir}/rust-unic-langid-impl-devel.list

%changelog

%autochangelog
