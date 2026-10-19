%global source0_hash 413775a7eac2261d2211a79d10ef275e5b6f7b527eec42ad09adce2ffa92b6e5
%bcond check 1
%global debug_package %{nil}
%global crate parse_datetime
Name:           rust-parse_datetime
Version:        0.14.0
Release:        1%{?dist}
Summary:        Parsing human-readable time strings and converting them to a DateTime
License:        MIT
URL:            https://crates.io/crates/parse_datetime
Source0:        https://static.crates.io/crates/parse_datetime/parse_datetime-%{version}.crate
Patch:          parse_datetime-fix-metadata.diff
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
Summary:        Parsing human-readable time strings and converting them to a DateTime
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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

%{cargo_test -- -- %{shrink:
    --skip parse_relative_time::tests::test_days
    --skip parse_relative_time::tests::test_direction
    --skip parse_relative_time::tests::test_duration_parsing
    --skip parse_relative_time::tests::test_fortnights
    --skip parse_relative_time::tests::test_hours
    --skip parse_relative_time::tests::test_months
    --skip parse_relative_time::tests::test_relative_days
    --skip parse_datetime_at_date
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-parse_datetime-devel -f %{oreon_filedir}/rust-parse_datetime-devel.list

%changelog

%autochangelog
