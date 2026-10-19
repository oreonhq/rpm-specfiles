%global source0_hash c44df99c4c5297b05653d1a1629f13bdc9fd4044acfbbaf30b15194a1eed4cd6
%bcond check 1
%global debug_package %{nil}
%global crate icu_datetime
Name:           rust-icu_datetime
Version:        2.3.0
Release:        1%{?dist}
Summary:        Human-readable formatting of dates, times, and time zones in hundreds of locales
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_datetime
Source0:        https://static.crates.io/crates/icu_datetime/icu_datetime-%{version}.crate
Patch:          icu_datetime-fix-metadata.diff
Patch10:        0001-In-icu_datetime-limit-use-of-the-icu-crate-to-doctes.patch
Patch11:        0002-Downstream-only-omit-a-test-that-would-require-icu_p.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Human-readable formatting of dates, times, and time zones in hundreds of locales
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+compiled_data-devel
Summary:        Human-readable formatting of dates, times, and time zones in hundreds of locales
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%package     -n %{name}+datagen-devel
Summary:        Human-readable formatting of dates, times, and time zones in hundreds of locales
BuildArch:      noarch
%description -n %{name}+datagen-devel

This package contains library source intended for building other packages which
use the "datagen" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-devel
Summary:        Human-readable formatting of dates, times, and time zones in hundreds of locales
BuildArch:      noarch
%description -n %{name}+experimental-devel

This package contains library source intended for building other packages which
use the "experimental" feature of the "%{crate}" crate.

%package     -n %{name}+ixdtf-devel
Summary:        Human-readable formatting of dates, times, and time zones in hundreds of locales
BuildArch:      noarch
%description -n %{name}+ixdtf-devel

This package contains library source intended for building other packages which
use the "ixdtf" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Human-readable formatting of dates, times, and time zones in hundreds of locales
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Human-readable formatting of dates, times, and time zones in hundreds of locales
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tomcli set Cargo.toml str dev-dependencies.icu_calendar.version '~%{version}'
tomcli set Cargo.toml list dev-dependencies.icu_calendar.features \
ixdtf unstable
tomcli set Cargo.toml str dev-dependencies.icu_time.version '~%{version}'
tomcli set Cargo.toml list dev-dependencies.icu_time.features ixdtf alloc
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a -- --lib
%cargo_test -a -- --test datetime
%cargo_test -a -- --test hijri_iran
%cargo_test -a -- --test pattern_serialization
%cargo_test -a -- --test resolved_components
%cargo_test -a -- --test simple_test
%cargo_test -a -- --test skeleton_serialization
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-icu_datetime-devel -f %{oreon_filedir}/rust-icu_datetime-devel.list

%changelog

%autochangelog
