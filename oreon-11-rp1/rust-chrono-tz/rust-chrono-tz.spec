%global source0_hash a6139a8597ed92cf816dfb33f5dd6cf0bb93a6adc938f11039f371bc5bcd26c3
%bcond check 0
%global debug_package %{nil}
%global crate chrono-tz
Name:           rust-chrono-tz
Version:        0.10.4
Release:        1%{?dist}
Summary:        TimeZone implementations for chrono from the IANA database
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/chrono-tz
Source0:        https://static.crates.io/crates/chrono-tz/chrono-tz-%{version}.crate
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
Summary:        TimeZone implementations for chrono from the IANA database
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        TimeZone implementations for chrono from the IANA database
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+case-insensitive-devel
Summary:        TimeZone implementations for chrono from the IANA database
BuildArch:      noarch
%description -n %{name}+case-insensitive-devel

This package contains library source intended for building other packages which
use the "case-insensitive" feature of the "%{crate}" crate.

%package     -n %{name}+filter-by-regex-devel
Summary:        TimeZone implementations for chrono from the IANA database
BuildArch:      noarch
%description -n %{name}+filter-by-regex-devel

This package contains library source intended for building other packages which
use the "filter-by-regex" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        TimeZone implementations for chrono from the IANA database
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        TimeZone implementations for chrono from the IANA database
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-chrono-tz-devel -f %{oreon_filedir}/rust-chrono-tz-devel.list

%changelog

%autochangelog
