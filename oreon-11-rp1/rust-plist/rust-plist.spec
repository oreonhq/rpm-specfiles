%global source0_hash 2896bade328c13f7042a297ea5ac5b0951f6cf989dea5f32c2fd98da398195cb
%bcond check 0
%global debug_package %{nil}
%global crate plist
Name:           rust-plist
Version:        1.10.1
Release:        1%{?dist}
Summary:        A rusty plist parser. Supports Serde serialization.
License:        MIT
URL:            https://crates.io/crates/plist
Source0:        https://static.crates.io/crates/plist/plist-%{version}.crate
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
Summary:        A rusty plist parser. Supports Serde serialization.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+enable_unstable_features_that_may_break_with_minor_version_bumps-devel
Summary:        A rusty plist parser. Supports Serde serialization.
BuildArch:      noarch
%description -n %{name}+enable_unstable_features_that_may_break_with_minor_version_bumps-devel

This package contains library source intended for building other packages which
use the "enable_unstable_features_that_may_break_with_minor_version_bumps" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A rusty plist parser. Supports Serde serialization.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-plist-devel -f %{oreon_filedir}/rust-plist-devel.list

%changelog

%autochangelog
