%global source0_hash ea6be833b323a56361118a747470a45a1bcd5c52a2ec9b1e40c83dafe687e453
%bcond check 1
%global debug_package %{nil}
%global crate fake
Name:           rust-fake
Version:        5.1.0
Release:        1%{?dist}
Summary:        Easy to use library for generating fake data
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fake
Source0:        https://static.crates.io/crates/fake/fake-%{version}.crate
Patch:          fake-fix-metadata.diff
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
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+always-true-rng-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+always-true-rng-devel

This package contains library source intended for building other packages which
use the "always-true-rng" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+bigdecimal-devel

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%package     -n %{name}+bigdecimal-rs-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+bigdecimal-rs-devel

This package contains library source intended for building other packages which
use the "bigdecimal-rs" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-tz-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+chrono-tz-devel

This package contains library source intended for building other packages which
use the "chrono-tz" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+dummy-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+dummy-devel

This package contains library source intended for building other packages which
use the "dummy" feature of the "%{crate}" crate.

%package     -n %{name}+either-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+either-devel

This package contains library source intended for building other packages which
use the "either" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+maybe-non-empty-collections-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+maybe-non-empty-collections-devel

This package contains library source intended for building other packages which
use the "maybe-non-empty-collections" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+rust_decimal-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+rust_decimal-devel

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%package     -n %{name}+semver-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+semver-devel

This package contains library source intended for building other packages which
use the "semver" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+ulid-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+ulid-devel

This package contains library source intended for building other packages which
use the "ulid" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+zerocopy-devel
Summary:        Easy to use library for generating fake data
BuildArch:      noarch
%description -n %{name}+zerocopy-devel

This package contains library source intended for building other packages which
use the "zerocopy" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f always-true-rng,derive
%install
%cargo_install -f always-true-rng,derive
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f always-true-rng,derive
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-fake-devel -f %{oreon_filedir}/rust-fake-devel.list

%changelog

%autochangelog
