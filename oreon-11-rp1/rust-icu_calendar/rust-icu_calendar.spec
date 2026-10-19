%global source0_hash 58655df2f728e46e4eee80bddebefacf52ec3e77cdb925014b47c5a5905eb55c
%bcond check 1
%global debug_package %{nil}
%global crate icu_calendar
Name:           rust-icu_calendar
Version:        2.3.0
Release:        1%{?dist}
Summary:        Date APIs for Gregorian and non-Gregorian calendars
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_calendar
Source0:        https://static.crates.io/crates/icu_calendar/icu_calendar-%{version}.crate
Patch:          icu_calendar-fix-metadata.diff
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
Summary:        Date APIs for Gregorian and non-Gregorian calendars
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Date APIs for Gregorian and non-Gregorian calendars
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+compiled_data-devel
Summary:        Date APIs for Gregorian and non-Gregorian calendars
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%package     -n %{name}+datagen-devel
Summary:        Date APIs for Gregorian and non-Gregorian calendars
BuildArch:      noarch
%description -n %{name}+datagen-devel

This package contains library source intended for building other packages which
use the "datagen" feature of the "%{crate}" crate.

%package     -n %{name}+ixdtf-devel
Summary:        Date APIs for Gregorian and non-Gregorian calendars
BuildArch:      noarch
%description -n %{name}+ixdtf-devel

This package contains library source intended for building other packages which
use the "ixdtf" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Date APIs for Gregorian and non-Gregorian calendars
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Date APIs for Gregorian and non-Gregorian calendars
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Date APIs for Gregorian and non-Gregorian calendars
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed -r -i \
's@([[:blank:]]*)(#\[ignore.*\bnetwork\b.*)@\1#[cfg(false)]\n&@' \
src/cal/east_asian_traditional.rs
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a -- --lib -- --exact --skip cal::east_asian_traditional_internal::simple::bounds
%cargo_test -a -- --test arithmetic -- --exact --skip cal::east_asian_traditional_internal::simple::bounds
%cargo_test -a -- --test exhaustive -- --exact --skip cal::east_asian_traditional_internal::simple::bounds
%cargo_test -a -- --test extended_year -- --exact --skip cal::east_asian_traditional_internal::simple::bounds
%cargo_test -a -- --test reference_year -- --exact --skip cal::east_asian_traditional_internal::simple::bounds
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-icu_calendar-devel -f %{oreon_filedir}/rust-icu_calendar-devel.list

%changelog

%autochangelog
